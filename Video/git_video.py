#!/usr/bin/env python3
"""
git_video.py — Visualizes the git history of the Text Adventure project as a video.

Requires: pip install matplotlib pillow imageio imageio-ffmpeg
Output:   git_history.mp4
"""

import subprocess
import datetime
import math
import io
import imageio
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
from PIL import Image

# ─── Git log parsing ──────────────────────────────────────────────────────────

def run(cmd):
    return subprocess.check_output(cmd, shell=True, text=True, cwd="/home/user/text_adventure")

def parse_git_history():
    """Return a list of commits sorted by timestamp (oldest first)."""
    raw = run("git log --all --name-status --format='COMMIT|%at|%an|%s'")
    commits = []
    current = None
    for line in raw.splitlines():
        if line.startswith("COMMIT|"):
            if current:
                commits.append(current)
            _, ts, author, msg = line.split("|", 3)
            current = {
                "timestamp": int(ts),
                "author": author,
                "message": msg,
                "files": [],
            }
        elif line and current:
            parts = line.split("\t")
            if len(parts) >= 2:
                status = parts[0][0]  # A / M / D / R
                fname = parts[-1]
                current["files"].append((status, fname))
    if current:
        commits.append(current)

    # Sort oldest → newest, skip pure merge commits (no files)
    commits.sort(key=lambda c: c["timestamp"])
    commits = [c for c in commits if c["files"] or c["message"].startswith("Merge") == False]
    return commits


# ─── Colour palette ───────────────────────────────────────────────────────────

BG        = "#0d1117"
GRID      = "#21262d"
TITLE_C   = "#e6edf3"
SUB_C     = "#8b949e"
ADD_C     = "#3fb950"   # green  – added / new
MOD_C     = "#d29922"   # yellow – modified
DEL_C     = "#f85149"   # red    – deleted

FILE_COLORS = {
    "game.py":          "#79c0ff",
    "rooms.py":         "#ffa657",
    "maps.py":          "#a5d6ff",
    "codierer.py":      "#d2a8ff",
    "text_adventure.py":"#79c0ff",
    ".gitignore":       "#8b949e",
}
DEFAULT_FILE_COLOR = "#58a6ff"

AUTHOR_COLORS = {
    "NKRACKER":         "#ffa657",
    "Claude":           "#79c0ff",
    "Nathanael Kroeker":"#ffa657",
}

WIDTH,  HEIGHT = 1280, 720
FPS    = 30
FRAMES_PER_COMMIT = 60   # 2 s per commit at 30 fps
HOLD_FRAMES        = 15  # brief pause between commits

# ─── File-size tracking ───────────────────────────────────────────────────────

def get_file_sizes(commits):
    """Return list of dicts {fname: size_in_lines} per commit."""
    sizes_over_time = []
    current = {}

    for c in commits:
        # Use git show to get file sizes at this commit's state
        sha = get_sha_for_commit(c)
        for status, fname in c["files"]:
            if status == "D":
                current.pop(fname, None)
            else:
                try:
                    out = subprocess.check_output(
                        f"git show {sha}:{fname} 2>/dev/null | wc -l",
                        shell=True, text=True, cwd="/home/user/text_adventure"
                    )
                    current[fname] = int(out.strip())
                except Exception:
                    current[fname] = current.get(fname, 0)
        sizes_over_time.append(dict(current))
    return sizes_over_time


def get_sha_for_commit(c):
    # Re-find SHA from timestamp + message
    out = run(f"git log --all --format='%at|%H|%s'")
    for line in out.splitlines():
        parts = line.split("|", 2)
        if len(parts) == 3 and int(parts[0]) == c["timestamp"] and parts[2] == c["message"]:
            return parts[1]
    return "HEAD"


# ─── Frame rendering ──────────────────────────────────────────────────────────

def render_frame(commits, sizes_over_time, commit_idx, progress, cumulative_changes):
    """
    Render one frame.
    commit_idx : which commit we're currently on
    progress   : 0.0 → 1.0 within this commit's animation
    """
    c   = commits[commit_idx]
    cur = sizes_over_time[commit_idx]

    fig = plt.figure(figsize=(WIDTH / 100, HEIGHT / 100), dpi=100, facecolor=BG)
    ax  = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor(BG)
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)
    ax.axis("off")

    # ── Header bar ──────────────────────────────────────────────────────────
    ax.add_patch(plt.Rectangle((0, HEIGHT - 70), WIDTH, 70, color="#161b22", zorder=1))
    ax.text(20, HEIGHT - 28, "Text Adventure", fontsize=20, fontweight="bold",
            color=TITLE_C, va="center", zorder=2, fontfamily="monospace")
    ax.text(20, HEIGHT - 52, "Git History Visualization", fontsize=11,
            color=SUB_C, va="center", zorder=2)

    # date
    dt = datetime.datetime.fromtimestamp(c["timestamp"]).strftime("%Y-%m-%d  %H:%M")
    ax.text(WIDTH - 20, HEIGHT - 28, dt, fontsize=11, color=SUB_C,
            va="center", ha="right", zorder=2, fontfamily="monospace")

    # ── Author badge ────────────────────────────────────────────────────────
    a_col = AUTHOR_COLORS.get(c["author"], DEFAULT_FILE_COLOR)
    ax.add_patch(FancyBboxPatch((WIDTH - 200, HEIGHT - 64), 180, 22,
                                boxstyle="round,pad=3", color=a_col, alpha=0.25, zorder=2))
    ax.text(WIDTH - 110, HEIGHT - 53, c["author"], fontsize=10,
            color=a_col, va="center", ha="center", fontweight="bold", zorder=3)

    # ── Commit message ───────────────────────────────────────────────────────
    msg = c["message"]
    if len(msg) > 68:
        msg = msg[:65] + "…"
    ax.text(WIDTH / 2, HEIGHT - 90, f'"{msg}"', fontsize=12, color=TITLE_C,
            va="top", ha="center", style="italic", zorder=2)

    # ── File bubbles ─────────────────────────────────────────────────────────
    # Layout: arrange files in a circular cluster
    all_files = sorted(cur.items(), key=lambda x: -x[1])
    max_lines  = max((v for _, v in all_files), default=1)
    cx, cy     = WIDTH / 2, HEIGHT / 2 + 10

    n = len(all_files)
    for i, (fname, lines) in enumerate(all_files):
        angle  = 2 * math.pi * i / max(n, 1) - math.pi / 2
        radius = 200 if n > 1 else 0
        bx     = cx + radius * math.cos(angle)
        by     = cy + radius * math.sin(angle)

        # Bubble size proportional to lines
        size = 20 + 80 * (lines / max_lines)

        # Colour: highlight files changed in this commit
        changed_files = [f for _, f in c["files"]]
        col = FILE_COLORS.get(fname, DEFAULT_FILE_COLOR)
        alpha = 0.9 if fname in changed_files else 0.35

        # Animate: pulse on appearance
        if fname in changed_files and progress < 0.5:
            pulse = 1 + 0.3 * math.sin(progress * math.pi * 4)
            size *= pulse

        circle = plt.Circle((bx, by), size / 2, color=col, alpha=alpha, zorder=3)
        ax.add_patch(circle)

        # Label
        short = fname.replace(".py", "")
        ax.text(bx, by, short, fontsize=8, color=BG if alpha > 0.5 else col,
                va="center", ha="center", fontweight="bold", zorder=4)
        ax.text(bx, by - size / 2 - 8, f"{lines} lines", fontsize=7, color=SUB_C,
                va="top", ha="center", zorder=4)

    # ── Changed files list (right panel) ─────────────────────────────────────
    panel_x = WIDTH - 260
    ax.add_patch(plt.Rectangle((panel_x - 10, 80), 260, HEIGHT - 180,
                                color="#161b22", alpha=0.8, zorder=2))
    ax.text(panel_x, HEIGHT - 110, "Changed Files", fontsize=11,
            color=SUB_C, va="top", fontweight="bold", zorder=3)

    for j, (status, fname) in enumerate(c["files"][:12]):
        y = HEIGHT - 135 - j * 22
        s_col = ADD_C if status == "A" else (DEL_C if status == "D" else MOD_C)
        s_sym = "+" if status == "A" else ("−" if status == "D" else "~")
        # Animate: fade in
        alpha_f = min(1.0, progress * 3 - j * 0.15) if progress > 0 else 0
        alpha_f = max(0, alpha_f)
        ax.text(panel_x, y, f"{s_sym}  {fname}", fontsize=9, color=s_col,
                va="top", fontfamily="monospace", alpha=alpha_f, zorder=3)

    # ── Timeline bar ─────────────────────────────────────────────────────────
    bar_y   = 50
    bar_h   = 12
    bar_x0  = 20
    bar_w   = WIDTH - 300

    # Background
    ax.add_patch(plt.Rectangle((bar_x0, bar_y), bar_w, bar_h,
                                color=GRID, zorder=2, linewidth=0))
    # Progress
    pct = (commit_idx + progress) / len(commits)
    ax.add_patch(plt.Rectangle((bar_x0, bar_y), bar_w * pct, bar_h,
                                color="#1f6feb", zorder=3, linewidth=0))
    # Current position dot
    dot_x = bar_x0 + bar_w * pct
    ax.plot(dot_x, bar_y + bar_h / 2, "o", color="#58a6ff", ms=10, zorder=4)

    ax.text(bar_x0, bar_y - 10, f"Commit {commit_idx + 1} / {len(commits)}",
            fontsize=9, color=SUB_C, va="top", zorder=2)

    # ── Stats bottom-left ────────────────────────────────────────────────────
    total_lines = sum(cur.values())
    ax.text(20, 30, f"Total lines: {total_lines:,}  |  Files: {len(cur)}",
            fontsize=9, color=SUB_C, va="bottom", fontfamily="monospace", zorder=2)

    # ── Render to numpy array ─────────────────────────────────────────────────
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches=None, pad_inches=0, dpi=100)
    plt.close(fig)
    buf.seek(0)
    img = Image.open(buf).convert("RGB")
    return np.array(img)


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    print("Parsing git history…")
    commits = parse_git_history()
    print(f"  {len(commits)} commits found.")

    print("Collecting file sizes per commit (this may take a moment)…")
    sizes_over_time = get_file_sizes(commits)

    out_path = "/home/user/text_adventure/git_history.mp4"
    print(f"Rendering video → {out_path}")

    cumulative = {}
    writer = imageio.get_writer(
        out_path,
        fps=FPS,
        codec="libx264",
        quality=8,
        macro_block_size=16,
        ffmpeg_params=["-pix_fmt", "yuv420p", "-movflags", "+faststart"],
    )

    for idx, commit in enumerate(commits):
        print(f"  [{idx + 1:2d}/{len(commits)}] {commit['message'][:55]}")

        # Animate this commit over FRAMES_PER_COMMIT frames
        for f in range(FRAMES_PER_COMMIT):
            progress = f / FRAMES_PER_COMMIT
            frame = render_frame(commits, sizes_over_time, idx, progress, cumulative)
            writer.append_data(frame)

        # Hold on last frame briefly
        final_frame = render_frame(commits, sizes_over_time, idx, 1.0, cumulative)
        for _ in range(HOLD_FRAMES):
            writer.append_data(final_frame)

    writer.close()
    import os
    size_mb = os.path.getsize(out_path) / 1_000_000
    print(f"\nDone!  {out_path}  ({size_mb:.1f} MB)")


if __name__ == "__main__":
    main()

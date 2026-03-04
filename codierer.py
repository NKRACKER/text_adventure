from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
from collections import deque


VALID_DIRECTIONS = ("n", "e", "s", "w")
OPPOSITE = {"n": "s", "s": "n", "e": "w", "w": "e"}


@dataclass
class RoomData:
    idx: int
    name: str
    story: str
    locked: bool
    kill: bool
    secret: bool
    items: List[str] = field(default_factory=list)
    mapping: Dict[str, int] = field(default_factory=dict)
    x: Optional[int] = None
    y: Optional[int] = None


def ask(prompt: str) -> str:
    return input(prompt).strip()


def ask_int(prompt: str, min_value: int | None = None) -> int:
    while True:
        raw = ask(prompt)
        try:
            value = int(raw)
            if min_value is not None and value < min_value:
                print(f"Bitte eine Zahl >= {min_value} eingeben.")
                continue
            return value
        except ValueError:
            print("Bitte eine gültige Zahl eingeben.")


def ask_optional_int(prompt: str) -> Optional[int]:
    while True:
        raw = ask(prompt)
        if raw == "":
            return None
        try:
            return int(raw)
        except ValueError:
            print("Bitte eine Zahl oder leer eingeben.")


def ask_yes_no(prompt: str) -> bool:
    while True:
        raw = ask(f"{prompt} [y/n]: ").lower()
        if raw in {"y", "yes", "j", "ja"}:
            return True
        if raw in {"n", "no", "nein"}:
            return False
        print("Bitte y oder n eingeben.")


def ask_items(prompt: str) -> List[str]:
    raw = ask(prompt)
    if not raw:
        return []
    return [item.strip() for item in raw.split(",") if item.strip()]


def ask_direction_target(room_count: int, direction: str) -> Optional[int]:
    while True:
        raw = ask(
            f"Zielraum für Richtung '{direction}' "
            f"(0 bis {room_count - 1}, leer = kein Ausgang): "
        )
        if raw == "":
            return None
        try:
            target = int(raw)
            if 0 <= target < room_count:
                return target
            print(f"Bitte eine Zahl zwischen 0 und {room_count - 1} eingeben.")
        except ValueError:
            print("Bitte eine gültige Zahl eingeben.")


def py_string(value: str) -> str:
    return repr(value)


def build_room_var(map_number: int, room_idx: int) -> str:
    return f"room{map_number}_{room_idx}"


def create_rooms_interactively() -> tuple[int, List[RoomData]]:
    print("=== Room- und Mapping-Generator V2 ===")
    map_number = ask_int("Map-Nummer eingeben (z. B. 2, 3, 4, 5): ", min_value=1)
    room_count = ask_int("Wie viele Räume soll die Map haben? ", min_value=1)

    use_coordinates = ask_yes_no(
        "Willst du optionale x/y-Koordinaten für eine bessere ASCII-Karte eingeben?"
    )

    rooms: List[RoomData] = []

    print("\n=== Räume anlegen ===")
    for i in range(room_count):
        print(f"\nRaum {i}")
        auto_name = ask_yes_no("Automatischen Namen im Stil '[i] Name' benutzen?")
        if auto_name:
            short_name = ask("Kurzer Raumname: ")
            name = f"[{i}] {short_name}"
        else:
            name = ask("Voller Raumname: ")

        story = ask("Story/Beschreibung: ")
        locked = ask_yes_no("Locked?")
        kill = ask_yes_no("Kill-Raum?")
        secret = ask_yes_no("Secret-Raum?")
        items = ask_items("Items (kommagetrennt, leer = keine): ")

        x = y = None
        if use_coordinates:
            x = ask_optional_int("x-Koordinate (leer = keine): ")
            y = ask_optional_int("y-Koordinate (leer = keine): ")

        rooms.append(
            RoomData(
                idx=i,
                name=name,
                story=story,
                locked=locked,
                kill=kill,
                secret=secret,
                items=items,
                x=x,
                y=y,
            )
        )

    print("\n=== Mappings anlegen ===")
    print("Für jede Richtung leer lassen, wenn es keinen Ausgang gibt.\n")

    for room in rooms:
        print(f"\nMappings für Raum [{room.idx}] {room.name}")
        for direction in VALID_DIRECTIONS:
            target = ask_direction_target(room_count, direction)
            if target is not None:
                room.mapping[direction] = target

    return map_number, rooms


def build_room_definitions(map_number: int, rooms: List[RoomData]) -> str:
    lines: List[str] = [f"#################", f"#ROOMS_{map_number}"]

    for room in rooms:
        var_name = build_room_var(map_number, room.idx)

        args: List[str] = [
            f"name={py_string(room.name)}",
            f"story={py_string(room.story)}",
        ]
        if room.locked:
            args.append("locked=True")
        if room.kill:
            args.append("kill=True")
        if room.secret:
            args.append("secret=True")
        if room.items:
            item_list = ", ".join(py_string(item) for item in room.items)
            args.append(f"items=[{item_list}]")

        joined_args = ",\n    ".join(args)

        lines.append(f"{var_name} = Room(")
        lines.append(f"    {joined_args}")
        lines.append(")")

    return "\n".join(lines)


def build_mapping_definitions(map_number: int, rooms: List[RoomData]) -> str:
    lines: List[str] = ["", f"#MAPPINGS_{map_number}"]

    for room in rooms:
        var_name = build_room_var(map_number, room.idx)
        if not room.mapping:
            lines.append(f"{var_name}.mapping = {{}}")
            continue

        lines.append(f"{var_name}.mapping = {{")
        for direction, target_idx in room.mapping.items():
            target_var = build_room_var(map_number, target_idx)
            lines.append(f'    "{direction}": {target_var},')
        lines.append("}")

    return "\n".join(lines)


def reachable_rooms(rooms: List[RoomData], start_idx: int = 0) -> List[int]:
    visited = set()
    stack = [start_idx]

    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        for target in rooms[current].mapping.values():
            if target not in visited:
                stack.append(target)

    return sorted(visited)


def find_one_way_edges(rooms: List[RoomData]) -> List[Tuple[int, str, int]]:
    one_way = []

    for room in rooms:
        for direction, target_idx in room.mapping.items():
            opposite = OPPOSITE[direction]
            target_room = rooms[target_idx]
            if target_room.mapping.get(opposite) != room.idx:
                one_way.append((room.idx, direction, target_idx))

    return one_way


def find_dead_ends(rooms: List[RoomData]) -> List[int]:
    return [room.idx for room in rooms if len(room.mapping) == 0]


def find_duplicate_coordinates(rooms: List[RoomData]) -> List[Tuple[int, int, List[int]]]:
    coords: Dict[Tuple[int, int], List[int]] = {}
    for room in rooms:
        if room.x is not None and room.y is not None:
            coords.setdefault((room.x, room.y), []).append(room.idx)

    duplicates = []
    for (x, y), idxs in coords.items():
        if len(idxs) > 1:
            duplicates.append((x, y, idxs))
    return duplicates


def all_have_coordinates(rooms: List[RoomData]) -> bool:
    return all(room.x is not None and room.y is not None for room in rooms)


def draw_text(grid: List[List[str]], x: int, y: int, text: str) -> None:
    for i, ch in enumerate(text):
        if 0 <= y < len(grid) and 0 <= x + i < len(grid[0]):
            grid[y][x + i] = ch


def render_coordinate_map(rooms: List[RoomData]) -> Tuple[str, List[str]]:
    cell_w = 8
    cell_h = 4

    min_x = min(room.x for room in rooms if room.x is not None)
    max_x = max(room.x for room in rooms if room.x is not None)
    min_y = min(room.y for room in rooms if room.y is not None)
    max_y = max(room.y for room in rooms if room.y is not None)

    width = (max_x - min_x + 1) * cell_w + 8
    height = (max_y - min_y + 1) * cell_h + 4

    grid = [[" " for _ in range(width)] for _ in range(height)]
    room_pos: Dict[int, Tuple[int, int, str]] = {}

    for room in rooms:
        label = f"[{room.idx}]"
        if room.kill:
            label = f"[{room.idx}X]"
        elif room.locked:
            label = f"[{room.idx}L]"
        elif room.secret:
            label = f"[{room.idx}S]"

        gx = (room.x - min_x) * cell_w
        gy = (room.y - min_y) * cell_h
        room_pos[room.idx] = (gx, gy, label)
        draw_text(grid, gx, gy, label)

    skipped: List[str] = []
    drawn_undirected = set()

    def has_reverse(source_idx: int, direction: str, target_idx: int) -> bool:
        opposite = OPPOSITE[direction]
        return rooms[target_idx].mapping.get(opposite) == source_idx

    for room in rooms:
        sx, sy, slabel = room_pos[room.idx]
        s_center_x = sx + len(slabel) // 2
        s_center_y = sy

        for direction, target_idx in room.mapping.items():
            tx, ty, tlabel = room_pos[target_idx]
            t_center_x = tx + len(tlabel) // 2
            t_center_y = ty

            bidirectional = has_reverse(room.idx, direction, target_idx)

            if bidirectional:
                pair = tuple(sorted((room.idx, target_idx)))
                if pair in drawn_undirected:
                    continue
                drawn_undirected.add(pair)

            if sy == ty:
                left_x = min(sx, tx)
                right_x = max(sx, tx)
                left_label = slabel if sx < tx else tlabel
                right_label = tlabel if sx < tx else slabel

                start = left_x + len(left_label)
                end = right_x - 1
                if end <= start:
                    skipped.append(f"{room.idx}->{target_idx} (horizontal zu nah)")
                    continue

                if bidirectional:
                    for x in range(start, end):
                        grid[sy][x] = "-"
                else:
                    if sx < tx:
                        for x in range(start, end - 1):
                            grid[sy][x] = "="
                        grid[sy][end - 1] = ">"
                    else:
                        grid[sy][start] = "<"
                        for x in range(start + 1, end):
                            grid[sy][x] = "="

            elif sx == tx:
                top_y = min(sy, ty)
                bottom_y = max(sy, ty)
                start = top_y + 1
                end = bottom_y
                if end <= start:
                    skipped.append(f"{room.idx}->{target_idx} (vertikal zu nah)")
                    continue

                if bidirectional:
                    for y in range(start, end):
                        grid[y][sx] = "|"
                else:
                    if sy < ty:
                        for y in range(start, end - 1):
                            grid[y][sx] = "|"
                        grid[end - 1][sx] = "v"
                    else:
                        grid[start][sx] = "^"
                        for y in range(start + 1, end):
                            grid[y][sx] = "|"
            else:
                skipped.append(f"{room.idx}->{target_idx} (nicht gerade zeichnbar)")

    lines = ["".join(row).rstrip() for row in grid]
    while lines and lines[-1] == "":
        lines.pop()

    return "\n".join(lines), skipped


def render_schematic_map(rooms: List[RoomData], start_idx: int = 0) -> str:
    visited = set()
    levels: Dict[int, List[int]] = {}
    q = deque([(start_idx, 0)])

    while q:
        node, depth = q.popleft()
        if node in visited:
            continue
        visited.add(node)
        levels.setdefault(depth, []).append(node)

        for target in rooms[node].mapping.values():
            if target not in visited:
                q.append((target, depth + 1))

    lines = ["Schematische Übersicht:"]
    for depth in sorted(levels):
        labels = []
        for idx in levels[depth]:
            room = rooms[idx]
            suffix = ""
            if room.kill:
                suffix = "X"
            elif room.locked:
                suffix = "L"
            elif room.secret:
                suffix = "S"
            labels.append(f"[{idx}{suffix}]")
        lines.append(f"Ebene {depth}: " + " -- ".join(labels))

    lines.append("")
    lines.append("Verbindungen:")
    for room in rooms:
        parts = []
        for direction, target in room.mapping.items():
            opposite = OPPOSITE[direction]
            if rooms[target].mapping.get(opposite) == room.idx:
                arrow = "--"
            else:
                arrow = "=>"
            parts.append(f"{direction} {arrow} [{target}]")
        joined = ", ".join(parts) if parts else "(keine)"
        lines.append(f"[{room.idx}] {joined}")

    return "\n".join(lines)


def build_map_function(map_number: int, map_text: str) -> str:
    indented = "\n".join(map_text.splitlines())
    return f'''def map{map_number}():
    return r"""
{indented}
"""
'''


def build_preview(rooms: List[RoomData]) -> str:
    lines: List[str] = ["", "===== VORSCHAU ====="]
    for room in rooms:
        lines.append(f"[{room.idx}] {room.name}")
        flags: List[str] = []
        if room.locked:
            flags.append("locked")
        if room.kill:
            flags.append("kill")
        if room.secret:
            flags.append("secret")
        if room.items:
            flags.append(f"items={room.items}")
        if room.x is not None and room.y is not None:
            flags.append(f"pos=({room.x},{room.y})")
        if flags:
            lines.append("  " + ", ".join(flags))
        if room.story:
            lines.append(f"  story: {room.story}")
        if room.mapping:
            pretty_mapping = ", ".join(f"{d}->{t}" for d, t in room.mapping.items())
            lines.append(f"  mapping: {pretty_mapping}")
        else:
            lines.append("  mapping: {{}}")
    return "\n".join(lines)


def build_analysis_report(rooms: List[RoomData]) -> str:
    reachable = reachable_rooms(rooms)
    all_indices = [room.idx for room in rooms]
    unreachable = [idx for idx in all_indices if idx not in reachable]

    one_way = find_one_way_edges(rooms)
    dead_ends = find_dead_ends(rooms)
    duplicate_coords = find_duplicate_coordinates(rooms)

    lines = ["", "===== ANALYSE ====="]
    lines.append(f"Erreichbar von Raum 0: {reachable}")

    if unreachable:
        lines.append(f"NICHT erreichbar von Raum 0: {unreachable}")
    else:
        lines.append("Alle Räume sind von Raum 0 erreichbar.")

    if one_way:
        lines.append("Einbahnstraßen / asymmetrische Wege:")
        for src, direction, dst in one_way:
            lines.append(f"  [{src}] -{direction}-> [{dst}]")
    else:
        lines.append("Keine Einbahnstraßen gefunden.")

    if dead_ends:
        lines.append(f"Tote Enden (keine Ausgänge): {dead_ends}")
    else:
        lines.append("Keine toten Enden gefunden.")

    if duplicate_coords:
        lines.append("Doppelte Koordinaten:")
        for x, y, idxs in duplicate_coords:
            lines.append(f"  ({x},{y}): Räume {idxs}")
    else:
        lines.append("Keine doppelten Koordinaten gefunden.")

    return "\n".join(lines)


def save_output(text: str) -> None:
    if not ask_yes_no("\nSoll der erzeugte Code in eine Datei gespeichert werden?"):
        return

    filename = ask("Dateiname (z. B. generated_map.py): ")
    if not filename:
        filename = "generated_map.py"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"Datei gespeichert: {filename}")


def main() -> None:
    map_number, rooms = create_rooms_interactively()

    print(build_preview(rooms))
    print(build_analysis_report(rooms))

    if all_have_coordinates(rooms) and not find_duplicate_coordinates(rooms):
        map_text, skipped = render_coordinate_map(rooms)
        print("\n===== ASCII-KARTE (mit Koordinaten) =====\n")
        print(map_text)
        if skipped:
            print("\nNicht direkt zeichnbare Verbindungen:")
            for entry in skipped:
                print(" -", entry)
    else:
        map_text = render_schematic_map(rooms)
        print("\n===== SCHEMATISCHE ÜBERSICHT =====\n")
        print(map_text)

    rooms_code = (
        build_room_definitions(map_number, rooms)
        + "\n"
        + build_mapping_definitions(map_number, rooms)
        + "\n"
    )

    maps_code = build_map_function(map_number, map_text)

    print("\n===== ROOMS.PY-CODE =====\n")
    print(rooms_code)

    print("\n===== MAPS.PY-CODE =====\n")
    print(maps_code)

    combined = (
        "# ===== ROOMS.PY BLOCK =====\n"
        + rooms_code
        + "\n# ===== MAPS.PY BLOCK =====\n"
        + maps_code
    )

    save_output(combined)


if __name__ == "__main__":
    main()
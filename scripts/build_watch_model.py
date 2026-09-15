"""Build assets/cad/fallout-smartwatch/model.glb for the homepage 3D viewer.

Real geometry (preferred):
    Export each part from SolidWorks as a separate .stl (File -> Save As -> STL,
    no Blender needed) into assets/cad/fallout-smartwatch/stl/:
        body.stl
        wrist-band.stl
        volume-knob.stl
        power-button-screen.stl
    Then run:  python scripts/build_watch_model.py
    This colors each part and merges them into model.glb.

Placeholder fallback:
    If no .stl files are found, this script builds a rough boxes-and-cylinders
    stand-in with the same proportions/colors as the real design, so the site's
    3D viewer has something to show before the real exports exist. It gets
    overwritten automatically once real .stl files are dropped in and this
    script is re-run.
"""

import sys
from pathlib import Path

import numpy as np
import trimesh

ROOT = Path(__file__).resolve().parent.parent
PROJECT_DIR = ROOT / "assets" / "cad" / "fallout-smartwatch"
STL_DIR = PROJECT_DIR / "stl"
OUTPUT = PROJECT_DIR / "model.glb"

# Color scheme lifted from the concept render: tan/salmon strap, mustard-gold
# body chassis, dark screen bezel, light screen, dark knurled knob.
PART_COLORS = {
    "body": (198, 148, 82, 255),
    "wrist-band": (222, 163, 118, 255),
    "volume-knob": (58, 58, 58, 255),
    "power-button-screen": (44, 46, 48, 255),
}
DEFAULT_COLOR = (170, 170, 175, 255)


def colorize(mesh: trimesh.Trimesh, rgba) -> trimesh.Trimesh:
    mesh.visual = trimesh.visual.ColorVisuals(
        mesh, vertex_colors=np.tile(rgba, (len(mesh.vertices), 1))
    )
    return mesh


def build_from_stl() -> trimesh.Scene | None:
    if not STL_DIR.exists():
        return None
    stl_files = sorted(STL_DIR.glob("*.stl"))
    if not stl_files:
        return None

    scene = trimesh.Scene()
    for path in stl_files:
        mesh = trimesh.load(path, force="mesh")
        color = PART_COLORS.get(path.stem, DEFAULT_COLOR)
        colorize(mesh, color)
        scene.add_geometry(mesh, node_name=path.stem)

    # Normalize scale/position: center on the body, unit-ish size so
    # <model-viewer>'s default camera framing looks reasonable.
    extents = scene.bounds
    center = extents.mean(axis=0)
    size = (extents[1] - extents[0]).max()
    scale = 1.0 / size if size else 1.0
    scene.apply_translation(-center)
    scene.apply_scale(scale)
    return scene


def wedge(length, width_a, width_b, thickness):
    """A simple tapered strap segment: wide at one end, narrow at the other."""
    hl, ha, hb, ht = length / 2, width_a / 2, width_b / 2, thickness / 2
    vertices = np.array(
        [
            [-hl, -ha, -ht], [-hl, ha, -ht], [-hl, ha, ht], [-hl, -ha, ht],
            [hl, -hb, -ht], [hl, hb, -ht], [hl, hb, ht], [hl, -hb, ht],
        ]
    )
    faces = np.array(
        [
            [0, 1, 2], [0, 2, 3],  # -x end
            [4, 6, 5], [4, 7, 6],  # +x end
            [0, 4, 5], [0, 5, 1],  # -z side... (approx, fine for a placeholder)
            [3, 2, 6], [3, 6, 7],
            [1, 5, 6], [1, 6, 2],
            [0, 3, 7], [0, 7, 4],
        ]
    )
    return trimesh.Trimesh(vertices=vertices, faces=faces, process=True)


def build_placeholder() -> trimesh.Scene:
    scene = trimesh.Scene()

    body = trimesh.creation.box(extents=(2.5, 1.9, 1.5))
    colorize(body, PART_COLORS["body"])
    scene.add_geometry(body, node_name="body")

    screen = trimesh.creation.box(extents=(1.6, 1.1, 0.12))
    screen.apply_translation((0, 0, 0.81))
    colorize(screen, PART_COLORS["power-button-screen"])
    scene.add_geometry(screen, node_name="power-button-screen")

    knob = trimesh.creation.cylinder(radius=0.28, height=0.5, sections=32)
    knob.apply_transform(trimesh.transformations.rotation_matrix(np.pi / 2, [1, 0, 0]))
    knob.apply_translation((0.95, 1.15, 0))
    colorize(knob, PART_COLORS["volume-knob"])
    scene.add_geometry(knob, node_name="volume-knob")

    band_top = wedge(length=3.2, width_a=1.9, width_b=0.8, thickness=0.3)
    band_top.apply_translation((2.85, 0, 0.9))
    band_top.apply_transform(trimesh.transformations.rotation_matrix(np.pi / 2, [0, 1, 0]))
    band_bottom = band_top.copy()
    band_bottom.apply_translation((0, 0, -1.8))
    band = trimesh.util.concatenate([band_top, band_bottom])
    colorize(band, PART_COLORS["wrist-band"])
    scene.add_geometry(band, node_name="wrist-band")

    extents = scene.bounds
    center = extents.mean(axis=0)
    size = (extents[1] - extents[0]).max()
    scene.apply_translation(-center)
    scene.apply_scale(1.0 / size if size else 1.0)
    return scene


def main() -> None:
    scene = build_from_stl()
    source = "real .stl exports"
    if scene is None:
        scene = build_placeholder()
        source = "procedural placeholder (no .stl files found in assets/cad/fallout-smartwatch/stl/)"

    PROJECT_DIR.mkdir(parents=True, exist_ok=True)
    scene.export(OUTPUT)
    print(f"Wrote {OUTPUT} from {source}")


if __name__ == "__main__":
    sys.exit(main())

from __future__ import annotations

import tomllib
from pathlib import Path

CONFIG_DIR  = Path.home() / ".uniplay"
CONFIG_FILE = CONFIG_DIR / "config.toml"

DEFAULTS: dict = {
    "music_dir": str(Path.home() / "Music"),
    "theme":     "matrix",
    "volume":    100,
    "seek_step": 5,
}


def load() -> dict:
    if not CONFIG_FILE.exists():
        return dict(DEFAULTS)
    try:
        data = tomllib.loads(CONFIG_FILE.read_text(encoding="utf-8"))
        return {**DEFAULTS, **data}
    except Exception:
        return dict(DEFAULTS)


def save(cfg: dict) -> None:
    CONFIG_DIR.mkdir(exist_ok=True)
    lines = []
    for k, v in cfg.items():
        if isinstance(v, str):
            lines.append(f'{k} = "{v}"')
        else:
            lines.append(f"{k} = {v}")
    CONFIG_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")

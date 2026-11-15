#!/usr/bin/env python3
"""Package the canonical planning skill without maintaining a second copy."""

import hashlib
import json
from pathlib import Path
import re
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


def main():
    repo = Path(__file__).resolve().parents[1]
    plugin = repo / "plugins/product-planning"
    skill = repo / ".agents/skills/visual-product-planning"
    manifest = json.loads((plugin / "plugin.json").read_text(encoding="utf-8"))
    name, version = manifest["name"], manifest["version"]
    if name != plugin.name or not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise ValueError("Plugin directory/name must match; use an X.Y.Z release version")
    if manifest["$schema"] != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        raise ValueError("Missing portable manifest schema")
    interface = manifest["extensions"]["com.openai"]["interface"]
    if not 1 <= len(interface["shortDescription"]) <= 30:
        raise ValueError("Listing subtitle must contain 1–30 characters")

    files = {}
    for source, destination in [(plugin, Path()), (skill, Path("skills") / skill.name)]:
        for path in sorted(source.rglob("*")):
            relative = path.relative_to(source)
            if any(part in {".DS_Store", "__pycache__"} for part in relative.parts):
                continue
            if path.is_symlink():
                raise ValueError(f"Symlinks are not packaged: {relative}")
            if path.is_file():
                target = (destination / relative).as_posix()
                if target in files:
                    raise ValueError(f"Duplicate archive path: {target}")
                files[target] = path.read_bytes()

    if f"skills/{skill.name}/SKILL.md" not in files:
        raise ValueError("Planning skill is missing")
    for field in ("logo", "composerIcon"):
        if interface[field].removeprefix("./") not in files:
            raise ValueError(f"Missing asset: {field}")

    archive = repo / "dist" / f"{name}-{version}.zip"
    archive.parent.mkdir(exist_ok=True)
    with ZipFile(archive, "w", compression=ZIP_DEFLATED) as package:
        for path, content in sorted(files.items()):
            entry = ZipInfo(f"{name}/{path}", date_time=(2026, 11, 15, 0, 0, 0))
            entry.compress_type = ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            package.writestr(entry, content)
    with ZipFile(archive) as package:
        if package.testzip() is not None:
            raise ValueError("ZIP integrity check failed")
        for path, content in files.items():
            if package.read(f"{name}/{path}") != content:
                raise ValueError(f"Archive differs from source: {path}")
    print(f"{archive}\n{len(files)} files; SHA-256 {hashlib.sha256(archive.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    main()

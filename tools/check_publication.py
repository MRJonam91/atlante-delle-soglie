# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright 2026 MRJonam91 and contributors
"""Small offline editorial gate; does not establish legal clearance or balance."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md", "LICENSE", "LICENSES/GPL-3.0-or-later.txt", "LICENSING.md",
    "NOTICE", "ASSETS.md", "THIRD_PARTY_NOTICES.md", "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md", "SECURITY.md", "SUPPORT.md", "CHANGELOG.md",
    ".github/FUNDING.yml", ".github/workflows/check.yml",
    "docs/RIGHTS_AND_COMMERCIAL.md", "docs/ROADMAP.md", "docs/PLAYTEST_LOG.md",
    "print/board.svg", "print/tokens.svg",
    *(f"docs/it/{name}.md" for name in ("regole", "personaggi", "avventura", "officina", "playtest")),
    *(f"docs/en/{name}.md" for name in ("rules", "characters", "adventure", "workshop", "playtest")),
)
EXCLUDED_PARTS = {".git", ".checks", "__pycache__", ".venv", "dist"}
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
RESTRICTED_GAME_NAMES = re.compile(
    r"\b(?:Disney|Lorcana|Kingdom Hearts|Elsa|Aladdin|Agrabah|Arendelle|"
    r"Lumière|Maleficent|Mickey|Paperino|Sora|Pixar)\b", re.IGNORECASE
)
SENSITIVE = (
    ("private user path", re.compile(r"[A-Za-z]:[\\/]Users[\\/]", re.IGNORECASE)),
    ("personal email", re.compile(r"\b[\w.+-]+@(?:gmail|hotmail|outlook|yahoo)\.[a-z]+\b", re.IGNORECASE)),
    ("GitHub token", re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,})\b")),
    ("private key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
)


def main() -> int:
    errors: list[str] = []
    for name in REQUIRED:
        if not (ROOT / name).is_file():
            errors.append(f"missing required file: {name}")
    files = sorted(
        p for p in ROOT.rglob("*")
        if p.is_file() and not any(part in EXCLUDED_PARTS for part in p.relative_to(ROOT).parts)
    )
    for path in files:
        name = path.relative_to(ROOT).as_posix()
        if path.is_symlink():
            errors.append(f"symlink not allowed in publication: {name}")
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (UnicodeError, OSError):
            errors.append(f"non-UTF8 or unreadable file: {name}")
            continue
        if name != "LICENSE" and not name.startswith("LICENSES/"):
            for label, pattern in SENSITIVE:
                if pattern.search(content):
                    errors.append(f"{label}: {name}")
        game_content = name.startswith(("docs/it/", "docs/en/", "print/"))
        if game_content and RESTRICTED_GAME_NAMES.search(content):
            errors.append(f"restricted franchise reference in playable content: {name}")
        if path.suffix == ".md":
            for match in LINK.finditer(content):
                target = match.group(1).strip().strip("<>")
                parts = urlsplit(target)
                if parts.scheme or parts.netloc or not parts.path:
                    continue
                destination = (path.parent / unquote(parts.path)).resolve()
                if not destination.is_relative_to(ROOT):
                    errors.append(f"local link escapes publication: {name}")
                elif not destination.exists():
                    errors.append(f"broken local link in {name}: {target}")
        if path.suffix == ".svg":
            try:
                if "<!DOCTYPE" in content or "<!ENTITY" in content or "<?xml-stylesheet" in content.lower():
                    raise ValueError("external declaration")
                document = ET.fromstring(content)
                if document.tag != "{http://www.w3.org/2000/svg}svg":
                    raise ValueError("not SVG")
                for element in document.iter():
                    tag = element.tag.rsplit("}", 1)[-1].lower()
                    if tag in {"script", "foreignobject", "image", "style", "animate", "animatemotion", "animatetransform", "set"}:
                        raise ValueError("active or imported content")
                    for attr, value in element.attrib.items():
                        local_attr = attr.rsplit("}", 1)[-1].lower()
                        if (
                            local_attr.startswith("on")
                            or local_attr == "style"
                            or (local_attr == "href" and not value.startswith("#"))
                            or re.search(r"(?:https?:|file:|data:|javascript:|url\s*\()", value, re.IGNORECASE)
                        ):
                            raise ValueError("active or external reference")
            except (ET.ParseError, ValueError) as exc:
                errors.append(f"unsafe or invalid SVG {name}: {exc}")
    if errors:
        print("Publication check FAILED:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Publication check passed: {len(files)} UTF-8 files; required files, local links, SVGs and editorial patterns checked.")
    print("This does not establish legal clearance, human playtesting or game balance.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Validate the public skill directory structure and frontmatter."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
NAME_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


def read_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    """Return supported frontmatter fields and validation errors."""
    lines = path.read_text(encoding="utf-8").splitlines()
    errors: list[str] = []

    if not lines or lines[0] != "---":
        return {}, ["frontmatter must start on the first line"]

    try:
        closing_line = lines.index("---", 1)
    except ValueError:
        return {}, ["frontmatter is missing its closing delimiter"]

    fields: dict[str, str] = {}
    for line in lines[1:closing_line]:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        if key not in {"name", "description"}:
            continue
        if key in fields:
            errors.append(f"frontmatter contains duplicate {key!r}")
        fields[key] = value.strip().strip("'\"")

    if not any(line.strip() for line in lines[closing_line + 1 :]):
        errors.append("skill body must not be empty")

    return fields, errors


def validate_skill(skill_dir: Path) -> list[str]:
    """Validate one immediate child of the skills directory."""
    relative_dir = skill_dir.relative_to(ROOT)
    skill_file = skill_dir / "SKILL.md"
    errors: list[str] = []

    if not NAME_PATTERN.fullmatch(skill_dir.name):
        errors.append(f"{relative_dir}: directory name must use lowercase kebab-case")

    if not skill_file.is_file():
        errors.append(f"{relative_dir}: missing SKILL.md")
        return errors

    fields, frontmatter_errors = read_frontmatter(skill_file)
    errors.extend(f"{skill_file.relative_to(ROOT)}: {error}" for error in frontmatter_errors)

    if not fields.get("name"):
        errors.append(f"{skill_file.relative_to(ROOT)}: missing non-empty 'name'")
    elif fields["name"] != skill_dir.name:
        errors.append(
            f"{skill_file.relative_to(ROOT)}: name {fields['name']!r} must match "
            f"directory {skill_dir.name!r}"
        )

    if not fields.get("description"):
        errors.append(f"{skill_file.relative_to(ROOT)}: missing non-empty 'description'")

    return errors


def main() -> int:
    """Validate all public skills."""
    if not SKILLS_DIR.is_dir():
        print("skills/: directory not found", file=sys.stderr)
        return 1

    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    if not skill_dirs:
        print("skills/: no skill directories found", file=sys.stderr)
        return 1

    errors = [error for skill_dir in skill_dirs for error in validate_skill(skill_dir)]
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(skill_dirs)} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

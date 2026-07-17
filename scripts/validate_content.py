#!/usr/bin/env python3
"""Validate tutorial metadata, internal links, draft rules, and obvious secrets."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FIELDS = {
    "title",
    "description",
    "category",
    "difficulty",
    "created_at",
    "updated_at",
    "verification",
    "status",
    "sources",
}
ALLOWED_VERIFICATION = {"tested", "source-verified", "automated-draft"}
ALLOWED_STATUS = {"published", "needs-review", "draft", "outdated"}
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
SECRET_PATTERNS = {
    "OpenAI-style API key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "GitHub token": re.compile(r"\bgh[psoru]_[A-Za-z0-9]{20,}\b"),
    "Private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "Generic secret assignment": re.compile(
        r"(?i)\b(api[_-]?key|access[_-]?token|client[_-]?secret|password)\s*[:=]\s*['\"][^'\"]{8,}['\"]"
    ),
}
FORBIDDEN_NAMES = {".env", ".env.local", ".env.production"}


def parse_front_matter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    block = text[4:end]
    result: dict[str, str] = {}
    for raw_line in block.splitlines():
        if not raw_line or raw_line.startswith(" ") or ":" not in raw_line:
            continue
        key, value = raw_line.split(":", 1)
        result[key.strip()] = value.strip().strip('"\'')
    return result


def validate_tutorial(path: Path, text: str, errors: list[str]) -> None:
    if path.name == "README.md":
        return
    metadata = parse_front_matter(text)
    missing = sorted(REQUIRED_FIELDS - metadata.keys())
    if missing:
        errors.append(f"{path.relative_to(ROOT)}: missing front matter fields: {', '.join(missing)}")
        return

    verification = metadata.get("verification")
    status = metadata.get("status")
    if verification not in ALLOWED_VERIFICATION:
        errors.append(f"{path.relative_to(ROOT)}: invalid verification '{verification}'")
    if status not in ALLOWED_STATUS:
        errors.append(f"{path.relative_to(ROOT)}: invalid status '{status}'")

    relative = path.relative_to(ROOT)
    if relative.parts[0] == "docs":
        if verification == "automated-draft":
            errors.append(f"{relative}: automated drafts cannot be published under docs/")
        if status == "draft":
            errors.append(f"{relative}: draft status cannot be published under docs/")
    if relative.parts[0] == "drafts" and path.name != "README.md" and status != "draft":
        errors.append(f"{relative}: files under drafts/ must use status: draft")

    if verification == "source-verified" and "尚未完成本项目" not in text:
        errors.append(f"{relative}: source-verified tutorial must explicitly state it was not fully tested")
    if verification == "tested" and metadata.get("verified_at", "").lower() in {"", "null"}:
        errors.append(f"{relative}: tested tutorial must include verified_at")
    if "http://" not in text and "https://" not in text:
        errors.append(f"{relative}: tutorial must contain at least one source URL")


def validate_links(path: Path, text: str, errors: list[str]) -> None:
    for target in LINK_RE.findall(text):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        clean_target = target.split("#", 1)[0].split("?", 1)[0]
        if not clean_target:
            continue
        resolved = (path.parent / clean_target).resolve()
        try:
            resolved.relative_to(ROOT)
        except ValueError:
            errors.append(f"{path.relative_to(ROOT)}: link escapes repository: {target}")
            continue
        if not resolved.exists():
            errors.append(f"{path.relative_to(ROOT)}: broken internal link: {target}")


def main() -> int:
    errors: list[str] = []

    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        relative = path.relative_to(ROOT)
        if path.name in FORBIDDEN_NAMES or path.suffix in {".pem", ".key", ".p12", ".pfx"}:
            errors.append(f"{relative}: forbidden sensitive file")
            continue

        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"{relative}: possible secret detected ({label})")

        if path.suffix.lower() == ".md":
            validate_links(path, text, errors)
            if relative.parts and relative.parts[0] in {"docs", "drafts"}:
                validate_tutorial(path, text, errors)

    if errors:
        print("Content validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Content validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

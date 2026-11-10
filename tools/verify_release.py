"""Verify the local v0.1-review publication candidate."""

from __future__ import annotations

import json
from pathlib import Path

from generate_release_manifest import OUTPUT, ROOT, included, sha256


REQUIRED = {
    ".github/ISSUE_TEMPLATE/mathematical-review.yml",
    "AI_ASSISTANCE.md",
    "CITATION.cff",
    "FORMALISATION_THEOREME_VOLUME_3D.md",
    "LICENSE",
    "README.md",
    "README.fr.md",
    "REPRODUCIBILITY.md",
    "REVIEWING.md",
    "STATUS.json",
    "metadata/ZENODO_METADATA_DRAFT.md",
    "output/pdf/DYN-Preprint-Volume-Deficit-3D-v0.1-review.pdf",
    "review/INTERNAL_AI_AUDIT.md",
    "review/REQUEST_FOR_HUMAN_REVIEW.md",
}
FORBIDDEN_PUBLIC_SUFFIXES = {".odt", ".doc", ".docx"}


def fail(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def parse_manifest() -> dict[str, str]:
    if not OUTPUT.is_file():
        fail("SHA256SUMS.txt is missing")
    parsed: dict[str, str] = {}
    for line_number, raw_line in enumerate(
        OUTPUT.read_text(encoding="utf-8").splitlines(), start=1
    ):
        digest, separator, relative = raw_line.partition("  ")
        if not separator or len(digest) != 64:
            fail(f"malformed SHA256SUMS line {line_number}")
        if relative in parsed:
            fail(f"duplicate manifest path: {relative}")
        parsed[relative] = digest
    return parsed


def main() -> None:
    manifest = parse_manifest()
    actual_files = {
        path.relative_to(ROOT).as_posix(): path
        for path in ROOT.rglob("*")
        if included(path)
    }
    if set(manifest) != set(actual_files):
        missing = sorted(set(actual_files) - set(manifest))
        stale = sorted(set(manifest) - set(actual_files))
        fail(f"manifest membership mismatch; missing={missing}, stale={stale}")

    for relative, path in actual_files.items():
        if sha256(path) != manifest[relative]:
            fail(f"hash mismatch: {relative}")

    absent = sorted(REQUIRED - set(actual_files))
    if absent:
        fail(f"required release files are absent: {absent}")

    forbidden = sorted(
        relative
        for relative in actual_files
        if Path(relative).suffix.lower() in FORBIDDEN_PUBLIC_SUFFIXES
        or Path(relative).name.startswith(".~lock")
    )
    if forbidden:
        fail(f"office or lock files must not be public: {forbidden}")

    status = json.loads((ROOT / "STATUS.json").read_text(encoding="utf-8"))
    if status.get("version") != "0.1-review":
        fail("STATUS.json has the wrong version")
    if status.get("human_review", {}).get("status") != "not_run":
        fail("human-review status must remain not_run before external review")
    if status.get("human_review", {}).get("independent_review_received") is not False:
        fail("independent review must remain false before external review")
    creator = status.get("creator", {})
    if creator != {
        "name": "ROYER Patrick",
        "project": "Projet Dynagénèse",
        "orcid": "0009-0009-4149-2834",
    }:
        fail("STATUS.json creator identity does not match the confirmed metadata")

    pdf = ROOT / "output/pdf/DYN-Preprint-Volume-Deficit-3D-v0.1-review.pdf"
    if pdf.stat().st_size < 10_000 or pdf.read_bytes()[:5] != b"%PDF-":
        fail("canonical PDF is missing or malformed")

    textual = "\n".join(
        path.read_text(encoding="utf-8", errors="replace")
        for relative, path in actual_files.items()
        if Path(relative).suffix.lower() in {".md", ".cff", ".json", ".yml", ".yaml"}
    )
    for marker in ("REPLACE_ME", "TODO_PUBLICATION", "<ORCID>"):
        if marker in textual:
            fail(f"unresolved publication marker: {marker}")
    for required_text in (
        "ROYER Patrick",
        "0009-0009-4149-2834",
        "ChatGPT",
        "Codex",
        "Claude AI",
        "DeepSeek",
        "Z.ai",
        "Kimi",
    ):
        if required_text not in (ROOT / "AI_ASSISTANCE.md").read_text(encoding="utf-8"):
            fail(f"AI_ASSISTANCE.md is missing: {required_text}")

    print(f"OK: {len(actual_files)} files match SHA256SUMS.txt")
    print("OK: required publication files and scientific-status guards are present")
    print("OK: confirmed creator, ORCID and AI-transparency metadata are present")
    print(f"OK: canonical PDF ({pdf.stat().st_size} bytes)")


if __name__ == "__main__":
    main()

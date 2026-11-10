"""Create and verify the SHA-256 manifest for the complete Zenodo upload set."""

from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS_DIR = ROOT.parents[1]
DIST = ROOT.parent / "dist"
OUTPUT = DIST / "SHA256SUMS-ZENODO.txt"
EXPECTED_SUPPLEMENT = ROOT / "metadata" / "ZENODO_NUMERICAL_SUPPLEMENT_SHA256.txt"

CORE_FILES = (
    ROOT / "output/pdf/DYN-Preprint-Volume-Deficit-3D-v0.1-review.pdf",
    DIST / "dyn-validex-lattice-ball-volume-deficit-3d-v0.1-review-source.zip",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def expected_supplement() -> dict[str, str]:
    expected: dict[str, str] = {}
    for raw_line in EXPECTED_SUPPLEMENT.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        digest, separator, name = line.partition("  ")
        if not separator or len(digest) != 64:
            raise SystemExit(f"Malformed supplement manifest line: {raw_line}")
        expected[name] = digest
    return expected


def main() -> None:
    files = list(CORE_FILES)
    for name, expected in expected_supplement().items():
        path = ANALYSIS_DIR / name
        if not path.is_file():
            raise SystemExit(f"Missing numerical archive: {path}")
        actual = sha256(path)
        if actual != expected:
            raise SystemExit(f"Numerical archive hash mismatch: {name}")
        files.append(path)

    missing = [path for path in CORE_FILES if not path.is_file()]
    if missing:
        raise SystemExit(f"Missing core upload files: {missing}")

    DIST.mkdir(parents=True, exist_ok=True)
    lines = [f"{sha256(path)}  {path.name}" for path in files]
    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"Wrote {OUTPUT} with {len(lines)} upload entries")
    print(f"Total payload bytes: {sum(path.stat().st_size for path in files)}")


if __name__ == "__main__":
    main()

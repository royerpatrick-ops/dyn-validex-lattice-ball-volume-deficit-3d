"""Build a deterministic source archive from the frozen release manifest."""

from __future__ import annotations

import hashlib
from pathlib import Path, PurePosixPath
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "SHA256SUMS.txt"
DIST = ROOT.parent / "dist"
ARCHIVE = DIST / "dyn-validex-lattice-ball-volume-deficit-3d-v0.1-review-source.zip"
ARCHIVE_HASH = DIST / "SOURCE_ARCHIVE_SHA256.txt"
ARCHIVE_PREFIX = "dyn-validex-lattice-ball-volume-deficit-3d-v0.1-review"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def manifest_entries() -> list[tuple[str, Path]]:
    if not MANIFEST.is_file():
        raise SystemExit("SHA256SUMS.txt is missing; generate it before archiving")

    entries: list[tuple[str, Path]] = []
    for line_number, raw_line in enumerate(
        MANIFEST.read_text(encoding="utf-8").splitlines(), start=1
    ):
        expected, separator, relative_text = raw_line.partition("  ")
        if not separator or len(expected) != 64:
            raise SystemExit(f"Malformed manifest line {line_number}")
        relative = PurePosixPath(relative_text)
        if relative.is_absolute() or ".." in relative.parts:
            raise SystemExit(f"Unsafe manifest path on line {line_number}")
        path = ROOT.joinpath(*relative.parts)
        if not path.is_file():
            raise SystemExit(f"Manifest file is missing: {relative_text}")
        actual = sha256(path)
        if actual != expected:
            raise SystemExit(f"Hash mismatch before archiving: {relative_text}")
        entries.append((relative.as_posix(), path))
    return entries


def add_file(archive: ZipFile, arcname: str, path: Path) -> None:
    info = ZipInfo(arcname, date_time=(1980, 1, 1, 0, 0, 0))
    info.compress_type = ZIP_DEFLATED
    info.create_system = 3
    info.external_attr = 0o100644 << 16
    archive.writestr(info, path.read_bytes(), compress_type=ZIP_DEFLATED, compresslevel=9)


def main() -> None:
    entries = manifest_entries()
    DIST.mkdir(parents=True, exist_ok=True)
    with ZipFile(ARCHIVE, mode="w") as archive:
        for relative, path in entries:
            add_file(archive, f"{ARCHIVE_PREFIX}/{relative}", path)
        add_file(
            archive,
            f"{ARCHIVE_PREFIX}/SHA256SUMS.txt",
            MANIFEST,
        )

    digest = sha256(ARCHIVE)
    ARCHIVE_HASH.write_text(
        f"{digest}  {ARCHIVE.name}\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"Wrote {ARCHIVE}")
    print(f"SHA-256: {digest}")


if __name__ == "__main__":
    main()

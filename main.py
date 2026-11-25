# SPDX-License-Identifier: MIT
"""news-image-20261125 entry: copy the bundled front-page image to /output.

The image (entry.png, JPEG bytes) sums up the world news of Wednesday
25 November 2026: Ukraine's sea-drone strikes on Russian ships, the Houthi
drone strike on Riyadh's tallest tower, Huawei's conviction in Brooklyn,
and the Nvidia/Anthropic market reversal. The program is deterministic and
offline: it copies the bundled asset byte-for-byte.
"""
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> int:
    # Copy, never re-encode: both runs must write byte-identical output.
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.png", out_dir / "entry.png")
    return 0


if __name__ == "__main__":
    sys.exit(main())

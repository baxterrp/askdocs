from pathlib import Path
from typing import Iterator


def load_files(path: str) -> Iterator[str]:
    for file in Path(path).iterdir():
        if file.is_file():
            for line in file.open():
                line = line.strip()
                if line:
                    yield line

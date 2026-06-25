from pathlib import Path
from typing import Iterator


def read_all_files(path: str) -> Iterator[str]:
    for file in Path(path).iterdir():
        if file.is_file():
            yield f"--- start {file.name} ---"
            for line in file.open():
                line = line.strip()
                if line:
                    yield line
            yield f"-- end {file.name} --\n"


def chunk_lines(lines: Iterator[str], chunk_size: int) -> Iterator[str]:
    words = []
    for line in lines:
        words.extend(line.split())
        if len(words) >= chunk_size:
            yield " ".join(words[:chunk_size])
            words = words[chunk_size:]
    if words:
        yield " ".join(words)

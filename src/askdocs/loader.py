from pathlib import Path
from typing import Iterator


def read_all_files(path: str) -> Iterator[str]:
    for file in Path(path).iterdir():
        if file.is_file():
            for line in file.open():
                line = line.strip()
                if line:
                    yield line


def chunk_lines(lines: Iterator[str], chunk_size: int) -> Iterator[str]:
    words = []
    for line in lines:
        words.extend(line.split())
        if len(words) >= chunk_size:
            yield " ".join(words[:chunk_size])
            words = words[chunk_size:]
    if words:
        yield " ".join(words)


def retrieve(prompt: str, path: str) -> Iterator[str]:
    prompt_words = set(prompt.lower().split())
    file_data = read_all_files(path)
    chunks = chunk_lines(file_data, 10)
    scored_chunks = []

    for chunk in chunks:
        chunk_words = set(chunk.lower().split())
        score = len(prompt_words & chunk_words)
        scored_chunks.append((chunk, score))

    for chunk in sorted(scored_chunks, key=lambda x: x[1], reverse=True)[:3]:
        yield chunk[0]


def build_prompt(prompt: str, chunks: list[str]) -> str:
    header = "Answer the following question using only the provided context:\n\n"
    body = f"prompt: {prompt}\n\n" + f"Context: {' '.join(chunks)}"

    return header + body

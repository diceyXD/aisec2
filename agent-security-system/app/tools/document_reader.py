from pathlib import Path


DATA_DIR = Path(__file__).resolve().parents[1] / "data"


def search_documents(query: str) -> str:
    query_terms = {term.strip(".,?!").lower() for term in query.split() if len(term) > 2}
    matches: list[str] = []

    for path in sorted(DATA_DIR.glob("*.txt")):
        content = path.read_text(encoding="utf-8")
        lowered = content.lower()
        score = sum(1 for term in query_terms if term in lowered)
        if score > 0:
            matches.append(f"{path.name}: {content.strip()}")

    if not matches:
        return "No relevant document content found."

    return "\n\n".join(matches[:2])

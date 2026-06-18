from pathlib import Path


OUTPUT_DIR = Path(__file__).resolve().parents[2] / "outputs"


def write_mock_file(filename: str, content: str) -> str:
    safe_name = Path(filename).name
    OUTPUT_DIR.mkdir(exist_ok=True)
    output_path = OUTPUT_DIR / safe_name
    output_path.write_text(content, encoding="utf-8")
    return f"Mock file written to {output_path}."

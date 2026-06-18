from pathlib import Path


OUTPUT_DIR = Path(__file__).resolve().parents[2] / "outputs"


def send_mock_email(recipient: str, subject: str, body: str) -> str:
    OUTPUT_DIR.mkdir(exist_ok=True)
    log_path = OUTPUT_DIR / "mock_email_log.txt"
    entry = (
        f"To: {recipient}\n"
        f"Subject: {subject}\n"
        f"Body: {body}\n"
        "---\n"
    )
    with log_path.open("a", encoding="utf-8") as file:
        file.write(entry)

    return f"Mock email recorded for {recipient}."

import json
from pathlib import Path


class FileHandler:
    def __init__(self, file_dir: str = "transcripts",
                 history_file: str = "data/history.json"):
        self.transcript_dir = Path(file_dir)
        self.history_file = Path(history_file)
        self.transcript_dir.mkdir(exist_ok=True)
        self.history_file.parent.mkdir(exist_ok=True)

    def save_file(self, content: str, filename: str) -> Path:
        filepath = self.transcript_dir / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"File saved to {filepath}")
        return filepath

    def load_file(self, filename: str) -> str:
        filepath = self.transcript_dir / filename
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()

    def save_history(self, entry: dict) -> None:
        history = []
        if self.history_file.exists():
            with open(self.history_file, 'r', encoding='utf-8') as f:
                history = json.load(f)
        history.append(entry)
        with open(self.history_file, 'w', encoding='utf-8') as f:
            json.dump(history, f, indent=2)
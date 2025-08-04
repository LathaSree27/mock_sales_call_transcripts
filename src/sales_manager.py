import subprocess
from datetime import datetime
from typing import Optional

from src.ollama_executor import OllamaExecutor
from src.file_handler import FileHandler
from src.transcript_generator import TranscriptGenerator



class SalesManager:
    """Handles the core sales call transcript operations"""

    def __init__(self):
        self.runner = OllamaExecutor()
        self.generator = TranscriptGenerator(self.runner)
        self.file_handler = FileHandler()
        self._verify_ollama()

    def _verify_ollama(self):
        """Verify Ollama is installed and available"""
        try:
            subprocess.run(["ollama", "--version"],
                           check=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("Error: Ollama is not installed or not in PATH.")
            print("Please install Ollama from https://ollama.com/")
            exit(1)

    def generate_transcript(self, duration: int, output_file: Optional[str],
                            language: str):
        """Generate and save a new sales call transcript"""
        transcript = self.generator.generate(duration, language)
        print("\nGenerated Transcript:")
        print(transcript)

        filename = output_file or f"transcript_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        self.file_handler.save_file(transcript, filename)

        self.file_handler.save_history({
            'type': 'generate',
            'timestamp': datetime.now().isoformat(),
            'filename': filename,
            'duration': duration,
            'language': language
        })

    def summarize_transcript(self, filename: str, model: str):
        """Generate and display a summary of a transcript"""
        transcript = self.file_handler.load_file(filename)
        summary = self.generator.summarize(transcript, model)
        print("\nTranscript Summary:")
        print(summary)

        self.file_handler.save_history({
            'type': 'summarize',
            'timestamp': datetime.now().isoformat(),
            'filename': filename,
            'model': model,
            'summary': summary
        })

    def answer_question(self, filename: str, question: str, model: str):
        """Answer a question about a transcript"""
        transcript = self.file_handler.load_file(filename)
        answer = self.generator.question(transcript, question, model)
        print(f"\nQuestion: {question}")
        print("Answer:")
        print(answer)

        self.file_handler.save_history({
            'type': 'question',
            'timestamp': datetime.now().isoformat(),
            'filename': filename,
            'question': question,
            'model': model,
            'answer': answer
        })
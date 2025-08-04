"""
Mock Sales Call Application
This module provides a simple command-line interface for simulating sales calls.
"""

from src.command_handler import CommandHandler
from src.sales_manager import SalesManager


if __name__ == "__main__":
    if __name__ == "__main__":
        manager = SalesManager()
        handler = CommandHandler(manager)
        handler.execute_command()
    # executor = OllamaExecutor(default_model='zephyr')
    # transcript_generator = TranscriptGenerator(executor)
    # print(transcript_generator.generate(duration=5,language="es"), flush=True)
    # print(transcript_generator.summarize(transcript_generator.generate(), model="mistral"), flush=True)
    # print(transcript_generator.question(transcript_generator.generate(),model="mistral", question = "What is the concern of the customer?"), flush=True)
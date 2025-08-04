"""
Mock Sales Call Application

This module provides a simple command-line interface for simulating sales calls.
"""
import subprocess
from typing import Optional


class OllamaExecutor:
    def __init__(self, default_model: str = 'mistral'):
        self.default_model = default_model

    def run(self, prompt: str, model: Optional[str] = None) -> str:
        model_to_use = model or self.default_model
        try:
            cmd = f'ollama run {model_to_use} "{prompt}"'
            result = subprocess.run(cmd,
                                    shell=True,
                                    check=True,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    text=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"Error running model: {e.stderr}")
            raise

class TranscriptGenerator:
    def __init__(self, executor: OllamaExecutor):
        self.executor = executor

    def generate(self, duration: int = 5, language: str = "en") -> str:
        prompt = f"""You are a system that generates sales call transcripts.
        Generate a realistic {duration}-minute sales call transcript between a sales rep and a potential customer.
        Format:
        - Each line should start with a timestamp (HH:MM:SS)
        - Followed by a space, then speaker name with company in parentheses
        - Then a colon and the dialogue
        Example:
        00:00:00 Sam (openai.com): Hey there Staya.
        00:00:02 Satya (microsoft.com): Hi Sam, how are you?
        Ensure the entire transcript strictly follows this format, without deviations.
        Language: {language}
        """
        result = self.executor.run(prompt)
        return result

    def summarize(self, transcript: str, model: str = "zephyr") -> str:
        prompt = f"""Summarize the following sales call transcript:
        {transcript}
        """
        result = self.executor.run(prompt, model=model)
        return result

    def question(self, transcript: str, question: str, model: str = "zephyr") -> str:
        prompt = f"""Based on this sales call 
        transcript:{transcript}\n
        Question: {question}\n
        Answer concisely:"""
        result = self.executor.run(prompt, model=model)
        return result

    def _clean(self, text: str) -> str:
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        return '\n'.join(lines)


if __name__ == "__main__":
    executor = OllamaExecutor(default_model='zephyr')
    transcript_generator = TranscriptGenerator(executor)
    print(transcript_generator.generate(duration=5,language="es"), flush=True)
    print(transcript_generator.summarize(transcript_generator.generate(), model="mistral"), flush=True)
    print(transcript_generator.question(transcript_generator.generate(),model="mistral", question = "What is the concern of the customer?"), flush=True)
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

if __name__ == "__main__":
    executor = OllamaExecutor()
    print(executor.run("Tell me a joke"), flush=True)

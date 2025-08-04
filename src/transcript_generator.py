from src.ollama_executor import OllamaExecutor


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


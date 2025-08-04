import unittest
from unittest.mock import MagicMock

from src.ollama_executor import OllamaExecutor
from src.transcript_generator import TranscriptGenerator


class TestTranscriptGenerator(unittest.TestCase):

    def setUp(self):
        # Create a mock OllamaExecutor instance
        self.mock_executor = MagicMock(spec=OllamaExecutor)
        self.generator = TranscriptGenerator(executor=self.mock_executor)

    def test_generate_transcript(self):
        # Arrange
        fake_transcript = "00:00:00 Sam (openai.com): Hello there."
        self.mock_executor.run.return_value = fake_transcript

        # Act
        result = self.generator.generate(duration=5, language="en")

        # Assert
        self.mock_executor.run.assert_called_once()
        self.assertIn("00:00:00", result)
        self.assertIn("Sam", result)

    def test_summarize_transcript(self):
        # Arrange
        fake_summary = "- Key point 1\n- Key point 2"
        self.mock_executor.run.return_value = fake_summary
        input_transcript = "00:00:00 Sam (openai.com): Hello."

        # Act
        result = self.generator.summarize(input_transcript, model="zephyr")

        # Assert
        self.mock_executor.run.assert_called_once()
        self.assertIn("Key point", result)

    def test_question_answering(self):
        # Arrange
        transcript = "00:00:00 Sam (openai.com): Hello."
        question = "What did Sam say?"
        fake_answer = "Sam greeted the customer."
        self.mock_executor.run.return_value = fake_answer

        # Act
        result = self.generator.question(transcript, question, model="zephyr")

        # Assert
        self.mock_executor.run.assert_called_once()
        self.assertIn("greeted", result)

    def test_clean_text(self):
        # Arrange
        messy_text = "\n\n  Hello\n\n  World  \n"
        expected = "Hello\nWorld"

        # Act
        result = self.generator._clean(messy_text)

        # Assert
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch, MagicMock
from src.sales_manager import SalesManager


class TestSalesManager(unittest.TestCase):

    @patch("src.sales_manager.subprocess.run")
    @patch("src.sales_manager.FileHandler")
    @patch("src.sales_manager.TranscriptGenerator")
    @patch("src.sales_manager.OllamaExecutor")
    def setUp(self, mock_executor, mock_generator_cls, mock_file_handler_cls, mock_subprocess):
        mock_subprocess.return_value = MagicMock()  # Simulate successful `ollama --version`
        self.mock_generator = MagicMock()
        self.mock_file_handler = MagicMock()

        mock_generator_cls.return_value = self.mock_generator
        mock_file_handler_cls.return_value = self.mock_file_handler

        self.sales_manager = SalesManager()

    def test_generate_transcript(self):
        self.mock_generator.generate.return_value = "mock transcript"

        self.sales_manager.generate_transcript(duration=5, output_file="test.txt", language="en")

        self.mock_generator.generate.assert_called_once_with(5, "en")
        self.mock_file_handler.save_file.assert_called_once_with("mock transcript", "test.txt")
        self.mock_file_handler.save_history.assert_called_once()

    def test_summarize_transcript(self):
        self.mock_file_handler.load_file.return_value = "mock transcript"
        self.mock_generator.summarize.return_value = "mock summary"

        self.sales_manager.summarize_transcript(filename="test.txt", model="zephyr")

        self.mock_file_handler.load_file.assert_called_once_with("test.txt")
        self.mock_generator.summarize.assert_called_once_with("mock transcript", "zephyr")
        self.mock_file_handler.save_history.assert_called_once()

    def test_answer_question(self):
        self.mock_file_handler.load_file.return_value = "mock transcript"
        self.mock_generator.question.return_value = "mock answer"

        self.sales_manager.answer_question(filename="test.txt", question="What is the goal?", model="zephyr")

        self.mock_file_handler.load_file.assert_called_once_with("test.txt")
        self.mock_generator.question.assert_called_once_with("mock transcript", "What is the goal?", "zephyr")
        self.mock_file_handler.save_history.assert_called_once()


if __name__ == '__main__':
    unittest.main()

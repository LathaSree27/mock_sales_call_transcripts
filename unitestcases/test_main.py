import subprocess
import unittest
from unittest.mock import patch, MagicMock
from src.main import OllamaExecutor 

class TestOllamaExecutor(unittest.TestCase):

    @patch('subprocess.run')
    def test_run_with_default_model(self, mock_run):
        mock_result = MagicMock()
        mock_result.stdout = 'Mocked response\n'
        mock_run.return_value = mock_result

        runner = OllamaExecutor()
        output = runner.run("Hello")

        mock_run.assert_called_once_with(
            'ollama run mistral "Hello"',
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        self.assertEqual(output, 'Mocked response')

    @patch('subprocess.run')
    def test_run_with_custom_model(self, mock_run):
        mock_result = MagicMock()
        mock_result.stdout = 'Response from llama3\n'
        mock_run.return_value = mock_result

        runner = OllamaExecutor()
        output = runner.run("How are you?", model="llama3")

        mock_run.assert_called_once_with(
            'ollama run llama3 "How are you?"',
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        self.assertEqual(output, 'Response from llama3')

if __name__ == '__main__':
    unittest.main()

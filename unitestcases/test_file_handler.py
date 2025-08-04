import unittest
import tempfile
import shutil
import os
import json
from src.file_handler import FileHandler


class TestFileHandler(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()
        self.transcript_dir = os.path.join(self.test_dir, "transcripts")
        self.history_file = os.path.join(self.test_dir, "data", "history.json")
        self.handler = FileHandler(file_dir=self.transcript_dir, history_file=self.history_file)

    def tearDown(self):
        # Remove the temporary directory after test
        shutil.rmtree(self.test_dir)

    def test_save_file_creates_file_with_content(self):
        filename = "test_transcript.txt"
        content = "00:00:00 Test (test.com): Hello"
        filepath = self.handler.save_file(content, filename)

        self.assertTrue(os.path.exists(filepath))
        with open(filepath, 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), content)

    def test_load_file_reads_correct_content(self):
        filename = "test_transcript.txt"
        content = "00:00:00 Test (test.com): Hello"

        # Save first to load it
        self.handler.save_file(content, filename)
        loaded = self.handler.load_file(filename)

        self.assertEqual(loaded, content)

    def test_save_history_creates_and_appends_entries(self):
        entry1 = {
        "type": "generate",
        "timestamp": "2025-08-04T08:10:43.020108",
        "filename": "meeting.txt",
        "duration": 5,
        "language": "en"
        }
        entry2 = {
        "type": "summarize",
        "timestamp": "2025-08-04T08:14:15.029057",
        "filename": "meeting.txt",
        "summary": "1. Acme Solutions offers custom software solutions to streamline business operations and improve efficiency.\n2. Their services include automating repetitive tasks, improving efficiency, and driving growth through custom software solutions.\n3. One specific example is inventory management with easy tracking of stock levels, automated reordering processes, and seamless data flow integration with existing systems.\n4. Implementation time varies depending on business needs but typically takes a few weeks to a couple of months.\n5. The cost of the solution depends on specific requirements, but Acme Solutions offers competitive pricing and excellent value for money. \n6. A meeting with their team can be arranged to discuss this opportunity further at the potential customer's convenience."
      }

        self.handler.save_history(entry1)
        self.handler.save_history(entry2)

        with open(self.history_file, 'r', encoding='utf-8') as f:
            history = json.load(f)

        self.assertEqual(len(history), 2)
        self.assertEqual(history[0]["type"], "generate")
        self.assertEqual(history[1]["type"], "summarize")


if __name__ == '__main__':
    unittest.main()

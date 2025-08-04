import argparse

from src.sales_manager import SalesManager


class CommandHandler:
    """Handles command line interface parsing and execution"""

    def __init__(self, sales_manager: SalesManager):
        self.sales_manager = sales_manager
        self.parser = self._create_parser()

    def _create_parser(self) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(description="Sales Call Transcript Generator and Analyzer")
        subparsers = parser.add_subparsers(dest='command', required=True)

        # Generate command
        generate_parser = subparsers.add_parser('generate', help='Generate a sales call transcript')
        generate_parser.add_argument('-d', '--duration', type=int, default=5)
        generate_parser.add_argument('-o', '--output')
        generate_parser.add_argument('-l', '--language', default='en')
        generate_parser.add_argument('-m', '--model', default='mistral')

        # Summarize command
        summarize_parser = subparsers.add_parser('summarize', help='Summarize a transcript')
        summarize_parser.add_argument('filename')
        summarize_parser.add_argument('-m', '--model', default='zephyr')

        # Question command
        question_parser = subparsers.add_parser('question', help='Ask a question about a transcript')
        question_parser.add_argument('filename')
        question_parser.add_argument('question')
        question_parser.add_argument('-m', '--model', default='zephyr')

        return parser

    def execute_command(self):
        """Parse arguments and execute the appropriate command"""
        args = self.parser.parse_args()

        if args.command == 'generate':
            self.sales_manager.generate_transcript(
                duration=args.duration,
                output_file=args.output,
                language=args.language,
            )
        elif args.command == 'summarize':
            self.sales_manager.summarize_transcript(
                filename=args.filename,
                model=args.model
            )
        elif args.command == 'question':
            self.sales_manager.answer_question(
                filename=args.filename,
                question=args.question,
                model=args.model
            )
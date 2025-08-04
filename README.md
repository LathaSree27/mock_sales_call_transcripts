# Mock Sales Call Application

A Python-based application for simulating and practicing sales calls with AI-powered responses.

## Features
- Simulate realistic sales call scenarios
- AI-powered responses for dynamic conversations
- Track and analyze call performance
- Customizable sales scripts and scenarios

## Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd MockSalesCall
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   install conda
   conda create --name myenv python=3.10
   conda activate minienv   
   ```

3. Install dependencies (for openai):
   ```bash
   pip install -r requirements.txt
   ```
4. Export Path Variables (for openai):
   ```bash
   export OPENAI_API_KEY='your-api-key-here'  # not needed for Ollama
   ```
5. install Tools for Running LLMs:
   ```bash
   brew install ollama #mocOS
   ollama pull mistral       
   ollama pull zephyr       
   ```

## Usage
```bash
python main.py
```

## Project Structure
```
MockSalesCall/
├── .gitignore
├── README.md
├── requirements.txt
└── src/
    └── __init__.py
    └── main.py
```

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any questions or feedback, please open an issue in the repository.

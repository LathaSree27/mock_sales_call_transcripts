from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mocksalescall",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A mock sales call simulation tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LathaSree27/mock_sales_call_transcripts",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        line.strip() for line in open("requirements.txt").readlines() 
        if line.strip() and not line.startswith("#")
    ],
    entry_points={
        "console_scripts": [
            "mocksalescall=main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

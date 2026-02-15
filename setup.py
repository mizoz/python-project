from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1.0",
    description="A Python project with requirements.txt and setup.py",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

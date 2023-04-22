from setuptools import setup, find_packages

setup(
    name="summary",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "summary = summary.main:main",
        ],
    },
)

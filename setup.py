from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    description="A simple math quiz game",
    author="Yunyi LI",
    author_email="yunyi.li@fau.de",
    license="MIT License",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "math_quiz=math_quiz.math_quiz:math_quiz",
        ],
    },
)
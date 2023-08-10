from setuptools import find_packages, setup


with open('README.md') as file:
    long_desc = file.read()

__version__ = "V0.0.7-3"

packages = find_packages()
repository_url = "https://github.com/Metim0l/free-gpt-engineer"

setup(
    name="free-gpt-engineer",
    author="Metim0l",
    packages=packages,
    version=__version__,
    description="Absolutely FREE AI for code generation. Specify what you want "
                "it to build, the AI asks for clarification, and then builds it.",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    project_urls={
        'Source': 'https://github.com/Metim0l/free-gpt-engineer',
    },
    install_requires=[
        "requests",
        "openai",
        "termcolor==2.3.0",
        "rudder-sdk-python==2.0.2",
        "dataclasses-json==0.5.7",
        "PyQt5==5.15.9",
        "typer==0.9.0"
    ],
    download_url=f"{repository_url}/archive/{__version__}.tar.gz",
    keywords=[
        "AI",
        "ChatGPT",
        "Code Generation"
    ],
    license='MIT',
    classifiers=[
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ],
    python_requires='>=3.6',
)

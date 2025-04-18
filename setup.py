from setuptools import setup, find_packages

setup(
    name="python_logger",
    version="0.1.0",
    author="Vaddi Jaswant",
    author_email="vaddijaswant@example.com",
    description="A simple logger package for Python projects.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/VADDIJASWANT/python_logger"
)
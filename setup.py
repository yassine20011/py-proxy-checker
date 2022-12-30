import setuptools

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="py-proxy-checker",
    version="0.1.7",
    author="Yassine Amjad",
    author_email="Yassine.amjad001@gmail.com",
    url="https://github.com/yassine20011/py-proxy-checker",
    description="A simple checkerproxy library",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=["checkerproxy"],
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",        
    ],
    python_requires='>=3.6',
    license='MIT',
    )
import setuptools

setuptools.setup(
    name="py-proxy-checker",
    version="0.1.2",
    author="Yassine Amjad",
    author_email="Yassine.amjad001@gmail.com",
    description="A simple checkerproxy library",
    packages=["checkerproxy"],
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    )
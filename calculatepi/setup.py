import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="calculatepi-pkg-Ramen-Nood1ez",
    version="0.0.9",
    author="Ramen Nood1ez",
    author_email="",
    description="A program that calculates pi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ramen-Nood1ez/CalculatePi/",
    project_urls={
        "Bug Tracker": "https://github.com/Ramen-Nood1ez/CalculatePi/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
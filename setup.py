import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
def _requires_from_file(filename):
    return open(filename, encoding="utf8").read().splitlines()

setuptools.setup(
    name="MySQLer",
    version="0.0.3",
    author="DMS",
    author_email="masato190411@gmail.com",
    description="table manager for aiomysql.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RextTeam/table-manager.py",
    install_requires=_requires_from_file('requirements.txt'),
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

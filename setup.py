import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open(f"mysqler/__init__.py", "r") as f:
    text = f.read()
    version = text.split('__version__ = "')[1].split('"')[0]

def _requires_from_file(filename):
    return open(filename, encoding="utf8").read().splitlines()

setuptools.setup(
    name="MySQLer",
    version=version,
    author="DMS",
    author_email="masato190411@gmail.com",
    maintainer="Rext",
    description="table manager for aiomysql.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RextTeam/MySQLer",
    project_urls={"Documentation": f"https://rextteam.github.io/MySQLer/"},
    install_requires=_requires_from_file('requirements.txt'),
    packages=setuptools.find_packages(),
    package_data={"mysqler": ("py.typed",)},
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

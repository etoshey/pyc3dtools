from setuptools import setup, find_packages

VERSION = '0.2.1'
DESCRIPTION = 'C3Dtools API package - Read c3d files'

with open("README.md", "r") as fh:
    long_description = fh.read()


# Setting up
setup(
    name="pyc3dtools",
    version=VERSION,
    author="Soroosh.b.k (C3Dtools.com)",
    author_email="<soroosh.b.k@gmail.com>",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['numpy','tqdm','requests'],    
    keywords=['python', 'c3d', 'motion capture', 'biomechanics'],
    license="MIT",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    url="https://github.com/etoshey/pyc3dtools",
    packages=find_packages(exclude=("exportData",))
)
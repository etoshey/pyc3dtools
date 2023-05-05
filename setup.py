from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'C3Dtools API package - Read c3d files'


# Setting up
setup(
    name="pyc3dtools",
    version=VERSION,
    author="Soroosh.b.k (C3Dtools.com)",
    author_email="<soroosh.b.k@gmail.com>",
    description=DESCRIPTION,
    install_requires=['numpy','tqdm'],
    keywords=['python', 'c3d', 'motion capture', 'biomechanics'],
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
from distutils.core import setup

setup(
    name='cached_property',
    version='1.0.0',
    author='Justus Schwabedal',
    author_email='jschwabedal@belco.tech',
    maintainer='Justus Schwabedal',
    maintainer_email='jschwabedal@belco.tech',
    packages=['cached_property'],
    long_description=open('README.md').read(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Apache License :: Version 2.0",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

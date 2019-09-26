import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='cached_property_bel',
    version='1.0.1',
    author='Justus Schwabedal',
    author_email='jschwabedal@belco.tech',
    maintainer='Justus Schwabedal',
    maintainer_email='jschwabedal@belco.tech',
    description="A cached-property decorator.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

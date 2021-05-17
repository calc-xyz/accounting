import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="accountingtools",
    version="0.0.1",
    author="Darek Chilimoniuk",
    author_email="darek@stack.pl",
    description="Double-entry accounting module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/calc-xyz/accounting",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

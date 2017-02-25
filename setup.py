# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <gogogo.vm@gmail.com>
"""

from __future__ import unicode_literals

import io
import os.path
import sys

import setuptools


REQUIREMENT_DIR = "requirements"
ENCODING = "utf8"

with io.open("README.rst", encoding=ENCODING) as f:
    long_description = f.read()

with io.open(
        os.path.join("docs", "pages", "introduction", "summary.txt"),
        encoding=ENCODING) as f:
    summary = f.read()

with open(os.path.join(REQUIREMENT_DIR, "requirements.txt")) as f:
    install_requires = [line.strip() for line in f if line.strip()]

with open(os.path.join(REQUIREMENT_DIR, "test_requirements.txt")) as f:
    tests_require = [line.strip() for line in f if line.strip()]

needs_pytest = set(["pytest", "test", "ptr"]).intersection(sys.argv)
pytest_runner = ["pytest-runner"] if needs_pytest else []

author = "Tsuyoshi Hombashi"
email = "gogogo.vm@gmail.com"
project_name = "typepy"

setuptools.setup(
    name=project_name,
    version="0.0.3",
    url="https://github.com/thombashi/{:s}".format(project_name),

    author=author,
    author_email=email,
    description=summary,
    include_package_data=True,
    install_requires=install_requires,
    keywords=["type", "validator", "converter"],
    license="MIT License",
    long_description=long_description,
    maintainer=author,
    maintainer_email=email,
    packages=setuptools.find_packages(exclude=["test*"]),
    setup_requires=[] + pytest_runner,
    tests_require=tests_require,

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

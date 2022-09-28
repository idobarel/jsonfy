from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Convert data class object and parse it to a json formated string.'
LONG_DESCRIPTION = 'Jsonfy is a python package that takes a data class object and parse it to a json formated string. You can use it to do the same thing, but in reverse as well.'

setup(
    name="jsonfy",
    version=VERSION,
    author="GodZilo (Ido Barel)",
    author_email="<vikbarel5@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=["python", "JSON", "json", "object"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ]
)
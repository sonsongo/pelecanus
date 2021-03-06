from setuptools import setup
import os
import codecs
import re

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    # intentionally *not* adding an encoding option to open
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

long_description = read('README.txt')


setup(
    name='pelecanus',
    packages=['pelecanus'],
    version=find_version('pelecanus', '__init__.py'),
    description='Python3 application for navigating and editing nested JSON',
    author='Erik Aker',
    author_email="eraker@gmail.org",
    url="https://github.com/pellagic-puffbomb/pelecanus",
    license="GNU General Public License v2",
    download_url="https://github.com/pellagic-puffbomb/pelecanus.git",
    keywords=["json", "hateoas"],
    tests_require=['nose', 'coverage'],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries"
        ],
    install_requires=[
    ],
    long_description=long_description
)

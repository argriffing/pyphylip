
from distutils.core import setup

from pyphylip import pyphylip_version


classifiers = [
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Bio-Informatics']

# This seems like a standard method.
long_description = open('README.rst').read()
short_description = 'a python module to read and write phylip alignment files'

setup(
        name = 'pyphylip',
        version = pyphylip_version,
        author = 'Alex Griffing',
        author_email = '',
        license = 'MIT',
        description = short_description,
        url = 'http://pypi.python.org/pypi/pyphylip',
        py_modules = ['pyphylip'],
        long_description = long_description,
        classifiers = classifiers)

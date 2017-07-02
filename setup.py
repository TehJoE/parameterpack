from setuptools import setup, find_packages
from codecs import open
from os import path
import re

here = path.abspath(path.dirname(__file__))
pattern = re.compile(r'^\.\. start-badges(.*)^\.\. end-badges\s*', re.MULTILINE | re.DOTALL)

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = re.sub(pattern, '', f.read())

setup(
    name='parameterpack',

    version='0.0.0',

    description='Ellipsis trickery for enabling fold expressions',
    long_description=long_description,

    url='https://github.com/TehJoE/parameterpack',

    author='Joe Lawson',
    author_email='',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',

        'Programming Language :: Python :: Implementation :: CPython',
    ],

    keywords='development fold functional pack unpack',

    packages=find_packages('src'),
    package_dir={'': 'src'},

    install_requires=[],

    tests_require=['pytest'],
    setup_requires=['pytest-runner'],

    extras_require={
        'dev': ['bumpversion', 'tox'],
    }
)

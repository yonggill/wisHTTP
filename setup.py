# Doesn't serve for python 2.x environment.

from wishttp import WISHTTP_VERSION
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='wisHTTP',
    version=WISHTTP_VERSION,
    author='yonggill',
    author_email='yonggill@wishket.com',
    packages=['wisHTTP'],
    url='https://wishttp.toolate.kr',
    license='LICENSE',
    description='light module for HTTP Request Client',
    install_requires=[

    ]
)

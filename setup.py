#!/usr/bin/env python

from distutils.core import setup


description = "A Facebook Python client."

VERSION = 'pre-0.1'

setup(
    name='python-facebook',
    version=VERSION,
    author='Glenn Siegman',
    author_email='gsiegman@gsiegman.com',
    url='https://github.com/gsiegman/python-facebook',
    description=description,
    long_description=description,
    license='BSD',
    platforms=['any',],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        ],
    packages=['facebook',],
    install_requires=['requests', 'bunch',]
)

# -*- coding: utf-8 -*-

import codecs
from os.path import abspath
from os.path import dirname
from os.path import join
from setuptools import find_packages
from setuptools import setup

import precise_bbcode


def read_relative_file(filename):
    """
    Returns contents of the given file, whose path is supposed relative
    to this module.
    """
    with codecs.open(join(dirname(abspath(__file__)), filename), encoding='utf-8') as f:
        return f.read()


setup(
    name='django-precise-bbcode',
    version=precise_bbcode.__version__,
    author='Morgan Aubert',
    author_email='morgan.aubert@zoho.com',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    url='https://github.com/ellmetha/django-precise-bbcode',
    license='BSD',
    description='A django BBCode integration..',
    long_description=read_relative_file('README.rst'),
    zip_safe=False,
    install_requires=[
        'django>=1.8',
        'pillow>=2.2.1',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)

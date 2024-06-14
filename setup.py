#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def get_version(*file_paths):
    """Retrieves the version from preferences_utils/__init__.py"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


version = get_version("preferences_utils", "__init__.py")


if sys.argv[-1] == 'publish':
    try:
        import wheel
        print("Wheel version: ", wheel.__version__)
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on git:")
    os.system("git tag -a %s -m 'build: bump version number to %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open('README.md').read()
history = open('HISTORY.md').read()

REPO_URL = 'https://github.com/otto-torino/django-preferences-utils'

setup(
    name='django-preferences-utils',
    version=version,
    description="""All you need for your django project settings""",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    author='abidibo',
    author_email='abidibo@gmail.com',
    url=REPO_URL,
    packages=[
        'preferences_utils',
        'preferences_utils.templatetags',
    ],
    include_package_data=True,
    license="MIT",
    zip_safe=False,
    keywords='django-preferences-utils',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django :: 4.2',
        'Framework :: Django :: 5.0',
        'Framework :: Django :: 5.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    project_urls={
        'Source': REPO_URL,
        'Tracker': REPO_URL + '/issues',
    },
)

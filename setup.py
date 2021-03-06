
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='cloud_desktop',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Amol Gupta',
    author_email='amolg98@gmail.com',
    url='https://github.com/amolg98/cloud_desktop',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
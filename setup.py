import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='mkdocs-snippet-plugin',
    version='1.0.2',
    description=
    'An mkdocs plugin that injects snippets from a file in a git repository',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    keywords='mkdocs python markdown snippet',
    url='https://github.com/mprivat/mkdocs-snippet-plugin',
    author='Michael Privat',
    author_email='Michael.Privat@availity.com',
    license='MIT',
    python_requires='>=2.7.9,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
    install_requires=['mkdocs>=0.17', 'gitpython'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(exclude=['*.tests']),
    entry_points={
        'mkdocs.plugins': ['snippet = snippet.plugin:SnippetPlugin']
    })

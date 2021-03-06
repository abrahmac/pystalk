import os.path
from setuptools import setup, find_packages

project_root = os.path.abspath(os.path.dirname(__file__))

install_requires = []
with open(os.path.join(project_root, 'requirements.txt'), 'r') as f:
    for line in f:
        install_requires.append(line.rstrip())

with open(os.path.join(project_root, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="pystalk",
    version="0.5.1",
    author="EasyPost",
    author_email="oss@easypost.com",
    url="https://github.com/easypost/pystalk",
    description="Very simple beanstalkd client",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="ISC",
    install_requires=install_requires,
    packages=find_packages(exclude=['tests']),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, <4',
    project_urls={
        'CI': 'https://travis-ci.org/EasyPost/pystalk',
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Database",
        "License :: OSI Approved :: ISC License (ISCL)",
    ]
)

from setuptools import setup, find_packages

setup(
    name='testtools',
    version='0.1.0',
    packages=find_packages(include=['testtools']),
    install_requires=[
        'numpy>=1.14.5',
        'matplotlib>=2.2.0'
    ]
)
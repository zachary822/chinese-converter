import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='chinese-converter',
    description='convert simplified chinese text to traditional chinese',
    version='1.0.2',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/zachary822/chinese-converter',
    author='Zachary Juang',
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['chinese_converter'],
    package_data={
        'chinese_converter': ['bigram.json', 'monogram.json', 'simplified.txt', 'traditional.txt']
    }
)

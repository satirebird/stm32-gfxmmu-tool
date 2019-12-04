#!/usr/bin/env python

import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()

REQUIREMENTS = [
    'Mako>=1.1.0',
]

setup(
    name='stm32-gfxmmu-tool',
    version='0.0.1',
    description='Generate c files for the gfxmmu lookup table',
    long_description=README,
    author='Sven Krauß',
    author_email='sven.krauss@web.de',
    url='https://github.com/satirebird/stm32-gfxmmu-tool',
    license="MIT",
    install_requires=REQUIREMENTS,
    keywords=['stm32', 'gfxmmu', 'lut'],
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
    ],
    entry_points={
        'console_scripts': ['stm32-gfxmmu-tool=stm32_gfxmmu_tool.main:main']
    },
)

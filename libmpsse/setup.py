#!/usr/bin/env python
from distutils.core import setup

setup(name='libmpsse',
      version='0.1',
      author='Craig Heffner',
      requires=['libmpsse'],
      scripts=['bin/bitbang',
               'bin/ds1305',
               'bin/gpio',
               'bin/i2ceeprom',
               'bin/spiflash'])

# -*- coding: utf-8 -*-
# @Author: Zymous
# @Date:   2017-04-28 16:56:29
# @Last Modified by:   Zymous
# @Last Modified time: 2017-04-28 17:15:45

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


config = {
    'description': 'My Tricks',
    'author': 'Zymous',
    'url': 'No url now',
    'download_url': "Where to download it.",
    'author_email': 'liaowu912@163.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['Tricks'],
    'scripts': [],
    'name': 'Tricks'
}

setup(**config)
import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, '../api_lib/README.rst')).read()

setup(
    name='api_lib',
    version='0.1',
    packages=['api_lib'],
    description='Lib for octopus and portal',
    long_description=README,
    author='Max Vakulenko',
    author_email='vakulenko.maxim@gmail.com',
    url='https://github.com/makvak/live-cv/',
    license='MIT',
    install_requires=[
    ]
)

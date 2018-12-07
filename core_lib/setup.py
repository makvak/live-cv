import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, '../core_lib/README.rst')).read()

setup(
    name='core_lib',
    version='0.1',
    packages=['core_lib'],
    description='Lib for common stuff like general requirement, consts, config functions...',
    long_description=README,
    author='Max Vakulenko',
    author_email='vakulenko.maxim@gmail.com',
    url='https://github.com/makvak/live-cv/',
    license='MIT',
    install_requires=[
        'django==2.1.4',
    ]
)

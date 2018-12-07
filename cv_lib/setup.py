import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, '../cv_lib/README.rst')).read()

setup(
    name='cv_lib',
    version='0.1',
    packages=['cv_lib'],
    description='Lib for image manager and image processor',
    long_description=README,
    author='Max Vakulenko',
    author_email='vakulenko.maxim@gmail.com',
    url='https://github.com/makvak/live-cv/',
    license='MIT',
    install_requires=[
        'django==2.1.4',
    ]
)

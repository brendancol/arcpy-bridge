from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

INSTALL_REQUIRES = [
]

TESTS_REQUIRES = [

]

setup(
    name='arcpy-bridge',
    version='0.0.1',
    description='Wrapper to spawn arcpy processes',
    url='https://github.com/brendancol/arcpy-bridge',
    author='Brendan Collins',
    author_email='brendancol@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRES,
    keywords='fme esri python arcpy',
)

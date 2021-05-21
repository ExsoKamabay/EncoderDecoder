import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

setup(
    name='kamabayEncoder',
    version='0.1.0',
    packages = find_packages(),
    include_package_data=True,
    description='decode encode data.',
    long_description = README,
    author='Exso Kamabay',
    url='https://github.com/ExsoKamabay/EncoderDecoder',
    license='Apache License 2.0',
    #install_requires=['url64', 'string-color', 'bs4','requests','art'],
    keywords = ['kamabay', 'encode', 'decode', 'encrypt', 'decrypt'],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],
)

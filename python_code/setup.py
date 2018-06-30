import sys, os
from distutils.core import setup
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

#script_name1 =  os.path.join('scripts', 'asciimath2fo.py')
#script_name2 =  os.path.join('scripts', 'asciimath2html.py')


setup(name="big_data_course_tools",
    version= ".2" ,
    description="tools for course",
    long_description=read('Readme.rst'),
    author="Paul Tremblay",
    author_email="Paul Henry Tremblay <paultremblay@gmail.com> ",
    license = 'BSD',
    url = "https://github.com/paulhtremblay/big_data_course",
    classifiers=[
        "Topic :: Big Data",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 3 - Development",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
    ],
    platforms='any',
    packages = find_packages(),
    #scripts=[script_name1, script_name2],
    data_files=[('big_data_course_data',
        ['big_data_course/data/isd.txt',
        'big_data_course/data/us_stations_keys.txt'
        ])],

    )

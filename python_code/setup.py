import sys, os
from distutils.core import setup
from setuptools import setup, find_packages

setup(name="course_tools",
    version= ".2" ,
    description="tools for course",
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
    #packages = find_packages(),
    packages=['course_tools/examples',
               'course_tools/map_reduce',
               'course_tools/misc',
               'course_tools/parsers',
                'course_tools/spark_code',
                ],

    )


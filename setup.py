#! /usr/bin/env python2.5
# -*- coding: utf-8 -*-


__author__ = 'Justin S Bayer, bayer.justin@googlemail.com'


from setuptools import setup, find_packages


setup(
    name="PyBrain2",
    version="0.4.0",
    description="PyBrain2 is the Swiss army knife for neural networking.",
    license="BSD",
    keywords="Neural Networks Machine Learning",
    url="http://pybrain2.org",
    packages=find_packages(exclude=['examples', 'docs']),
    include_package_data=True,
    test_suite='pybrain2.tests.runtests.make_test_suite',
    package_data={'pybrain': ['rl/environments/ode/models/*.xode']},
    install_requires = ["scipy"],
)

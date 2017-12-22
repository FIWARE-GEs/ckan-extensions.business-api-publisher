# -*- coding: utf-8 -*-

# Copyright (c) 2014 - 2017 CoNWeT Lab., Universidad Politécnica de Madrid

# This file is part of CKAN Store Publisher Extension.

# CKAN Store Publisher Extension is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# CKAN Store Publisher Extension is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with CKAN Store Publisher Extension.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages
import sys, os

version = '0.4'

setup(
    name='ckanext-baepublisher',
    version=version,
    description="CKAN extension that allows users to publish datasets in the FIWARE Store (as offerings) in a simpler way. To do so, a new tab is added in the Datasets Manage menu that offers a form to set the basic options of the offering.",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Aitor Magan, Francisco de la Vega',
    author_email='fdelavega@conwet.com',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.baepublisher'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'requests-oauthlib==0.5.0'
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        baepublisher=ckanext.baepublisher.plugin:StorePublisher
    ''',
)
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name="yemendata",
    version="0.1",
    author="ezzine",
    author_email="ezzine@hotmail.com",
    description="Code behind yemendata.org",
    long_description=(read('README')),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: GeoNode',
        'License :: OSI Approved :: GNU Library or General Public License (GPL)',
    ],
    license="GPL 3",
    keywords="yemendata geonode django",
    url='https://github.com/ezzine/Yemen-Data',
    scripts = [
               'scripts/yemendata',
              ],
    packages=find_packages('.'),
    include_package_data=True,
    zip_safe=False,
)

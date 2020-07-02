'''
familytoolswap_backend: Educational Webapp Project with Alex Gittemeier, Tom Gittemeier, Dan Telle, and Steve Telle

Note that "python setup.py test" invokes pytest on the package. With appropriately
configured setup.cfg, this will check both xxx_test modules and docstrings.

Copyright 2020, Alex Gittemeier, Tom Gittemeier, Dan Telle, Steve Telle.
Licensed under GPLv3.0.
'''
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

# This is a plug-in for setuptools that will invoke py.test
# when you run python setup.py test
class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest  # import here, because outside the required eggs aren't loaded yet
        sys.exit(pytest.main(self.test_args))


version = "0.1"

setup(name="familytoolswap_backend",
      version=version,
      description="Educational Webapp Project with Alex Gittemeier, Tom Gittemeier, Dan Telle, and Steve Telle",
      long_description=open("README.rst").read(),
      classifiers=[ # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 1 - Planning',
        'Programming Language :: Python'
      ],
      keywords="", # Separate with spaces
      author="Alex Gittemeier, Tom Gittemeier, Dan Telle, Steve Telle",
      author_email="gatormeier@yahoo.com",
      url="https://github.com/DATS-STL/DATS-backend",
      license="GPLv3.0",
      packages=find_packages(exclude=['examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      tests_require=['pytest'],
      cmdclass={'test': PyTest},
      
      # TODO: List of packages that this one depends upon:   
      install_requires=['flask'],
      # TODO: List executable scripts, provided by the package (this is just an example)
      entry_points={
        'console_scripts': 
            ['familytoolswap_backend=familytoolswap_backend:main']
      }
)

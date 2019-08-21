'''
this is the set-up file for the package
'''

from setuptools import setup
from setuptools import find_packages

setup(
    name='TimerWrapper',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.3',
    description='Timer for long time periods',

    # The project's main homepage.
    url='https://github.com/carvetighter/Timer',

    # Author details
    author='Brent Allen',
    author_email='carvetighter@gmail.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.5',
    ],

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    #packages=['<pacage name>, <package name>'],

)
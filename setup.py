import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.1.0'
PACKAGE_NAME = 'agrifoodpy_data'
AUTHOR = 'AgriFoodPy developers'
AUTHOR_EMAIL = 'juanpablo.cordero@york.ac.uk'
URL = 'https://github.com/FixOurFood/agrifoodpy-data'

LICENSE = 'BSD-3-Clause'
DESCRIPTION = 'Prepackaged data for the AgriFoodPy modelling package'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'xarray',
      'netcdf4',
]

EXTRAS_REQUIRE = {
      'geo': ['numpy', 'pandas', 'matplotlib', 'geopandas', 'shapely'],
}

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      extras_require=EXTRAS_REQUIRE,
      python_requires='>=3.9',
      classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Science/Research',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Programming Language :: Python :: 3.12',
            'Topic :: Scientific/Engineering',
      ],
      project_urls={
            'Source': URL,
            'Issues': f'{URL}/issues',
      },
      packages=find_packages(),
      include_package_data=True
      )

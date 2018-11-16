# import versioneer

from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name="openscm",
    version="v0.0.0",
    description="Description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/znicholls/example",
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        # "Development Status :: 3 - Alpha",
        # "Intended Audience :: Developers",
        # "License :: OSI Approved :: MIT License",
        # "Programming Language :: Python :: 3",
        # "Programming Language :: Python :: 3.5",
        # "Programming Language :: Python :: 3.6",
        # "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
    ],
    # keywords="simple climate model",
    # license="GNU Affero General Public License v3.0 or later",
    packages=["example"],
    install_requires=["numpy"],
    # project_urls={  # Optional
    #     "Bug Reports": "https://github.com/openclimatedata/openscm/issues",
    #     "Source": "https://github.com/openclimatedata/openscm/",
    # },
    # extras_require={
    #     "docs": ["sphinx >= 1.4", "sphinx_rtd_theme", "sphinx-autodoc-typehints"],
    #     "tests": ["pytest", "pytest-cov", "codecov", "nbval", "notebook"],
    #     "dev": [
    #         "setuptools>=38.6.0",
    #         "twine>=1.11.0",
    #         "wheel>=0.31.0",
    #         "black",
    #         "flake8",
    #         "pandas",
    #         "matplotlib",
    #         "numpy",
    #     ],
    # },
)

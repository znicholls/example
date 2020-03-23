import versioneer
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


PACKAGE_NAME = "example"
AUTHORS = [
    ("Zeb Zebedee", "zebedee.nicholls@climate-energy-college.org"),
]
URL = "https://github.com/znicholls/example"

DESCRIPTION = (
    "Minimal example of how to setup a pure Python repository for scientific research"
)
README = "README.rst"

SOURCE_DIR = "src"

REQUIREMENTS = ["numpy", "scipy"]
REQUIREMENTS_DEPLOY = ["twine>=1.11.0", "setuptools>=38.6.0", "wheel>=0.31.0"]
REQUIREMENTS_DOCS = ["sphinx>=1.4", "sphinx_rtd_theme"]
REQUIREMENTS_TESTS = ["codecov", "pytest-cov", "pytest>=4.0"]

REQUIREMENTS_DEV = [
    *["flake8"],
    *REQUIREMENTS_DEPLOY,
    *REQUIREMENTS_DOCS,
    *REQUIREMENTS_TESTS,
]

REQUIREMENTS_EXTRAS = {
    "deploy": REQUIREMENTS_DEPLOY,
    "docs": REQUIREMENTS_DOCS,
    "tests": REQUIREMENTS_TESTS,
    "dev": REQUIREMENTS_DEV,
}

with open(README, "r") as readme_file:
    README_TEXT = readme_file.read()


class Example(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        pytest.main(self.test_args)


cmdclass = versioneer.get_cmdclass()
cmdclass.update({"test": Example})

setup(
    name=PACKAGE_NAME,
    version=versioneer.get_version(),
    description=DESCRIPTION,
    long_description=README_TEXT,
    long_description_content_type="text/x-rst",
    author=", ".join([author[0] for author in AUTHORS]),
    author_email=", ".join([author[1] for author in AUTHORS]),
    url=URL,
    # license="2-Clause BSD License",  # TODO add license guide resources
    classifiers=[  # full list at https://pypi.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 4 - Beta",
        # "License :: OSI Approved :: BSD License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
    ],
    keywords=["example", "python", "repo"],
    packages=find_packages(SOURCE_DIR),  # no exclude as only searching in `src`
    package_dir={"": SOURCE_DIR},
    # next line is only required if you have data files that have to be included
    # e.g. csvs which define certain conventions etc.
    # include_package_data=True,
    # TODO: add link to how requirements work in detail
    install_requires=REQUIREMENTS,
    extras_require=REQUIREMENTS_EXTRAS,
    # TODO: add resources on cmdclass
    cmdclass=cmdclass,
    # TODO: add resources on entry points
    # entry_points={
    #     "console_scripts": [
    #         "example-cli-hello=example.cli:hello",
    #     ]
    # },
)

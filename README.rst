Example
=======

.. sec-begin-index

+-------------------+---------+-----------+
| Repository health | |CI CD| | |Codecov| |
+-------------------+---------+-----------+

+-----------------+------------------+
| Latest releases | |Latest Version| |
+-----------------+------------------+

+-----------------+----------------+---------------+
| Latest activity | |Contributors| | |Last Commit| |
+-----------------+----------------+---------------+

**Minimum requirements for a reproducible, one line install package with continuous integration**

#. ``README.rst``: start with something basic which just notes down initial thoughts
#. fill out setup.py
#. fill out setup.cfg (TODO: explain setup.cfg file)
#. add basic directory structure, ``mkdir -p src/example``, ``touch src/example/__init__.py`` (change example to your package name in these paths)
#. add gitignore file (python template is easy, add `*.DS_Store` if working on osx)
#. add Makefile with basics
#. make first venv, ``make first-venv``
#. ``source ./venv/bin/activate`` (path could be different here if people get fancy with paths) (make sure conda isn't active so you don't get weird stuff happening)
#. ``versioneer install`` (https://github.com/warner/python-versioneer)
#. make your actual venv, ``deactivate``, ``make -B virtual-environment``, ``source ./venv/bin/activate`` (can't do make venv as then you get circular dependency)
#. add tests directories, ``mkdir -p tests/unit``, ``mkdir -p tests/integration`` (TODO: add explanation on what these are)
#. setup code coverage output to be sensible, ``.coveragerc``
#. setup an example test by putting the following in ``tests/unit/test_utils.py``

.. code-block:: python

    from example.utils import add_example


    def test_addition():
        expected = 4
        result = add_example(1, 3)

        assert expected == result

#. test that the test fails by running ``make test``
#. add code to pass the test in ``src/example/utils.py``

.. code-block:: python

    def add_example(first, second):
        """
        Add the inputs

        Parameters
        ----------
        first : Any
            First input to add

        second : Any
            Second input to add

        Returns
        -------
        Any
            Sum of the inputs
        """
        return first + second


#. test that the test passes and code coverage is 100% by running ``make test``
#. add GitHub pull request template, issue template and CI/CD (TODO explanation of how things work)
#. add code coverage settings, ``.codecov.yml``
#. push check that CI runs and passes and that a code coverage report is generated

--- End of minimal setup ---

Beyond this minimal setup, there are lots of other things which can be done (see list below).
If you'd like to learn about or contribute guides to any of these please make a pull request on which we can discuss!

- automatic documentation with sphinx and read the docs
- CHANGELOGS
- releasing with PyPI/pip and conda
- examples of repository usage with jupyter notebooks (and testing of notebooks)
- in depth code linting with packages like mypy and pylint

.. sec-end-index

.. contents:: :depth: 2

Contributing
------------

If you'd like to contribute, please make a pull request!
The pull request templates should ensure that you provide all the necessary information.

.. sec-begin-license

License
-------

This collection is licensed under a `Creative Commons CC0 license <https://creativecommons.org/publicdomain/zero/1.0/>`_,
unless noted otherwise for specific parts:

    The person who associated a work with this deed has dedicated the work to the
    public domain by waiving all of his or her rights to the work worldwide under
    copyright law, including all related and neighboring rights, to the extent allowed
    by law. You can copy, modify, distribute and perform the work, even for commercial
    purposes, all without asking permission.

.. sec-end-license

.. sec-begin-links

.. |CI CD| image:: https://github.com/znicholls/example/workflows/Example%20CI-CD/badge.svg
    :target: https://github.com/znicholls/example/actions?query=workflow%3A%22Example+CI-CD%22
.. |Codecov| image:: https://img.shields.io/codecov/c/github/znicholls/example.svg
    :target: https://codecov.io/gh/znicholls/example/branch/master/graph/badge.svg
.. |Latest Version| image:: https://img.shields.io/github/tag/znicholls/example.svg
    :target: https://github.com/znicholls/example/releases
.. |Last Commit| image:: https://img.shields.io/github/last-commit/znicholls/example.svg
    :target: https://github.com/znicholls/example/commits/master
.. |Contributors| image:: https://img.shields.io/github/contributors/znicholls/example.svg
    :target: https://github.com/znicholls/example/graphs/contributors

.. sec-end-links

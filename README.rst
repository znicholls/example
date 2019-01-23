Example
=======

.. sec-begin-index

Temporary notes:

#. README: start with something basic which just notes down initial thoughts
#. fill out setup.py
#. fill out setup.cfg (TODO: explain setup.cfg file)
#. add basic directory structure, `mkdir -p src/example`, `touch src/example/__init__.py` (change example to your package name in these paths)
#. add gitignore file (python template is easy, add `*.DS_Store` if working on osx)
#. add Makefile with basics
#. make first venv, `make first-venv`
#. source ./venv/bin/activate (path could be different here if people get fancy with paths) (make sure conda isn't active so you don't get weird stuff happening)
#. versioneer install (https://github.com/warner/python-versioneer)
#. make your actual venv, `deactivate`, `make virtual-environment`, `source ./venv/bin/activate` (can't do make venv as then you get circular dependency)
#. add tests directories, `mkdir -p tests/unit`, `mkdir -p tests/integration` (TODO: add explanation on what these are)
#. setup code coverage output to be sensible, `.coveragerc`
#. setup an example test by putting the following in `tests/unit/test_utils.py`



.. code-block:: python

    from example.utils import add_example


    def test_addition():
        expected = 4
        result = add_example(1, 3)

        assert expected == result

#. test that the test fails by running `make test`

#. sphinx

An example of how to setup a pure Python repository.
The repository includes examples of:

- packaging
- testing
- automatic documentation with Sphinx
- contributing guide
- license
- github pull request and issue templates
- code coverage
- easy version tracking with versioneer
- automating repetitive tasks with make
- changelog
- continuous integration using travis

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

===================
Python Markdown Doc
===================

.. start-badges


|travis|
|codecov|
|landscape|
|version|
|wheel|
|pyup|
|gitter|


.. |travis| image:: https://travis-ci.org/Pawamoy/pymarkdoc.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/Pawamoy/pymarkdoc/

.. |codecov| image:: https://codecov.io/github/Pawamoy/pymarkdoc/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/Pawamoy/pymarkdoc/

.. |landscape| image:: https://landscape.io/github/Pawamoy/pymarkdoc/master/landscape.svg?style=flat
    :target: https://landscape.io/github/Pawamoy/pymarkdoc/
    :alt: Code Quality Status

.. |pyup| image:: https://pyup.io/repos/github/pawamoy/pymarkdoc/shield.svg
    :target: https://pyup.io/repos/github/pawamoy/pymarkdoc/
    :alt: Updates

.. |gitter| image:: https://badges.gitter.im/Pawamoy/pymarkdoc.svg
    :alt: Join the chat at https://gitter.im/Pawamoy/pymarkdoc
    :target: https://gitter.im/Pawamoy/pymarkdoc?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

.. |version| image:: https://img.shields.io/pypi/v/pymarkdoc.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/pymarkdoc/

.. |wheel| image:: https://img.shields.io/pypi/wheel/pymarkdoc.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/pymarkdoc/


.. end-badges

Generate Markdown doc from your Python docstrings

License
=======

Software licensed under `MPL 2.0`_ license.

.. _MPL 2.0 : https://www.mozilla.org/en-US/MPL/2.0/

Installation
============

::

    pip install pymarkdoc

Documentation
=============

https://github.com/Pawamoy/pymarkdoc/wiki

Development
===========

To run all the tests: ``tox``

I need help to make this tool available on command line.
The thing is that `getdoc`_ needs a module as an object to get its documentation,
so we have to import it. To import it, all the modules it is importing
have to be installed (either on the system or in the current virtual environment). Python
path also must have been set correctly. Even more, in the case of a Django project, settings
have to be set up. This require many options and checks to be developed!

.. _getdoc : https://github.com/Pawamoy/python-getdoc

Todo:

- Make tool available on command line
- Add a command-line option to specify a virtualenv to activate
- Add command-line options to work with frameworks (Django, Flask, ...)
- Add command-line options to configure the rendering method

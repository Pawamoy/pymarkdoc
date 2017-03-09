===================
Python Markdown Doc
===================

.. start-badges


|travis|
|version|
|wheel|
|pyup|
|gitter|


.. |travis| image:: https://travis-ci.org/Pawamoy/pymarkdoc.svg?branch=master
    :target: https://travis-ci.org/Pawamoy/pymarkdoc/
    :alt: Travis-CI Build Status

.. |pyup| image:: https://pyup.io/repos/github/Pawamoy/pymarkdoc/shield.svg
    :target: https://pyup.io/repos/github/Pawamoy/pymarkdoc/
    :alt: Updates

.. |gitter| image:: https://badges.gitter.im/Pawamoy/pymarkdoc.svg
    :target: https://gitter.im/Pawamoy/pymarkdoc
    :alt: Join the chat at https://gitter.im/Pawamoy/pymarkdoc

.. |version| image:: https://img.shields.io/pypi/v/pymarkdoc.svg?style=flat
    :target: https://pypi.python.org/pypi/pymarkdoc/
    :alt: PyPI Package latest release

.. |wheel| image:: https://img.shields.io/pypi/wheel/pymarkdoc.svg?style=flat
    :target: https://pypi.python.org/pypi/pymarkdoc/
    :alt: PyPI Wheel


.. end-badges

Generate Markdown doc from your Python docstrings

License
=======

Software licensed under `ISC`_ license.

.. _ISC: https://www.isc.org/downloads/software-support-policy/isc-license/

Installation
============

::

    pip install pymarkdoc

Documentation
=============

http://pymarkdoc.readthedocs.io/en/latest/


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

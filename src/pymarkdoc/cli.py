"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mpymarkdoc` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``pymarkdoc.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``pymarkdoc.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
from os.path import join, basename, dirname, isfile, isdir, abspath
from os import listdir
import sys

import click
from getdoc import get_module_doc


def _get_doc(path):
    try:
        top_dir = __import__(basename(path))
    except ImportError:
        click.echo('pymarkdoc: import error %s' % basename(path))
        return None
    if not hasattr(top_dir, '__file__'):
        click.echo('pymarkdoc: %s is not a package/module' % path)
        return None
    else:
        return get_module_doc(top_dir)


@click.command()
@click.argument('names', nargs=-1)
def main(names):
    paths = list(names)
    if len(paths) == 0:
        paths.append('.')

    for path in paths:
        absolute_path = abspath(path)
        sys.path.append(dirname(absolute_path))
        sys.path.append(absolute_path)

        doc = _get_doc(absolute_path)
        if doc is not None:
            for d in doc:
                click.echo(d)

# -*- coding: utf-8 -*-

"""Main test script."""


from click.testing import CliRunner

from pymarkdoc.cli import main


def test_main():
    """Main test method."""

    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.output == '()\n'
    assert result.exit_code == 0

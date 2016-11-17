
from click.testing import CliRunner

from pymarkdoc.cli import main


def test_main():
    runner = CliRunner()
    result = runner.invoke(main, [])

    return True

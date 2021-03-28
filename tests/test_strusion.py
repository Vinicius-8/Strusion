# importing from parent folder
import pytest
import os
import sys
import inspect

sys.path.append('..')
absolute_path = os.path.abspath(inspect.getfile(inspect.currentframe()))
current_dir = os.path.dirname(absolute_path)
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

PATH = sys.path[0]

from Strusion import strusion


def test_config_default_output():
    sub = strusion.config_default_output('my_subtitle.srt')

    assert sub == 'my_subtitle.mod.srt'


# with pytest.raises(Exception):
# strusion.config_default_output('my_subtitle.ass')


def test_is_srt():
    sub = strusion.is_srt('my_subtitle.srt')

    assert sub

    sub = strusion.is_srt('my_subtitle.srv')

    assert not sub


def test_main():
    with pytest.raises(SystemExit):
        strusion.main() == None

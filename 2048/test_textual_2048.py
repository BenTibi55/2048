from pytest import *
from textual_2048 import *
import builtins


def test_read_player_command(monkeypatch):
    monkeypatch.setattr(builtins, "input", mock_input_return)
    assert read_player_command() in ['g', 'd', 'h', 'b']



from src.Keyboard import Keyboard

kb = Keyboard('White Project 007', 5000, 3)

assert str(kb) == 'White Project 007'

kb.change_lang()
assert str(kb.language) == 'RU'
kb.change_lang()
assert str(kb.language) == 'EN'
kb.change_lang()
assert str(kb.language) == 'RU'
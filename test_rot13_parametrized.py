'''
	Test1
	Test ROT13 with various arbitrary letters, indicating expected input and output
'''
import pytest	
from rot13 import rot13

@pytest.mark.parametrize(("input", "expected"), [
	("A", "N"),
	("a", "n"),
	("S", "F"),
	("x", "k")
])
	
def test_eval(input, expected):
	assert rot13(input) == expected


	
	



 

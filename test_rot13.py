'''
	Test1
	Test ROT13 with an arbitrary letter that which when added 13 will be beyond Z or z
'''
	
import pytest

from rot13 import rot13


def  test_rot13():
	result =  rot13("U")
	return result
	
result = test_rot13()

assert result=="H"
	
	



 

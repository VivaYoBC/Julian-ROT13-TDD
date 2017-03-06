
import sys
from rot13 import rot13

def test_rot13_file_read_completely_into_memory():	
	r = []
	with open("rotfile.txt", "r") as f:
		data = f.read()
		for x in data:
			if x == '\n':
				r += "\n"
			else:
				r += rot13(x)
	return str("".join(r))		
	
expected = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm\nGur Dhvpx Oebja Sbk Whzcf Bire Gur Ynml Qbt\nYn Encvqn Mbeen Pnsr Oevapn Rapvzn qry Creeb Sybwb\n"

assert test_rot13_file_read_completely_into_memory() == expected

# result = test_rot13_file_read_completely_into_memory()
# print(result == expected)

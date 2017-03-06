
import sys
from rot13 import rot13

def test_rot13_file_line_at_a_time():	
	r = []
	 
	with open("rotfile.txt", "r") as f:
		for line in f:
			l = [rot13(x) for x in line]
			l = "".join(l)
			r += l
			r += "\n"
	return str("".join(r))		
	
expected = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm\nGur Dhvpx Oebja Sbk Whzcf Bire Gur Ynml Qbt\nYn Encvqn Mbeen Pnsr Oevapn Rapvzn qry Creeb Sybwb\n"
	
assert test_rot13_file_line_at_a_time() == expected

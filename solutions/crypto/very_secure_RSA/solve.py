# copy out.txt to a new file (out.py) in order to import from it e, N and ciphertext as variables
from out import e, N, ciphertext
from string import ascii_letters, digits

charset = ascii_letters + digits + "_{}" # these are the only chars that can be in the flag according to the given regexp

dec = ""

for enc in ciphertext: # iterate over all encrypted chars
	for c in charset: # for each encrypted char, bruteforce possible chars until a match is found
		if pow(ord(c), e, N) == enc: # if it matches, append to the decrypted string and move on to the next encrypted char
			dec += c
			break

print(dec)

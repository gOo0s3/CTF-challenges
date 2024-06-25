from Crypto.PublicKey import RSA

with open("flag.txt") as flag_file:
	flag = flag_file.read().strip()

pub_key = RSA.generate(2048).public_key()

e = pub_key.e
N = pub_key.n
ciphertext = [pow(ord(c), e, N) for c in flag]

print(f"{e = }\n{N = }\n{ciphertext = }")

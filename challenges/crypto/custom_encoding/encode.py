chars = input("Enter plaintext: ")

lookup1 = "_{}!1234567890abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

out = ""

prev = 0
for char in chars:
	cur = lookup1.index(char)
	out += lookup2[(cur - prev) % 40]
	prev = cur

print(f"Ciphertext: {out}")

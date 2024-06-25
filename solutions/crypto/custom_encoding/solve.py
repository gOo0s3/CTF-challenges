lookup1 = "_{}!1234567890abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

ciphertext = "TGjGbrPbGbgiLoHjKgbNaoQPHlEaHLQcmdMlSPIQTcTpBECAEkgbBCqfL"

decoded = ""

prev = 0
for char in ciphertext:
	cur = lookup2.index(char)
	decoded += lookup1[(cur + prev) % 40]
	prev += cur % 40

print(f"{decoded = }")

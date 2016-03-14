# Unshamefully stolen from https://gist.github.com/deeplook/4947835
# To make this display indefinitely remove n < 50 and n += 1 and replace
# n < 50 with while True

from pyfiglet import figlet_format
from termcolor import cprint
from time import sleep

fout = open("last_digit.txt", "w")

pi = ""
n = 0
k, a, b, a1, b1 = 2, 4, 1, 12, 4
while True:
	p, q, k = k * k, 2 * k + 1, k + 1
	a, b, a1, b1 = a1, b1, p * a + q * a1, p * b + q * b1
	d, d1 = a / b, a1 / b1
	while d == d1:
		fout.write(str(d) + "\n")
		pi += str(d)
		# if(n < 8):
		a, a1 = 10 * (a % b), 10 * (a1 % b1)
		d, d1 = a / b, a1 / b1
		n += 1
		if(n == 8):
			cprint(figlet_format(pi, font="starwars"))
			pi = ""
			n = 0
			sleep(0.5)

def do_fizzbuzz():
	"""
	fizzbuzz : print fizz buzz fizzbuzz
	3: fizz
	5: buzz
	15: fizzbuzz
	ect: num
	"""

	for i in range(1,11) :
		if i%3 == 0 :
			print("fizz")
		else :
			print(i)

if __name__=='__main__':
	do_fizzbuzz()

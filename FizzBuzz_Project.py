
def fizzbuzz(numbers):
	for number in numbers:
		if number % 3 == 0 and number % 5 == 0:
		   print "fizzbuzz and", number
		elif number % 3 == 0:
			 print "fizz"
		elif number % 5 == 0:
			 print "buzz"

if __name__ == "__main__":
   print "Main is being called"
   numbers = range(1,100)
   fizzbuzz(numbers)
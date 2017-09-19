class Dog(object):
	def print_self(self):
		print("i am dog")
class Xiaotq(Dog):
	def print_self(self):
		print("i am xiaotq")

def introduce(temp):
	temp.print_self()


dog = Dog()
xiaotq = Xiaotq()

introduce(dog)
introduce(xiaotq)

class Animal:
	def eat(self):
		print("***eat***")
	def drink(self):
		print("***drink***")
	def sleep(self):
		print("***sleep***")
	def run(self):
		print("***run***")

class Dog(Animal):#继承父类
	def bark(self):
		print("***汪汪汪***")
class Xiaotq(Dog):#继承父类的父类
	def fly(self):
		print("***fly***")
		
		
dog = Dog()
dog.bark()
dog.run()
xiaottq = Xiaotq()
xiaottq.fly()
xiaottq.bark()
xiaottq.sleep()

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
class labuladuo(Dog):
	def bark(self):#重写
		print("***唔汪汪唔汪汪***")
	def bark_father(self):#调用被重写的方法
		Dog.bark(self)#第一种
		super().bark()#第二种

labuladuo1 = labuladuo()
labuladuo1.bark_father()
labuladuo1.bark()

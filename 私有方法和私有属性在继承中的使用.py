class A:
	def __init__(self):
		self.num1 = "公有属性"
		self.__num2 = "私有属性"
	def __str__(self):
		return "父类"
	def test1(self):
		print("*******共有方法*******") 
	def __test2(self):
		print("****私有方法****")
	def test3(self):#子类可以调用父类调用私有属性的共有方法
		print("****公有方法*****")
		print(self.__num2)

class B(A):
	def __str__(self):
		return "子类"
	#def test4(self):
	#	self.__test2()
	#	print(self.__num2)
#在子类中不可以直接调用父类的私有属性和私有方法
	pass

a = A()
print(a)

b = B()
print(b)
b.test1()
print(b.num1)
b.test3()
#b.test4()
#print(b.__num)
#b.__test2()

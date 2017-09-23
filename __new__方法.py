class Dog(object):
	def __init__(self):
		print("*****init class******")
	def __del__(self):
		print("*****del class******")
	def __str__(self):
		print("*****str class******")
	def __new__(cls):
		print(id(cls))
		print("*****new class******")
		return object.__new__(cls)#调用父类的new方法

print(id(Dog))
xtq = Dog()
#当重写了父类的__new__方法时,没重写时,默认调用父类的__new_方法
#创建一个对象相当于做了三件事情
#1.调用__new__方法创建对象,然后找一个变量来接受new的返回值,这个返回值便是创建出来的对象的引用
#2.__init__(刚刚创建出的对象的引用)
#3.返回对象的引用

'''
new方法只负责创建对象
init方法只负责初始化对象

'''

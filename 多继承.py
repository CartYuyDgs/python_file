class Base(object):#有object就是新式类,没有就是经典类
	def test1(self):
		print("test1*******")
	def test(self):
		print("********Base")
class A(Base):
	def test2(self):
		print("test2*******")
	def test(self):
		print("********A")
class B(Base):
	def test3(self):
		print("test3*******")
	def test(self):
		print("********B")

class C(A,B):#多继承
	def test(self):#相当于重写
		#print("********C")
		B.test(self)#指定调用某个父类的方法
	

c = C()
c.test1()
c.test2()
c.test3()
c.test()
print(C.__mro__)#打印调用某个方法时搜索顺序

class Test(object):
	def __init__(self,swith):
		self.switch = swith
	def calc(self,a,c):
		try:
			return a/c
		except Exception as result:
			if self.switch:
				print("捕获开启")
				print(result)
			else:
				raise
'''
def judge(a):
	if a== "True":
		return 1
	elif a == "False":
		return 1
	else:
		return 0
b = input("请输入一个值,True或者False:")
if judge(b) == 1:
	c = Test(b)
	c.calc(11,0)
else:
	print("输入错误,程序退出!")
'''
c= Test(True)
c.calc(11,0)
d = Test(False)
d.calc(11,0)

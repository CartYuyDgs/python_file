class ShortInputExcept(Exception):
	def __init__(self,lenth,atleast):
		self.lenth = lenth
		self.atleast = atleast

def main():
	try:
		s = input("请输入-->")
		if(len(s)<3):
			#raise,引发一个自定义的异常
			raise ShortInputExcept(len(s),3)
	except ShortInputExcept as result:
		print("ShortInputExcept: 输入的长度是:",result.lenth,"长度至少是:",result.atleast)
	else:
		print("没有异常发生")

main()

lass Game(object):
	
	num = 0#类属性
	#实例方法
	def __init__(self):#self可以改变
		self.name = 'laowang'
		self.num +=10#实例属性
	@classmethod #类方法	
	def add_num(cls):#cls可以改变
		cls.num += 100
	#静态方法	
	@staticmethod
	def print_num():#可以没有参数
		print('*******************')
		print('穿越火线')
		print('1.开始游戏')
		print('2.结束游戏')
		print('*******************')
game = Game()
print(game.num)
Game.add_num()#可以通过类的名字调用类方法
print(game.num)
print(Game.num)
game.add_num()#也可以调用这个类创造出的对象调用类方法
print(Game.num)
print(game.num)
#调用静态方法
Game.print_num()
game.print_num()

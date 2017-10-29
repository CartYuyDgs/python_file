

class Person(object):
	"""docstring for Person"""
	def __init__(self, name):
		self.name = name
		self.hp = 100
		self.gun = None
	def anzhaung_zidan(self,danjia_temp,zidan_temp):
		danjia_temp.baocun_zidan(zidan_temp)
	def anzhaung_danjia(self,gun_temp,danjia_temp):
		gun_temp.baocun_danjia(danjia_temp)
	def na_qiang(self,gun_temp):
		self.gun = gun_temp
	def koubanji(self,diren):
		self.gun.kaihuo(diren)
	def diaoxue(self,shanghai_pro):
		self.hp-=shanghai_pro
	def __str__(self):
		if self.gun:
			return "my name is %s,i have gun,my hp is %d"%(self.name,self.hp)
		else:
			if self.hp>0:
				return "my name is %s,i have not gun,my hp is %d"%(self.name,self.hp)
			else:
				return "%s:i am die!"%(self.name)
class Gun(object):
	"""docstring for Gun"""
	def __init__(self, name):
		self.name = name
		self.danjia = None
	def __str__(self):
		return "%s"%(self.name)
	def baocun_danjia(self,danjia_pro):
		self.danjia = danjia_pro
	def kaihuo(self,diren):
		zidan_temp = self.danjia.tanchu_zidan()
		if zidan_temp:
			zidan_temp.dazhong(diren)
		else:
			print("no zidan!")
class Danjia(object):
	"""docstring for Danjia"""
	def __init__(self, max):
		self.max = max
		self.zidan_list = []
	def baocun_zidan(self,zidan_pro):
		self.zidan_list.append(zidan_pro)
	def tanchu_zidan(self):
		if self.zidan_list:
			return self.zidan_list.pop()
		else:
			return None
	def __str__(self):
		return "info of danjia:max:%d/%d"%(len(self.zidan_list),self.max)
class Zidan(object):
	"""docstring for Zidan"""
	def __init__(self, shanghai):
		self.shanghai = shanghai
	def __str__(self):
		return "info of zidan:shanghai:%d"%(self.shanghai)
	def dazhong(self,diren):
		diren.diaoxue(self.shanghai)
def main():
	'''creat a person laowang'''
	lao_wang = Person("laowang")
	'''creat a Gun'''
	AK47 = Gun("ak47")
	'''creat a danjia'''
	dan_jia = Danjia(100)
	'''creat same zidans'''
	for i in range(20):
		zidan = Zidan(20)
	'''Creat a laosong'''
	lao_song = Person("laosong")
	'''ba zidan anzhuang daodanjia'''
	for i in range(20):
		lao_wang.anzhaung_zidan(dan_jia,zidan)
	'''ba danjia anzhuang dao qiang'''
	
	lao_wang.anzhaung_danjia(AK47,dan_jia)
	'''laowang an qiang'''
	lao_wang.na_qiang(AK47)
	'''kou ban ji'''
	'''laowang koubanji'''
	lao_wang.koubanji(lao_song)
	'''
	print(lao_wang)
	print(AK47)
	print(dan_jia)
	print(zidan)
	'''
	print(AK47)
	print(lao_song)
	lao_wang.koubanji(lao_song)
	print(AK47)
	print(lao_song)
	lao_wang.koubanji(lao_song)
	print(AK47)
	print(lao_song)
	lao_wang.koubanji(lao_song)
	print(AK47)
	print(lao_song)
	lao_wang.koubanji(lao_song)
	print(AK47)
	print(lao_song)
	lao_wang.koubanji(lao_song)
	print(AK47)
	print(lao_song)
	lao_wang.koubanji(lao_song)

if __name__ == '__main__':
	main()


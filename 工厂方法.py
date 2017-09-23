class Story(object):#店铺类
		
		def select_car(self):
			pass

		def order(self,car_type):
			return self.select_car(car_type)

#创建两个4S店

class CarStore(Story):
	def select_car(self,car_type):#方法重写
		return Factory().select_car_by_type(car_type)

class BMWstory(Story):
	def select_car(self,car_type):
		return BMWFactory().select_car_by_type(car_type)	

#工厂类
class Factory(object):#解耦
	def select_car_by_type(self,car_type):
		if car_type == "beijing":
			return BeiJ()
		else:
			return Fengs()
class BMWFactory(object):
	pass
class Car(object):
	def move(self):
		print('move...')
	def music(self):
		print('music...')
	def stop(self):
		print('stop...')

#汽车类
class Fengs(Car):
	def __init__(self):
		print("*********fengs************")
class BeiJ(Car):
	def __init__(self):
		print("*********beijing************")


car_story = CarStore()
car = car_story.order("beijing")
car.move()
car.music()
car.stop()
car2 = car_story.order("fengs")

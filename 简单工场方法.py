class CarStore(object):#店铺类
	def __init__(self):
		self.factory = Factory()
	def order(self,car_type):
		return self.factory.select_car_by_type(car_type)
		

class Factory(object):#解耦
	def select_car_by_type(self,car_type):
		if car_type == "beijing":
			return BeiJ()
		else:
			return Fengs()
class Car(object):
	def move(self):
		print('move...')
	def music(self):
		print('music...')
	def stop(self):
		print('stop...')

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

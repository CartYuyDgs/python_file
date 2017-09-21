class CarStore(object):
	def order(self,car_type):
		if car_type == "beijing":
			return BeiJ()
		else:
			return fengs()

class Car(object):
	def move(self):
		print('move...')
	def music(self):
		print('music...')
	def stop(self):
		print('stop...')

class fengs(Car):
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
car.move()
car.music()
car.stop()

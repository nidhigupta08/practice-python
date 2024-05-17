class Transportation:
    def travel_time(self, distance):
        pass

class Car(Transportation):
    def travel_time(self, distance):
        speed = 60  # average speed in mph
        return distance / speed

class Bicycle(Transportation):
    def travel_time(self, distance):
        speed = 15  # average speed in mph
        return distance / speed

class Train(Transportation):
    def travel_time(self, distance):
        speed = 80  # average speed in mph
        return distance / speed

# Usage
car = Car()
print("Travel time by car for 120 miles:", car.travel_time(120))

bicycle = Bicycle()
print("Travel time by bicycle for 20 miles:", bicycle.travel_time(20))

train = Train()
print("Travel time by train for 200 miles:", train.travel_time(200))

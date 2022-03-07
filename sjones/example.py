class Car():
    def exclaim(self):
        print("I am a Car!")
    
class Yugo(Car):
    def exclaim(self):

car_call= Car()
yugo_call = Car() 

car_call.exclaim()

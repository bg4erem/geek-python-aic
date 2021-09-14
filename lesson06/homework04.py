class Car:
    speed: str
    color: str
    name: str
    is_police = False

    def __init__(self,speed,color,name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        if self.speed > 0:
            print(f"The car is on way with speed of {self.speed}")
        else:
            self.speed = 5
            print(f"The car started going, speed {self.speed}")

    def stop(self):
        print(f"The car is stopped")
        self.speed = 0

    def turn(self,direction):
        print(f"The car turned {direction}")

    def show_speed(self):
        print(f"Current speed is {self.speed}")

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed <60:
            print(f"Current speed is {self.speed}")
        else:
            print(f"Current speed is {self.speed}. You are overspeeding the limit 60, overspeed is {self.speed - 60})")

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed <40:
            print(f"Current speed is {self.speed}")
        else:
            print(f"Current speed is {self.speed}. You are overspeeding the limit 40, overspeed is {self.speed - 40})")

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
    is_police = True


honda_fit = TownCar(70,"black",'Fit')
honda_fit.show_speed()
honda_fit.stop()
honda_fit.show_speed()

ford_police = PoliceCar(100, "white and blue", "Ford")
ford_police.go()
ford_police.turn('right')
ford_police.show_speed()


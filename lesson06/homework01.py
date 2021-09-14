import time


class TrafficLight:
    __color: str
    import time

    def running(self, greentime):
        __color = "Red"
        print(__color)
        time.sleep(7)
        __color = "Yellow"
        print(__color)
        time.sleep(2)
        __color = "GREEN"
        print(__color)
        time.sleep(greentime)
        __color = "red"

a = TrafficLight()
a.running(15)
class Road:
    _length: int
    _width: int

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass_calc(self, thickness):
        result = self._length * self._width * 0.025 * thickness
        print(f"Необходимо {round(result)} т асфальта")

E36 = Road(4500, 40)
E36.asphalt_mass_calc(7)

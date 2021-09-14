class Stationery:
    title: str

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Запуск отрисовки при помощи ручки")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Запуск отрисовки при помощи карандаша")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Запуск отрисовки при помощи маркера")

pen = Pen("pen")
pen.draw()
pencil = Pencil("pencil")
pencil.draw()
handle = Handle("handle")
handle.draw()
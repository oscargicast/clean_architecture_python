class Circulo:
    def __init__(self, radio: float):
        self.radio = radio

    def __get_pi(self):
        return 3.1416

    def area(self):
        return self.__get_pi() * self.radio ** 2

if __name__ == '__main__':
    circulo = Circulo(10)
    print(circulo.area())
    # It must fails.
    print(circulo.__get_pi())
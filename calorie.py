from temp import Temperature


class Calorie:

    def __init__(self, weight, height, age, temperature):
        self.temperature = temperature
        self.age = age
        self.height = height
        self.weight = weight

    def calculate(self):
        result = 10 * self.weight + 6.5 * self.height + 5 - self.temperature * 10
        return result


if __name__ == "__main__":
    temerature, l_time = Temperature(country="italy", city="rome").get()
    calorie = Calorie(temperature=temerature, weight=70, height=175, age=32)
    print(calorie.calculate())
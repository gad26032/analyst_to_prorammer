class Mlek:
    def __init__(self, height, name='Noname', age=0):
        self.name = name
        self.age = age
        self.height = height

    def say_name(self):
        print(self.name)


class Aggressive:
    def laugh(self):
        print(self.name.upper())



class Dog(Mlek):
    def __init__(self, height):
        super().__init__(height)
        self.fleas = []

    def wof(self):
        print('Wof')

    def put_flea(self, flea):
        self.fleas.append(flea)


class Mastif(Dog, Aggressive):

    def __init__(self, color, height=23):
        super().__init__(height)
        self.color = color

    def wof(self):
        print('WOFWOF')



class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print('Wof')

    def say_name(self):
        print(self.name)




class Knife:
    def dowload_data(self):
        pass

    def plot_grapf(self):
        pass
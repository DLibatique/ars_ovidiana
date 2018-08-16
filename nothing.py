class Person:

    def __init__(self, name):
        self.name = name

    def learn_info(self):
        print("Hi! I'm " + self.name + "! I'm a visiting lecturer in Classics at the College of the Holy Cross.")
        print("I earned my PhD from BU, and I'm interested in Ovid, Sophocles, gender, narratology, reception, and DH.")

    def see_sites(self):
        print("Go to https://dlibatique.github.io")
        print("Or https://ergaleia.github.io")

d = Person('Daniel')
d.learn_info()

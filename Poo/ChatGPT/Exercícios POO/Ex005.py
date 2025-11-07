class Animal:
    def falar(self):
        return 'Som de animal'

class Cachorro(Animal):
    def falar(self):
        return 'AU AU!!'

dog = Cachorro()
print(dog.falar())

a = Animal()
print(a.falar())


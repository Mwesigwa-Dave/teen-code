class Dog():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def bark(self, tone):
        print(self.name + " is barking " + tone)

dog1 = Dog('Scooby', 2, 'Male')
dog2 = Dog('Sherine', 3, 'Female')
dog3 = Dog('Asterine', 7, 'Female')
dog4 = Dog('Kerine', 5, 'Male')

print('name: ' + dog1.name)
print('age: ', dog1.age, 'yrs')
print('gender: ' + dog1.gender)
dog1.bark('loudly')

print('________________________________')

print('name: ' + dog2.name)
print('age: ', dog2.age, 'yrs')
print('gender: ' + dog2.gender)
dog2.bark('softly')

print('________________________________')

print('name: ' + dog3.name)
print('age: ', dog3.age, 'yrs')
print('gender: ' + dog3.gender)
dog3.bark('loudly')

class Dog:
    "Друг человека"
    species = "canis"
    legs = 4
    name = "Бобик"
    age = 2
bulldog = Dog()
chihuahua = Dog()
bulldog.species = "vulpes"
chihuahua.legs = 5
print(bulldog.species)
print(chihuahua.legs)
print(bulldog.__dict__)
print(chihuahua.__dict__)
print(Dog.__doc__)
del Dog.name
print(Dog.name)

class User:
    role = "guest"
    active = True
setattr(User, 'role', 'admin')
setattr(User, "email", "ttt@mail.ru")
print(User.role)
print(getattr(User, 'active'))
print(User.email)
delattr(User, "role")
print(User.__dict__)

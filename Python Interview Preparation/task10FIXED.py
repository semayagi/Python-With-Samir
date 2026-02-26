import copy

class User:
  users = {}
#   def __init__(self, name, age=0, tags=[]): # Изменяемое по умолчанию
#     self.name = name
#     self.age = age
#     self.tags = copy.deepcopy(tags) # 0.5 баллов
#     # 1. Долго
#     # 2. Вдруг пользователь хочет работать снаружи? - мы никогда не должны диктовать пользователю

  def __init__(self, name, age=0, tags: list[int] | None = None):
    self.name = name
    self.age = age
    self.tags = tags or [] # Норм. Если tags 1 - сразу записывается (предусловие работает - дальше не идём)
    # tags and [] - не подойдёт (предусловие не работает - дальше не идём)

  def add_tag(self, tag):
    self.tags.append(tag)


  @classmethod
  def create(cls, name, age):
    if name in cls.users:
      raise ValueError("User already exists")
    user = cls(name, age) # хотим объект класса, а не юзера
    # фабрика создаёт объекты класса
    cls.users[name] = user
    return user


#   @staticmethod
#   def get(name):
#     return User.users[name] # А что, если будет наследование?

  @classmethod
  def get(cls, name):
    return cls.users[name]

  def __str__(self):
    return "User: " + self.name + " (" + str(self.age) + ")" # self.name 

u1 = User.create("Alex", 20) 
u1.add_tag("admin")
u2 = User.create("Alex", 30) # добавить create
print(User.get("Alex")) # выведется 20 летний, ведь только create складирует
print(u2)

"""
Идейно методы отличаются от функций лишь одним - принимают как первый аргумент ссылку на объект/класс

"""
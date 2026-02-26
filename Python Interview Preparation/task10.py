
class User:
  users = {}
  def __init__(self, name, age=0, tags=[]):
    self.name = name
    self.age = age
    self.tags = tags


  def add_tag(self, tag):
    self.tags.append(tag)


  @classmethod
  def create(cls, name, age):
    if name in cls.users:
      raise ValueError("User already exists")
    user = User(name, age)
    cls.users[name] = user
    return user


  @staticmethod
  def get(name):
    return User.users[name]
  def __str__(self):
    return "User: " + name + " (" + str(self.age) + ")"

u1 = User.create("Alex", 20)
u1.add_tag("admin")
u2 = User("Alex", 30)
print(User.get("Alex"))
print(u2)

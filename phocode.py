# # link https://phocode.com/python/python-huong-doi-tuong-trong-python/
#
#
# # exam 1
# import sys
#
#
# def hello():
#     pass
#
#
# print(type(1))  # int
# print(type(''))  # str
# print(type(""))  # str
# print(type([]))  # list
# print(type(()))  # tuple
# print(type({}))  # dictionary
# print(type(object))  # type
# print(type(hello))  # function
# print(type(sys))  # module
# print('----------')
#
#
# # exam 2
# class first:
#     pass
#
#
# fr = first()
# print(type(fr))
# print(type(first))
# print('----------')
#
#
# # exam 3
# class cat:
#     def __init__(self, name):
#         self.name = name
#
#
# bito = cat('bito')
# sut = cat('sut')
# print(bito.name)
# print(sut.name)
# print('----------')
#
#
# class dynamic:
#     pass
#
#
# d = dynamic()
# d.name = '123'
# print(d.name)
# print('----------')
#
#
# class dog:
#     species = 'mammal'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# ki = dog('ki', 8)
# bia = dog('bia', 0.5)
#
# print(ki.name, ki.age)
# print(bia.name, bia.age)
# print(dog.species)
# print(bia.__class__.species)
# print(ki.species)
# print('----------')
#
#
# # exam 3 encapsulation
# class circle:
#     pi = 3.14
#
#     def __init__(self, radius=1):
#         self.radius = radius
#
#     def area(self):
#         return self.radius * self.radius * circle.pi
#
#     def setradius(self, radius):
#         self.radius = radius
#
#     def getradius(self):
#         return self.radius
#
#
# c = circle()
# c.setradius(5)
# print(c.getradius())
# print(c.area())
# print('----------')
#
#
# # exam 4 inheritance
# class animal:
#     def __init__(self):
#         print('animal created')
#
#     def whoamI(self):
#         print('animal')
#
#     def eat(self):
#         print('eating')
#
#
# class shark(animal):
#     def __init__(self):
#         animal.__init__(self)
#         print('shark created')
#
#     def whoamI(self):
#         print('shark')
#
#     def dangerous(self):
#         print('caution')
#
#
# s = shark()
# s.whoamI()
# s.eat()
# s.dangerous()
# print('----------')
#
#
# # exam 5 Polymorphism
# class a:
#     def __init__(self, name=''):
#         self.name = name
#
#     def talk(self):
#         print('a')
#
#
# class b(a):
#     def talk(self):
#         print('123')
#
#
# class c(a):
#     def talk(self):
#         print('abc')
#
#
# x = a()
# x.talk()
# y = b('bito')
# y.talk()
# z = c('sut')
# z.talk()
# print('----------')
#
#
# # exam 6
# class book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def __str__(self):
#         return "Title: %s , author: %s, pages: %s" % (self.title, self.author, self.pages)
#
#     def __len__(self):
#         return self.pages
#
#     def __del__(self):
#         print('A book is destroyed')
#
#
# abc = book('machine learning', 'andrew ng', 1000)
# print(abc)
# print(len(abc))
# del book
# print('----------')


# exam 7
class vector:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)

    def __add__(self, other):
        data = []
        for j in range(len(self.data)):
            data.append(self.data[j] + other.data[j])
        return vector(data)

    def __sub__(self, other):
        data = []
        for j in range(len(self.data)):
            data.append(self.data[j] - other.data[j])
        return vector(data)


x = vector([1, 2, 3])
y = vector([11, 12, 13])
print(x + y)
print(x - y)


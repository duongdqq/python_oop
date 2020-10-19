# link https://o7planning.org/vi/11415/lop-va-doi-tuong-trong-python


# example 1
class rectangle:
    """this is retangle class"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getwidth(self):
        return self.width

    def getheight(self):
        return self.height

    def getarea(self):
        return self.width * self.height


r1 = rectangle(10, 20)
r2 = rectangle(100, 50)

print(r1.width)
print(r1.height)
print(r1.getwidth())
print(r1.getheight())
print(r1.getarea())
print('---------')
print(r2.width)
print(r2.height)
print(r2.getwidth())
print(r2.getheight())
print(r2.getarea())


# example 2
class person:
    def __init__(self, name, age=1, gender='male'):
        self.name = name
        self.age = age
        self.gender = gender

    def showinfor(self):
        print(self.name)
        print(self.age)
        print(self.gender)


print('----------')
duong = person('duong', 23, 'male')
duong.showinfor()
print('----------')
thao = person('thao')
thao.showinfor()
print('----------')
bito = person('bito', 3)
bito.showinfor()

# example 3
r1 = rectangle(20, 10)
r2 = rectangle(30, 100)
r3 = r1

test1 = r1 == r2
test2 = r1 == r3

print(test1)
print(test2)


# example 4
class player:
    minage = 10
    maxage = 50

    def __init__(self, name, age):
        self.name = name
        self.age = age


player1 = player('bito', 3)
player2 = player('bia', 1)
print(player1.name)
print(player1.age)
print(player2.name)
print(player2.age)
print('----------')
player1.age = 100
print(player1.name)
print(player1.age)
print('----------')
player1.address = 'sai dong'
print(player1.address)
# print(player2.address)  # error

# example 5
player1 = player('tom', 23)
print(getattr(player1, 'name'))
print(getattr(player1, 'age'))

setattr(player1, 'age', 10000)
print(player1.age)

has_address = hasattr(player1, 'address')
print(has_address)

setattr(player1, 'address', 'usa')
print(player1.address)

delattr(player1, 'age')


# print(player1.age)


# example 6
class customer:
    'this is computer class'

    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone


john = customer('john', 123456, 'USA')
print(john.__dict__)
print(john.__doc__)
print(john.__class__)
print(john.__class__.__name__)
print(john.__module__)


# example 7
class player:
    minage = 1
    maxage = 100

    def __init__(self, name, age):
        self.name = name
        self.age = age


print('---------')
player1 = player('bito', 3)
player2 = player('bia', 10)

print(player.minage)
print(player1.minage)
print(player2.minage)

player.minage = 99
print(player.minage)
print(player1.minage)
print(player2.minage)

player1.minage = 10000
print(player.minage)
print(player1.minage)
print(player2.minage)

# example 8
print(dir(player))

print('\n\n')

player1 = player('tom', 23)
player1.address = 'usa'

print(dir(player1))

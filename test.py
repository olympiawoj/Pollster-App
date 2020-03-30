# # a = 3
# # b = "123"

# # print(a*b)
# # print(type(a*b))


# list_1 = [1, 2, 4]
# list_2 = [1, 3, 5]

# #combined should be 1,2,4,3,5], not [1,2,4,1,3,5].
# #Set, a term in mathematics for a sequence consisting of distinct language is also extended in its language by Python and can easily made using set().

# list_1.extend(list_2)
# combined = set(list_1)

# #an object
# print('combined', combined)

# list_1.extend(list_2)
# combined1 = list(set(list_1))
# #an araray 
# print('combined1', combined1)



# class Parent(object):
#    def fun(self):
#       print('hi')

# p = Parent()
# p.fun()

# class Child(Parent):
#   def fun(self):
#     print('Bye')

# c = Child()
# c.fun()


def insertionSortRecursive(arr,n):
    # Comment A
    if n <= 0:
        return
    insertionSortRecursive(arr,n-1)
    last = arr[n-1]
    j = n-2
    while (j>=0 and arr[j]>last):
        arr[j+1] = arr[j]
        j = j-1
    arr[j+1]=last
    return arr


print(insertionSortRecursive([5, 4, 3, 2, 1], 5))


#O(n)- iterate one through list to find smallest element
#reeat until finds the smallest elemnt

class Person:
    name = ""
    age = 0

    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

    def __repr__(self):
        return {'name':self.name, 'age':self.age}

    def __str__(self):
        return 'Person(name='+self.name+', age='+str(self.age)+ ')'

class Girl:
    def __str__(self):
        return f'{super().__str__()},  in. tall'

p = Person("Olympia", 17)
print(p)

g = Girl()
print(g)

class Animal:
    def __init__(self, age, gender):
        self.age = age
        self.gender = gender


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.
# super() -  allows you to call methods of the superclass in your subclass. The primary use case of this is to extend the functionality of the inherited method.

# YOUR CODE HERE
class Llama(Animal):
    def __init__(self, age, gender, height, is_domesticated):
        super().__init__(age, gender)
        self.height = height
        self.is_domesticated=is_domesticated

    def __str__(self):
        return f'{super().__str__()}, {self.height} in. tall'


animal = Animal(15, "Male")
l = Llama(15, "Male", 20, True)
print(l)
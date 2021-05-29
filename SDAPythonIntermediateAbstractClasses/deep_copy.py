from figure import Rectangle
from copy import deepcopy

p1 = Rectangle(3, 4)
print("a value is ", p1.a)
print("b value is ", p1.b)

p2 = p1

lst = [1, p1, 3]
shallow_copy_lst = list(lst)
deep_copy_lst = deepcopy(lst)

lst[1].a = 5

print("lst is          ", lst)
print("shallow copy is ", shallow_copy_lst)
print("deep copy is    ", deep_copy_lst)
print("a value is ", p1.a)
print("b value is ", p1.b)
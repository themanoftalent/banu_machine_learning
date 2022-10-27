# create an iterator object from that iterable
try:
    mytuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
    myit = iter(mytuple)
    for i in myit:
        print(i)
except StopIteration:
    print(next(myit))

except:
    print("An exception occurred")

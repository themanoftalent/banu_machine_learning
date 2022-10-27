# Iterating Through an Iterator
# We use the next() function to manually iterate through all the items of an iterator.
# When we reach the end and there is no more data to be returned, it will raise the StopIteration Exception.
# Following is an example.


# define a list
my_list = [6, 9, 0, 3, 12, 15, 18]  # 4 elements

# get an iterator using iter()
my_iter = iter(my_list)

# iterate through it using next()
print(next(my_iter))  # Output: 6
print(next(my_iter))  # Output: 9

# next(obj) is same as obj.__next__()
print(my_iter.__next__())  # Output: 0
print(my_iter.__next__())  # Output: 3
print(my_iter.__next__())  # Output: 12
print(my_iter.__next__())  # Output: 15
print(my_iter.__next__())  # Output: 18

# # This will raise error, no items left
# next(my_iter)


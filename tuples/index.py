# create a tuple using ()
# number tuple
number_tuple = (10, 20, 25.75)
print(number_tuple)
"""
(10, 20, 25.75)
"""

# string tuple
string_tuple = ('Jessa', 'Emma', 'Kelly')
print(string_tuple)
"""
('Jessa', 'Emma', 'Kelly')
"""

# mixed type tuple
sample_tuple = ('Jessa', 30, 45.75, [25, 78])
print(sample_tuple)

"""
('Jessa', 30, 45.75, [25, 78])
"""

# create a tuple using tuple() constructor
sample_tuple2 = tuple(('Jessa', 30, 45.75, [23, 78]))
print(sample_tuple2)

# packing variables into tuple
tuple1 = 1, 2, "Hello"
# display tuple
print(tuple1)
print(type(tuple1))

# unpacking tuple into variable
i, j, k = tuple1
# printing the variables
print(i, j, k)

"""
(1, 2, 'Hello')
<class 'tuple'>
1 2 Hello

"""
# x, y, z, w, v are all tuples
# tuples are immutable

x = 5,4,3 # no brackets imply tuple
print(x)

y = (8,9,10) # regular parenthesis imply tuple too
print(y)

z = "hello","world","sup"
print(z)

w = True, False, True
print(w)

v = ("the", "quick", True, 92.2)
print(v[2]) # indexed like array

# +--------------+---------------------------+-----------------+-------------------+
# | Collection   | Ordered                   | Changeable      | Allows Duplicates |
# +--------------+---------------------------+-----------------+-------------------+
# | List         | ✓                         | ✓               | ✓                |
# +--------------+---------------------------+-----------------+-------------------+
# | Tuple        | ✓                         | ✗               | ✓                |
# +--------------+---------------------------+-----------------+-------------------+
# | Set          | ✗                         | ✗*              | ✗                |
# +--------------+---------------------------+-----------------+-------------------+
# | Dictionary   | ✓**                       | ✓               | ✗                |
# +--------------+---------------------------+-----------------+-------------------+

# * Sets are unchangeable, but you can add or remove items.
# ** Dictionaries are ordered as of Python 3.7 (insertion order is preserved).

a = [5,4,3] # square brackets imply list


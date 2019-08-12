a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = (3, 4, 1, 2, 7, 6, 5, 8, 9)
c = {5, 6, 7, 8, 1, 2, 3, 4, 9}

sorted(a)
print(sorted(a))

sorted(b)
print(sorted(b))

sorted(c)
print(sorted(c))

def compare():
    if sorted(a) == sorted(b) == sorted(c):
        return True
    else:
        return False

ff = compare()
print(ff)
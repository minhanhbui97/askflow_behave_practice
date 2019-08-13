a = [1, 2, 3, 4, 5, 6, 7, 8]
b = (3, 4, 1, 2, 7, 6, 5, 8)
c = {5, 6, 7, 8, 1, 2, 3, 4}

# convert set into an ordered list
converted_c = list(c)

# sorted tuple b returns an ordered list without
sorted_b = sorted(b)


def compare_sets():
    if len(a) == len(b) == len(c):
        count = 0
        for i in range(len(a)):
            if a[i] == sorted_b[i] == converted_c[i]:
                count += 1
        if count == len(a):
            return True
        else:
            return False
    else:
        return False


print(a)
print(sorted_b)
print(converted_c)

f = compare_sets()
print(f)

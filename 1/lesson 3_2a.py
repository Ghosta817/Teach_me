def update_dictionary(d, key, value):
    if key in d:
        d[key] +=[value]
    elif (2 * key) in d:
        d[2 * key] += [value]
    else:
        d[2 * key] = [value]

d = {}
print(update_dictionary(d, 0, -5))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 1, -1)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 2, -2)
print(d)
update_dictionary(d, 3, -3)
print(d)

d = {}
kol = {'a': 300, 'b': 225, 'c': 75, 'd': 200, 'e': 150, 'f': 50}
for key, value in {'a': [5, 1, 3], 'b': [3, 1, 1], 'c': [1, 1, 0], 'd': [4, 0, 1], 'e': [4, 0, 0],
                   'f': [2, 0, 0]}.items():
    a = value[0]
    b = value[1]
    c = value[2]
    d[key] = ((4 - a) ** 2 + (1 - b) ** 2 + (0 - c) ** 2) ** 0.5
while len(d) != 4:
    key = ''
    minim = 0
    for k, v in d.items():
        if minim < v:
            minim = v
            key = k
    del d[key]
    minim = 0
rez = 0
for key in d.keys():
    rez += kol[key]
rez_fin = rez / 4
print(rez_fin)

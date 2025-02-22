cubes = [1, 8, 27, 65, 125]
cubes[3] = 64

print(cubes)
cubes.append(216)
cubes.append(8 ** 3)
print(cubes)

rgb = ["red", "green", "blue"]
rgba = rgb
rgba.append("alpha")
print(rgb)
letters = ['a', 'd', 'c', 'r', 'b', 'x', 'y', 'k', 'l', 'm']

letters.append('n')
letters[2:3]= ['vf', 'v']
len(letters)
print(letters)

a, b = 0, 1
while a<10:
    print(a)
    a, b = b, a+b
    



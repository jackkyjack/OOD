inp = input("Enter a list of points: ").split('/')
points = inp[0].split(',')
p = []
for point in points:
    x, y = map(float, point.split())
    p.append([x, y])

startp = [float(inp[1].split()[0]), float(inp[1].split()[1])]
if startp in p:
    p.remove(startp)
    p.sort()
else:
    print(f"{startp} is not in {p}")
    exit()

output = 0
while p:
    nearest_point = None
    for i in p:
        distance = ((((i[0]-startp[0])**2)+((i[1]-startp[1])**2))**0.5)
        if nearest_point is None or distance < output:
            nearest_point = i
            output = distance
    if nearest_point is not None:
        print(f"{startp} -> {nearest_point} | The distance is {output:.4f}")
        p.remove(nearest_point)
        startp = nearest_point
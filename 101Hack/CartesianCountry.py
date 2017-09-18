x1, y1 = map(int, raw_input().split())
x2, y2 = map(int, raw_input().split())
xc, yc = map(int, raw_input().split())

xdist = 2 * min(abs(x1 - xc), abs(x2 - xc)) + 1
ydist = 2 * min(abs(y1 - yc), abs(y2 - yc)) + 1

# print xdist,ydist
print (xdist * ydist - 1) / 2

file = open('p102_triangles.txt', 'r')
points = file.readlines()
num = 0
for line in points:
    coeffs = line.split(',')
    x1 = float(coeffs[0]); x2 = float(coeffs[2]); x3 = float(coeffs[4]);
    y1 = float(coeffs[1]); y2 = float(coeffs[3]); y3 = float(coeffs[5]);
    det = (x3 - x1) * (y3 - y2) - (x3 - x2) * (y3 - y1)
    a1 = ((y3 - y2) * x3 + (x2 - x3) * y3) / det
    a2 = ((y1 - y3) * x3 + (x3 - x1) * y3) /det
    if (a1 >= 0 and a2 >= 0 and a1 + a2 <= 1):
        num = num + 1
print(num)

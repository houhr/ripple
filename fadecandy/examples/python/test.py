# 0   1   2   3   4   5   6   7
# 8   9   10  11  12  13  14  15
# 16  17  18  19  20  21  22  23
# 24  25  26  27  28  29  30  31
# 32  33  34  35  36  37  38  39
# 40  41  42  43  44  45  46  47
# 48  49  50  51  52  53  54  55
# 56  57  58  59  60  61  62  63

import opc, time, random

numLEDs = 64
client = opc.Client('localhost:7890')
n = [26, 27, 28, 34, 36, 42, 44, 45]
v = [18, 20, 26, 28, 35]
conj = [19, 20, 27, 28, 33, 34, 35, 36, 37, 38]
pixels = [ (0,0,0) ] * numLEDs
centralDot = [19, 20, 26, 27, 28, 29, 34, 35, 36, 37, 43, 44]
o0 = [27, 28, 35, 36]
o1 = [18, 19, 20, 21, 26, 29, 34, 37, 42, 43, 44, 45]
o2 = [9, 10, 11, 12, 13, 14, 17, 22, 25, 30, 33, 38, 41, 46, 49, 50, 51, 52, 53, 54]
o3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 15, 16, 23, 24, 31, 32, 39, 40, 47, 48, 55, 56, 57, 58, 59, 60, 61, 62, 63]

t0 = [27, 28, 36]
t1 = [18, 19, 20, 21, 27, 29, 36, 37, 45]
t2 = [9, 10, 11, 12, 13, 14, 18, 22, 27, 30, 36, 38, 45, 46, 54]
t3 = [0, 1, 2, 3, 4, 5, 6, 7, 9, 15, 18, 23, 27, 31, 36, 39, 45, 47, 54, 55, 63]

x0 = [27, 28, 35, 36]
x1 = [18, 21, 27, 28, 35, 36, 42, 45]
x2 = [9, 14, 18, 21, 27, 28, 35, 36, 42, 45, 49, 54]
x3 = [0, 7, 9, 14, 18, 21, 27, 28, 35, 36, 42, 45, 49, 54, 56, 63]

h0 = [27, 28, 35, 36]
h1 = [26, 27, 28, 29, 34, 35, 36, 37]
h2 = [25, 26, 27, 28, 29, 30, 33, 34, 35, 36, 37, 38]
h3 = [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]

p0 = []


common = []

class Dot:

    def __init__(self, l, c):
        self.location = l
        self.color = c

    def dimInAndOut(self):
        # Turn off this LED
        pixels[self.location] = (0, 0, 0)
        client.put_pixels(pixels)

        for num in range(1, 11):
            pixels[self.location] = (int(self.color[0] / 10 * num), int(self.color[1] / 10 * num), int(self.color[2] / 10 * num))
            time.sleep(0.01)
            client.put_pixels(pixels)

        # Stay for 0.5 sencond
        time.sleep(0.5)

        for num in range(1, 11):
            pixels[self.location] = (int(self.color[0] / 10 * (11 - num)), int(self.color[1] / 10 * (11 - num)), int(self.color[2] / 10 * (11 - num)))
            time.sleep(0.01)
            client.put_pixels(pixels)

        # Turn off this LED
        pixels[self.location] = (0, 0, 0)
        client.put_pixels(pixels)

def turnOffAll():
    for i in range(numLEDs):
        pixels[i] = (0, 0, 0)
        client.put_pixels(pixels)

def dimInAndOut(i, c):
    turnOffAll()
    for num in range(1, 11):
        pixels[i] = (int(c[0] / 10 * num), int(c[1] / 10 * num), int(c[2] / 10 * num))
        time.sleep(0.1)
        client.put_pixels(pixels)
    time.sleep(0.5)
    for num in range(1, 11):
        pixels[i] = (int(c[0] / 10 * (11 - num)), int(c[1] / 10 * (11 - num)), int(c[2] / 10 * (11 - num)))
        time.sleep(0.1)
        client.put_pixels(pixels)

def dimIn(i, c):
    for num in range(1, 11):
        pixels[i] = (int(c[0] / 10 * num), int(c[1] / 10 * num), int(c[2] / 10 * num))
        client.put_pixels(pixels)
        time.sleep(0.1)


def showCentralDot(a, c):
    turnOffAll()
    for num in range(1, 11):
        for i in a:
            pixels[i] = (int(c[0] / 10 * num), int(c[1] / 10 * num), int(c[2] / 10 * num))
        client.put_pixels(pixels)
        time.sleep(0.02)

while(True):
    # for num in range(0, 5):
    #     i = int(random.randrange(0, numLEDs))
    #     dot = Dot(i, (i*i%255, i*i*i%255, i*i*i*i%255))
    #     dot.dimInAndOut()

    showCentralDot(h0, (171, 92, 37))
    showCentralDot(h1, (171, 92, 37))
    showCentralDot(h2, (171, 92, 37))
    showCentralDot(h3, (171, 92, 37))
    showCentralDot(h2, (171, 92, 37))
    showCentralDot(h1, (171, 92, 37))
    showCentralDot(h0, (171, 92, 37))

    showCentralDot(x0, (72, 210, 155))
    showCentralDot(x1, (72, 210, 155))
    showCentralDot(x2, (72, 210, 155))
    showCentralDot(x3, (72, 210, 155))
    showCentralDot(x2, (72, 210, 155))
    showCentralDot(x1, (72, 210, 155))
    showCentralDot(x0, (72, 210, 155))

    showCentralDot(t0, (172, 16, 55))
    showCentralDot(t1, (172, 16, 55))
    showCentralDot(t2, (172, 16, 55))
    showCentralDot(t3, (172, 16, 55))
    showCentralDot(t2, (172, 16, 55))
    showCentralDot(t1, (172, 16, 55))
    showCentralDot(t0, (172, 16, 55))

    showCentralDot(o0, (72, 116, 255))
    showCentralDot(o1, (72, 116, 255))
    showCentralDot(o2, (72, 116, 255))
    showCentralDot(o3, (72, 116, 255))
    showCentralDot(o2, (72, 116, 255))
    showCentralDot(o1, (72, 116, 255))
    showCentralDot(o0, (72, 116, 255))

    turnOffAll()

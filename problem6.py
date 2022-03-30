import math
def spherVolume(radius):
    v = (4.0 / 3.0) * math.pi * radius * radius * radius
    s = 4.0 * math.pi * radius * radius
    return ("부피값,겉면적값",v,s);

radius = float(input('구의 반지름을 입력하세요: '))
print(spherVolume(radius))
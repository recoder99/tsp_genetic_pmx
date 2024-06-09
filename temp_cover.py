import numpy as np
import math
import matplotlib.pyplot as plt

###########################################################################

def temp(temp: int):
    f = temp_freezing(temp)
    c = temp_cool(temp)
    w = temp_warm(temp)
    h = temp_hot(temp)

    return f, c, w, h

def temp_freezing(temp: int):
    if 0 <= temp <= 30:
        return 1
    elif 30 < temp <= 50:
        return -0.05 * temp + 2.5
    elif 50 < temp <= 110:
        return 0
    else:
        return -1

def temp_cool(temp: int):
    if 0 <= temp <= 30:
        return 0
    elif 30 < temp <= 50:
        return 0.05 * temp - 1.5
    elif 50 < temp <= 70:
        return -0.05 * temp + 3.5
    elif 70 < temp <= 110:
        return 0
    else:
        return -1

def temp_warm(temp: int):
    if 0 <= temp <= 50:
        return 0
    elif 50 < temp <= 70:
        return 0.05 * temp - 2.5
    elif 70 < temp <= 90:
        return -0.05 * temp + 4.5
    elif 90 < temp <= 110:
        return 0
    else:
        return -1

def temp_hot(temp: int):
    if 0 <= temp <= 70:
        return 0
    elif 70 < temp <= 90:
        return 0.05 * temp - 3.5
    elif 90 < temp <= 110:
        return 1
    else:
        return -1

###########################################################################

def cover(cloud_cover: int):
    s = cover_sunny(cloud_cover)
    p = cover_partlycloudy(cloud_cover)
    o = cover_overcast(cloud_cover)

    return s, p, o

def cover_sunny(cloud: int):
    if 0 <= cloud <= 20:
        return 1
    elif 20 < cloud <= 40:
        return -0.05 * cloud + 2
    elif 40 < cloud <= 100:
        return 0
    else:
        return -1

def cover_partlycloudy(cloud: int):
    if 0 <= cloud <= 20:
        return 0
    elif 20 < cloud <= 50:
        return 0.03 * cloud - 0.67
    elif 50 < cloud <= 80:
        return -0.03 * cloud + 2.67
    elif 80 < cloud <= 100:
        return 0
    else:
        return -1

def cover_overcast(cloud: int):
    if 0 <= cloud <= 60:
        return 0
    if 60 < cloud <= 80:
        return 0.05 * cloud - 3
    elif 80 <= cloud:
        return 1
    else:
        return -1

###########################################################################
    
def getSpeed(fast, slow):
    f = fast
    s = slow

    fY = ((f - -0.5) / 0.02)
    sY = ((s - -0.5) / 0.02)

    fY = math.ceil(fY)
    sY = math.ceil(sY)

    y = np.zeros(101)

    print(y)

    y[:math.ceil(sY)] = s
    y[math.ceil(fY):] = f

    steps = fY - sY
    delta_y = f - s
    step_size = delta_y / steps

    for i in range(sY, fY):
        y[i] = s + (i - sY) * step_size

    sumY = 0.00
    sumXY = 0.00

    x_values = []
    y_values = []

    for i in range(101):
        x_values.append(i)
        y_values.append(y[i])
        sumXY = sumXY + (i * y[i])
        sumY = sumY + y[i]

    plt.plot(x_values, y_values)
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.title('Y values over X')
    plt.show()

    return sumXY / sumY

###########################################################################

if __name__ == '__main__':
    t = int(input())
    c = int(input())

    tR = temp(t)
    cR = cover(c)

    print(f'Temperature-------------------\nFreezing: {tR[0]} || Cool: {tR[1]} || Warm: {tR[2]} || Hot: {tR[3]}')
    print(f'Cloud Cover-------------------\nSunny: {cR[0]} || Partly Cloudy: {cR[1]} || Overcast: {cR[2]}')

    fast = min(tR[2], cR[0])
    slow = min(tR[1], cR[1])

    speed = getSpeed(fast, slow)

    print("Output-------------------")
    print("Fast: ", fast)
    print("Slow: ", slow) 
    print("Speed: ", speed)

###########################################################################

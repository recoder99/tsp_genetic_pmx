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

if __name__ == '__main__':
    w = temp(62)
    c = cover(47)
    print(f'Temperature: {w} \nCloud Cover: {c}')
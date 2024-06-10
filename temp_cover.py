##########################################################################

def calcFreezing(temp):
    if 0 >= temp < 30:
        return 1
    elif 30 <= temp < 50:
        return -0.05 * temp + 2.5
    elif 50 <= temp < 70:
        return 0
    elif 70 <= temp < 90:
        return 0
    else:
        return 0
    
def calcCool(temp):
    if 0 >= temp < 30:
        return 0
    elif 30 <= temp < 50:
        return 0.05 * temp - 1.5
    elif 50 <= temp < 70:
        return -0.05 * temp + 3.5
    elif 70 <= temp < 90:
        return 0
    else:
        return 0
    
def calcWarm(temp):
    if 0 >= temp < 30:
        return 0
    elif 30 <= temp < 50:
        return 0
    elif 50 <= temp < 70:
        return 0.05 * temp - 2.5
    elif 70 <= temp < 90:
        return -0.05 * temp + 4.5
    else:
        return 0
    
def calcHot(temp):
    if 0 >= temp < 30:
        return 0
    elif 30 <= temp < 50:
        return 0
    elif 50 <= temp < 70:
        return 0
    elif 70 <= temp < 90:
        return 0.05 * temp - 3.5
    else:
        return 1
    
def determineTemp(temp):
    freezing = calcFreezing(temp)
    cool = calcCool(temp)
    warm = calcWarm(temp)
    hot = calcHot(temp)

    return freezing, cool, warm, hot

##########################################################################

def calcSunny(clouds):
    if 0 <= clouds < 20:
        return 1
    elif 20 <= clouds < 40:
        return -0.05 * clouds + 2
    else:
        return 0
    
def calcPartlyCloudy(clouds):
    if 0 <= clouds < 20:
        return 0
    elif 20 <= clouds < 40:
        return 0.033333333333333 * clouds - 0.67
    elif 40 <= clouds < 80:
        return -0.033333333333333 * clouds + 2.67
    else:
        return 0
    
def calcOvercast(clouds):
    if 0 <= clouds < 60:
        return 0
    elif 60 <= clouds < 80:
        return 0.05 * clouds - 3
    else:
        return 1
    
def determineCloudCover(clouds):
    sunny = calcSunny(clouds)
    partly_cloudy = calcPartlyCloudy(clouds)
    overcast = calcOvercast(clouds)
    
    return sunny, partly_cloudy, overcast

##########################################################################

def calculateSpeed(fast, slow):
    if slow + fast == 0:
        return 0
    
    speed = ((slow * 25) + (fast * 75)) / (slow + fast)
    return speed

##########################################################################

temperature = int(input("Enter temperature: "))
cover = int(input("Enter cover: "))

f, c, w, h = determineTemp(temperature)
s, p, o = determineCloudCover(cover)

fast = min(s, w)
slow = min(p, c)

speed = calculateSpeed(fast, slow)

print(f"Speed: {speed:.5f}")

##########################################################################
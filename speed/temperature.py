##################################---------- TEMPERATURE ----------##################################

def temp(t):
    f = temp_freezing(t)
    c = temp_cool(t)
    w = temp_warm(t)
    h = temp_hot(t)
    return f, c, w, h

def temp_freezing(t):
    if 0 >= t < 30:
        return 1
    elif 30 <= t < 50:
        return (-0.05 * t + 2.5)
    elif 50 <= t < 70:
        return 0
    elif 70 <= t < 90:
        return 0
    else:
        return 0
    
def temp_cool(t):
    if 0 >= t < 30:
        return 0
    elif 30 <= t < 50:
        return (0.05 * t - 1.5)
    elif 50 <= t < 70:
        return (-0.05 * t + 3.5)
    elif 70 <= t < 90:
        return 0
    else:
        return 0
    
def temp_warm(t):
    if 0 >= t < 30:
        return 0
    elif 30 <= t < 50:
        return 0
    elif 50 <= t < 70:
        return (0.05 * t -2.5)
    elif 70 <= t < 90:
        return (-0.05 * t + 4.5)
    else:
        return 0
    
def temp_hot(t):
    if 0 >= t < 30:
        return 0
    elif 30 <= t < 50:
        return 0
    elif 50 <= t < 70:
        return 0
    elif 70 <= t < 90:
        return (0.05 * t -3.5)
    else:
        return 1
    
##################################---------- TEMPERATURE ----------##################################
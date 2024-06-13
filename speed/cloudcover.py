##################################---------- CLOUD COVER ----------##################################

def cover(c):
    s = cover_sunny(c)
    cl = cover_partly(c)
    o = cover_overcast(c)
    return s, cl, o

def cover_sunny(c):
    if 0 <= c < 20:
        return 1
    elif 20 <= c < 40:
        return (-0.05 * c + 2)
    else:
        return 0
    
def cover_partly(c):
    if 0 <= c < 20:
        return 0
    elif 20 <= c < 40:
        return (0.033333333333333 * c - 0.67)
    elif 40 <= c < 80:
        return (-0.033333333333333 * c + 2.67)
    else:
        return 0
    
def cover_overcast(c):
    if 0 <= c < 60:
        return 0
    elif 60 <= c < 80:
        return (0.05 * c - 3)
    else:
        return 1
    
##################################---------- CLOUD COVER ----------##################################
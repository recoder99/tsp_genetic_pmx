from temperature import temp
from cloudcover import cover
    
def Slow(s):
    if s <= 25:
        return 1
    elif 25 < s < 75:
        return (-0.02 * s + 1.5)
    else:
        return 0

def Fast(s):
    if s <= 25:
        return 0
    elif 25 < s < 75:
        return (0.02 * s - 0.5)
    else:
        return 1

def COG(t, c):
    f, co, w, h = temp(t)
    s, cl, o = cover(c)

    print("\n|| Freezing: ", f, " || Cool: ", co, " || Warm: ", w, "Hot: ", h, " ||")
    print("\n|| Sunny: ", s, " || Partly Cloudy: ", cl, " || Overcast: ", o, " ||")

    fast = min(s, w)
    slow = min(cl, co)

    if slow + fast == 0:
        return 0
    
    speed = ((slow * 25) + (fast * 75)) / (slow + fast)
    return speed

t = int(input("Input temperature: "))
c = int(input("Input cloud cover: "))

speed = COG(t, c)

print(f"\nSpeed: {speed:.2f}")
print(f"Slow: {Slow(speed) * 100:.2f}")
print(f"Fast: {Fast(speed) * 100:.2f}\n")
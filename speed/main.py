import matplotlib.pyplot as plt
from temperature import temp
from cloudcover import cover

def GetSlopeIntercept(y1, y2, fast, slow):
    y_25 = y1
    y_75 = y2

    slope = (y_75 - y_25) / (75 - 25)
    intercept = y_25 - slope * 25

    point_slow = round((slow - intercept) / slope)
    point_fast = round((fast - intercept) / slope)

    point_slow = point_slow + abs((point_slow % 10) - 5)
    point_fast = point_fast + abs((point_fast % 10) - 5)
    return [slope, intercept, point_slow, point_fast]

def Slow(s):
    slope, intercept = GetSlopeIntercept("slow")

    if s <= 25:
        return 1
    elif 25 < s < 75:
        return (slope * s + intercept)
    else:
        return 0

def Fast(s):
    slope, intercept = GetSlopeIntercept("fast")

    if s <= 25:
        return 0
    elif 25 < s < 75:
        return (slope * s - intercept)
    else:
        return 1

def COG(t, c):
    x_val = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
    y_arr = []
    y_sum = 0
    xy_sum = 0

    f, co, w, h = temp(t)
    s, cl, o = cover(c)

    print("\n|| Freezing: ", f, " || Cool: ", co, " || Warm: ", w, "|| Hot: ", h, " ||")
    print("\n|| Sunny: ", s, " || Partly Cloudy: ", cl, " || Overcast: ", o, " ||")

    fast = round(min(s, w), 3)
    slow = round(min(cl, co), 3)

    if slow + fast == 0:
        return 0

    if slow > fast:
        y_25, y_75 = 1, 0
    else:
        y_25, y_75 = 0, 1

    speed_array = GetSlopeIntercept(y_25, y_75, fast, slow)

    for i in x_val:
        if i <= speed_array[2]:
            y_arr.append(slow)
            y_sum += slow
            xy_sum += slow * i
        elif i >= speed_array[3]:
            y_arr.append(fast)
            y_sum += fast
            xy_sum += fast * i
        else:
            y_arr.append(i * speed_array[0] + speed_array[1])
            y_sum += i * speed_array[0] + speed_array[1]
            xy_sum += (i * speed_array[0] + speed_array[1]) * i

    speed = xy_sum / y_sum
    print(f"\nSpeed: {speed:.3f}")

    # Plot the graph
    plt.figure(figsize=(10, 6))
    plt.plot(x_val, y_arr, marker='o', linestyle='-', color='b')
    plt.axvline(x=speed, color='r', linestyle='--', label=f'Speed: {speed:.3f}')
    plt.axhline(y=slow, color='g', linestyle='--', label=f'Slow: {slow}')
    plt.axhline(y=fast, color='y', linestyle='--', label=f'Fast: {fast}')
    plt.title("Fuzzy Logic Speed Control Graph")
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.ylim(0, 1)  
    plt.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])  
    plt.grid(True)
    plt.legend()
    plt.show()

    return speed

t = int(input("Input temperature: "))
c = int(input("Input cloud cover: "))

speed = COG(t, c)
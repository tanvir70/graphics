from matplotlib import pyplot as plt


def dda(x0, x1, y0, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    m = dy / dx
    steps = max(dx, dy)

    alist = []
    blist = []

    for i in range(steps):
        if m < 0:
            x0 = x0 + 1
            y0 = y0 + m
        elif m == 1:
            x0 += 1
            y0 += 1
        elif m > 0:
            x0 += 1 / m
            y0 += 1
        print("x0 = ", round(x0, 1), end=",")
        print("y0 = ", round(y0, 1), end="\n")

        alist.append(x0)
        blist.append(y0)
    plt.plot(alist, blist, linestyle="--", marker="+")
    plt.show()


print("Enter first point: ")
x0 = int(input())
y0 = int(input())
print("Enter last point: ")
x1 = int(input())
y1 = int(input())
dda(x0, x1, y0, y1)
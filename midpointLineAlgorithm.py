
from matplotlib import pyplot as plt

def midPoint(X1, Y1, X2, Y2):
    # calculate dx & dy
    dx = X2 - X1
    dy = Y2 - Y1

    d = dy - (dx / 2)
    x = X1
    y = Y1

    print(x, ",", y, "\n")

    alist = []
    blist = []

    while (x < X2):
        x = x + 1

        if (d < 0):
            d = d + dy

        else:
            d = d + (dy - dx)
            y = y + 1

        print(x, ",", y, "\n")
        alist.append(x)
        blist.append(y)

    plt.plot(alist, blist, linestyle="--", marker="+")
    plt.show()

if __name__ == '__main__':
    X1 = 4
    Y1 = 8
    X2 = 10
    Y2 = 12
    midPoint(X1, Y1, X2, Y2)


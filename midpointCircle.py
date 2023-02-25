import matplotlib.pyplot as plt


def midPointCircleDraw(x_centre, y_centre, r):
    x = r
    y = 0

    # Creating empty lists for storing x and y coordinates
    x_points = []
    y_points = []

    # Adding the first point
    x_points.append(x + x_centre)
    y_points.append(y + y_centre)

    if (r > 0):
        x_points.append(x + x_centre)
        y_points.append(-y + y_centre)
        x_points.append(y + x_centre)
        y_points.append(x + y_centre)
        x_points.append(-y + x_centre)
        y_points.append(x + y_centre)

    P = 1 - r

    while x > y:

        y += 1

        if P <= 0:
            P = P + 2 * y + 1

        else:
            x -= 1
            P = P + 2 * y - 2 * x + 1

        if (x < y):
            break

        # Adding the generated point and its reflection in the other octants after translation to the lists
        x_points.append(x + x_centre)
        y_points.append(y + y_centre)
        x_points.append(-x + x_centre)
        y_points.append(y + y_centre)
        x_points.append(x + x_centre)
        y_points.append(-y + y_centre)
        x_points.append(-x + x_centre)
        y_points.append(-y + y_centre)

        if x != y:
            x_points.append(y + x_centre)
            y_points.append(x + y_centre)
            x_points.append(-y + x_centre)
            y_points.append(x + y_centre)
            x_points.append(y + x_centre)
            y_points.append(-x + y_centre)
            x_points.append(-y + x_centre)
            y_points.append(-x + y_centre)

    # Creating the plot using Matplotlib
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.plot(x_points, y_points, linestyle='none', marker='o')
    plt.show()


# Driver Code
if __name__ == '__main__':
    midPointCircleDraw(0, 0, 3)

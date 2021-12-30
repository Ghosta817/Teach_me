import matplotlib.pyplot as plt

from random_walk import RandomWalk

# новые блуждания строятся до тех пор пока программа остается активной.
while True:
    fig, ax = plt.subplots(figsize=(15, 9))
    # Построение случайного блуждания и нанесение точек на диаграмму.
    rw = RandomWalk(50000)
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=3)

    # Выделение первой и последней точек.
    ax.scatter(0, 0, c='green', edgecolors='none', s=15)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=15)

    # Удаление осей.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

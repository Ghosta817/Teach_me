import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=10)

# Название заголовка диаграммы и меток осей.
plt.title("Square Numbers", fontsize=20)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Назначение размера шрифта делений на осях.
plt.tick_params(axis='both', which='major', labelsize=10)

# Назначение диапазона для каждой оси.
plt.axes([0, 1100, 0, 1100000])

# Вывод на экран
plt.show()

# Запись в файл
# plt.savefig('squares_plot.png', bbox_inches='tight')

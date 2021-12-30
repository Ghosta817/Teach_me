import pygal

from die import Die

# Создание кубика D6.
die_1 = Die()
die_2 = Die(10)

# Моделирование серии бросков с сохранением результатов в списке.
results = []
roll_times = 50000
for _ in range(roll_times):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Анализ результатов.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Визуализация результатов.
hist = pygal.Bar()

hist.title = f"Results of rolling two D6 and D10 dices {roll_times} times."
hist.x_labels = [x for x in range(2, die_1.num_sides + die_2.num_sides + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual.svg')

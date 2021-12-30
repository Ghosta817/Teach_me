import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = (int(row[4]) - 32) * 5 / 9
            low = (int(row[5]) - 32) * 5 / 9
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Нанесение данных на диаграмму.
fig = plt.figure(dpi=128, figsize=(15, 9))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Форматирование диагрммы.
plt.title('Daily high and low temperatures - 2018\nDeath Valley', fontsize=20)
plt.xlabel('', fontsize=10)
fig.autofmt_xdate()
plt.ylabel('Temperature (С)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

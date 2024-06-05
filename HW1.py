import pandas as pd

# Чтение данных из CSV-файла
df = pd.read_csv('weekly_deaths_2010_2024.csv', delimiter=';')

# Вывод первых 5 строк данных
print("Первые 5 строк данных:")
print(df.head())

# Вывод информации о данных
print("\nИнформация о данных:")
print(df.info())

# Вывод статистического описания данных
print("\nСтатистическое описание данных:")
print(df.describe())

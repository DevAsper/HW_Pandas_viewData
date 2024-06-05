import pandas as pd

# Загрузка данных из CSV-файла
df = pd.read_csv('dz.csv')

 # Группировка данных по городу и вычисление средней зарплаты
average_salary_by_city = df.groupby('City')['Salary'].mean()

# Вывод результатов
print("\nСредняя зарплата по городам:")
print(average_salary_by_city)

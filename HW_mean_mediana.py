import pandas as pd
import numpy as np

# Создание DataFrame с данными учеников
data = {
    'Имя': ['Мария', 'Анна', 'Виктор', 'Галина', 'Сергей', 'Дмитрий', 'Ирина', 'Игорь', 'Ксения', 'Раиса'],
    'Математика': [5, 3, 4, 5, 2, 4, 4, 5, 4, 4],
    'Физика': [4, 5, 3, 4, 4, 2, 5, 3, 5, 3],
    'Химия': [3, 4, 5, 2, 3, 4, 5, 4, 3, 5],
    'Биология': [4, 3, 2, 5, 5, 3, 2, 4, 5, 4],
    'Литература': [5, 4, 3, 3, 4, 3, 5, 3, 4, 5]
}
df = pd.DataFrame(data)

# Вывод первых нескольких строк DataFrame
print("Первые несколько строк DataFrame:")
print(df.head())

# Вычисление средней оценки по каждому предмету
mean_scores = df.mean(numeric_only=True)
print("\nСредняя оценка по каждому предмету:")
print(mean_scores)

# Вычисление медианной оценки по каждому предмету
median_scores = df.median(numeric_only=True)
print("\nМедианная оценка по каждому предмету:")
print(median_scores)

# Вычисление Q1 и Q3 для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math
print("\nКвартили и IQR для оценок по математике:")
print(f"Q1 (25-й процентиль): {Q1_math}")
print(f"Q3 (75-й процентиль): {Q3_math}")
print(f"IQR (межквартильный размах): {IQR_math}")

# Вычисление стандартного отклонения
std_deviation = df.std(numeric_only=True)
print("\nСтандартное отклонение по каждому предмету:")
print(std_deviation)

"""
Написать EDA для датасета про пингвинов
Необходимо:
● Использовать 2-3 точечных графика
● Применить доп измерение в точечных графиках, используя
аргументы hue, size, stile
● Использовать PairGrid с типом графика на ваш выбор
● Изобразить Heatmap
● Использовать 2-3 гистограммы

"""

# Seaborn — библиотека для создания
# статистических графиков на Python

# разведочный анализ данных (EDA) по заданному дата сету

import matplotlib.pyplot as plt
import seaborn as sns

penguins = sns.load_dataset("penguins")

# def first():
#     plt.scatter(penguins['bill_length_mm'], penguins['bill_depth_mm'])
#     plt.show()

#     plt.scatter(penguins['flipper_length_mm'], penguins['body_mass_g'])
#     plt.show()
# first()

# ● Применить доп измерение в точечных графиках, используя
# аргументы hue, size, stile
# hue='sex' - разбивка по полу
# size=5 - размер точек
# def second():
#     sns.catplot(data=penguins, x='flipper_length_mm', y='body_mass_g',
#                 hue='sex',
#                 size=5)

#     plt.show()

# second()

# ● Использовать PairGrid с типом графика на ваш выбор
# создадим объект класса PairGrid, в качестве данных передадим ему
# как количественные, так и категориальные переменные

# def third():
#     x_vars = ["body_mass_g", "bill_length_mm", "bill_depth_mm",
#               "flipper_length_mm"]
#     y_vars = ["body_mass_g"]
#     g = sns.PairGrid(penguins, hue="species", x_vars=x_vars, y_vars=y_vars)
#     g.map_diag(sns.histplot, color=".3")
#     g.map_offdiag(sns.scatterplot)
#     g.add_legend()
#     plt.show()

# third()

# ● Изобразить Heatmap
# def fourth():
#     sns.displot(penguins, x="bill_length_mm", y="bill_depth_mm", hue="species")
#     plt.show()
# fourth()

def fifth():
    penguins['bill_depth_mm'].hist(bins=4)
    plt.show()
    
fifth()
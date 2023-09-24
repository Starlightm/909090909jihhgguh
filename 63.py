"""
1. Изобразите отношение households к population с
помощью точечного графика
2. Визуализировать longitude по отношения к
median_house_value, используя линейный график
3. Представить гистограмму по housing_median_age
4. Изобразить гистограмму по median_house_value с
оттенком housing_median_age
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea


data = pd.read_csv('california_housing_test.csv')

# def first():
#     households = data.households
#     population = data.population 
    # plt.scatter(households, population)  #scatter - точечный график
#     plt.xlabel("households")
#     plt.ylabel("population")
#     plt.show()
# first()

# def second():
#     longitude = data.longitude
#     median_house_value = data.median_house_value
#     plt.plot(longitude, median_house_value)# plot -линейный график
#     plt.xlabel("longitude")
#     plt.ylabel("median_house_value")
#     plt.title("Line plot for longitude and median_house_value")
#     plt.show()
# second()


# Гистограммы агрегируют числовые данные по группам с равными интервалами,
# которые называют бинами, и отображают частоту
# встречаемости значений в каждом из бинов
# second()

# def third():
#     housing_median_age = data.housing_median_age
#     plt.hist(housing_median_age, bins=10) #hist -гистограммa
#     plt.show()
# third()

# Изобразить гистограмму по median_house_value с
# оттенком housing_median_age

# def fourth():

#     median_house_value = data.median_house_value
#     housing_median_age = data.housing_median_age

#     plt.hist(housing_median_age, bins=7, edgecolor='black')

#     plt.hist(median_house_value, bins=7)
#     plt.hist(housing_median_age, bins=7)

#     plt.show()

# fourth()

def fourth():
    sea.histplot(data=data, x="median_house_value", y="housing_median_age")
    plt.show()

fourth()




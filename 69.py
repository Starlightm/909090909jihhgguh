# изобразить гистограмму flipper_lenght_mm c оттенком height_group
from random import randint
import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")

def first():
    sns.histplot(penguins, x="flipper_length_mm", hue="species")
    plt.show()

first()

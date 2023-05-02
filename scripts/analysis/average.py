import pandas as pd
import matplotlib.pyplot as plt


#TODO исправить
def average(param_key, param_number):
    '''
    Функция для построения графика зависимости
    среднего численного параметра от качественного параметра
    '''
    # param_key - качественное значение по типу key, mode
    # param_number - количественное значение по типу liveness, popularity
    df = pd.read_csv("data/SpotifyFeatures.csv")
    keys = set(df[param_key])
    number = []
    key = []
    for item in keys:
        number.append(df.loc[df[param_key] == item, param_number].mean())
        key.append(item)

    plt.figure(figsize=(15, 8))
    plt.bar(key, number)
    plt.xticks(rotation=90)
    plt.xlabel(param_key)
    plt.ylabel(param_number)
    plt.title(f"Avarage {param_number} of {param_key}s")
    plt.show()

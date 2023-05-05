import pandas as pd
import matplotlib.pyplot as plt


def average(param_key, param_number):
    '''
    Функция для построения графика зависимости
    среднего численного параметра от качественного параметра
    Возвращает лист ключей и лист значений
    '''
    # param_key - качественное значение по типу key, mode
    # param_number - количественное значение по типу liveness, popularity

    df_to_graph = df.groupby(param_key, as_index=False)[param_number].mean()

    plt.figure(figsize=(15, 8))
    plt.bar(df_to_graph[param_key], df_to_graph[param_number])
    plt.xticks(rotation=90)
    plt.xlabel(param_key)
    plt.ylabel(param_number)
    plt.title(f"Avarage {param_number} of {param_key}s")
    plt.show()
    return df_to_graph


df = pd.read_csv("data/SpotifyFeatures.csv")
#df2 = df.groupby("artist_name")["popularity"].mean().head(100)
#plt.bar(df2.keys(), df2)
#plt.show()

def genre_evolution(genre):
    df2 = df.loc[df["genre"] == genre]["popularity"]
    y = df2.values.tolist()
    x = [k for k in range(len(y))]
    plt.plot(x, y, 'o', color='r')
    plt.show()




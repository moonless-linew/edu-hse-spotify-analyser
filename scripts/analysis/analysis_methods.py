import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/SpotifyFeatures.csv")


def average(param_key, param_number):
    '''
    Функция для получения зависимости
    среднего численного параметра от качественного параметра
    Возвращает лист ключей и лист значений
    '''
    # param_key - качественное значение по типу key, mode
    # param_number - количественное значение по типу liveness, popularity

    df_to_graph = df.groupby(param_key)[param_number].mean()
    return list(df_to_graph.keys), list(df_to_graph)


def describe_artist(name, param):
    '''
    Функция для описания параметра артиста
    Возвращает словарь
    '''
    return df.loc[df["artist_name"] == name, param].describe().to_dict()


# TODO адаптировать для интерфейса
def corr_matrix():
    '''
    Функция для построения матрицы корреляции
    '''
    df = pd.read_csv("data/SpotifyFeatures.csv")
    f = plt.figure(figsize=(19, 15))
    plt.matshow(df.corr(), fignum=f.number)

    # названия осей
    plt.xticks(range(df.select_dtypes(['number']).shape[1]), 
               df.select_dtypes(['number']).columns, 
               fontsize=14, rotation=45) 
    plt.yticks(range(df.select_dtypes(['number']).shape[1]), 
               df.select_dtypes(['number']).columns,
               fontsize=14)
    
    # шкала корреляции
    cb = plt.colorbar() 
    cb.ax.tick_params(labelsize=14)

    # заголовок
    plt.title('Матрица корреляции', fontsize=16)
    plt.show()


def top_tracks(key, count):
    '''
    Функция для получения топа треков по параметру
    Возвращает лист названия столбцов и лист листов значений
    '''
    df_sorted = df.sort_values([key, "artist_name", "track_name"], ascending=[False, True, True]).head(count)
    df_sorted = df_sorted[["artist_name", "track_name", "genre", key]]
    return list(df_sorted.keys()), df_sorted.values.tolist()
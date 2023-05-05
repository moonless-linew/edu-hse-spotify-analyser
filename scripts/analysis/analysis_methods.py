import pandas as pd
import matplotlib.pyplot as plt


def average(param_key, param_number, df):
    '''
    Функция для получения зависимости
    среднего численного параметра от качественного параметра
    Возвращает лист ключей и лист значений
    '''
    # param_key - качественное значение по типу key, mode
    # param_number - количественное значение по типу liveness, popularity

    df_to_graph = df.groupby(param_key, as_index=False)[param_number].mean()
    return list(df_to_graph[param_key]), list(df_to_graph[param_number])


def describe_artist(name, param, df):
    '''
    Функция для описания параметра артиста
    Возвращает словарь
    '''
    return df.loc[df["artist_name"] == name, param].describe().to_dict()


# TODO адаптировать для интерфейса
def corr_matrix(df):
    '''
    Функция для построения матрицы корреляции
    '''
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


def top_tracks(key, count, df):
    '''
    Функция для получения топа треков по параметру
    Возвращает лист названия столбцов и лист листов значений
    '''
    df_sorted = df.sort_values([key, "artist_name", "track_name"], ascending=[False, True, True]).head(count)
    df_sorted = df_sorted[["artist_name", "track_name", "genre", key]]
    out = []
    b = df_sorted.values.tolist()
    keys = df_sorted.keys()
    for i in range(count):
        d = {}
        for j in range(len(keys)):
            d[keys[j]] = b[i][j]
        out.append(d)
    return out


def artist_popularity(name, df):
    '''
    Функция для получения популярности треков артиста по порядку
    Возвращает лист индексов и лист значений популярности
    '''
    df2 = df.loc[df["artist_name"] == name]["popularity"]
    y = df2.values.tolist()
    x = [k for k in range(len(y))]
    return x, y


def genre_evolution(genre, df):
    df2 = df.loc[df["genre"] == genre]["popularity"]
    y = df2.values.tolist()
    x = [k for k in range(len(y))]
    return x, y

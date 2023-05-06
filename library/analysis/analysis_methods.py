import pandas as pd
import matplotlib.pyplot as plt


def average(param_key, param_number, df, color, title):
    """
    Функция для построения графика зависимости
    среднего численного параметра от качественного параметра
    """
    # param_key - качественное значение по типу key, mode
    # param_number - количественное значение по типу liveness, popularity

    df_to_graph = df.groupby(param_key, as_index=False)[param_number].mean()
    plt.figure(figsize=(15, 8))
    plt.bar(df_to_graph[param_key], df_to_graph[param_number], color=color)
    plt.xlabel(param_key, fontsize=14)
    plt.xticks(rotation=45)
    plt.ylabel(param_number, fontsize=14)
    plt.title(title, fontsize=16)
    plt.show()


# выполнено в ui
def describe_artist(name, param, df):
    """
    Функция для описания параметра артиста.
    Возвращает словарь
    """
    return df.loc[df["artist_name"] == name, param].describe().to_dict()


# выполнено в ui
def corr_matrix(df):
    """
    Функция для построения матрицы корреляций
    """
    f = plt.figure(figsize=(15, 8))
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
    plt.title('Matrix of correlation', fontsize=16)
    plt.show()


# выполнено в ui
def top_tracks(key, count, df, reverse):
    """
    Функция для получения топа треков по параметру.
    Возвращает лист названия столбцов и лист листов значений
    """
    # reverse = True -> по возрастанию
    # reverse = False -> по убыванию
    df_sorted = df.sort_values([key, "artist_name", "track_name"], ascending=[reverse, True, True]).head(count)
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


def artist_param_graph(name, df, param):
    """
    Функция для построения графика
    популярности треков артиста по порядку
    """
    df2 = df.loc[df["artist_name"] == name][param]
    y = df2.values.tolist()
    x = [k for k in range(len(y))]
    plt.figure(figsize=(15, 8))
    plt.plot(x, y, "-o")
    plt.title(f"{param} of {name}", fontsize=16)
    plt.xlabel("Number of track", fontsize=14)
    plt.ylabel(param, fontsize=14)
    plt.show()


def genre_evolution(genre, df, color):
    """
    Функция для построения графика
    популярности треков жанра по порядку
    """
    df2 = df.loc[df["genre"] == genre]["popularity"]
    y = df2.values.tolist()
    x = [k for k in range(len(y))]
    plt.figure(figsize=(15, 8))
    plt.plot(x, y, "o", color=color)
    plt.title(f"Evolution of {genre} genre", fontsize=16)
    plt.xlabel("Number of track", fontsize=14)
    plt.ylabel("Popularity", fontsize=14)
    plt.show()


#TODO доп функционал
def average_artists_popularity(df):
    """
    Функция для получения списка средних популярностей артистов.
    Возвращает словарь: ключ - имя артиста, значение - средняя популярность
    """
    df_to_print = df.groupby("artist_name")["popularity"].mean()
    return df_to_print.to_dict()

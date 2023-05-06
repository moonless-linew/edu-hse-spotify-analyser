import matplotlib.pyplot as plt
import numpy as np


# выполнено в ui
def average(param_key, param_number, df, type, color="r"):
    """
    Функция для построения графика зависимости
    среднего численного параметра от качественного параметра
    """
    # param_key - качественное значение по типу key, mode
    # param_number - количественное значение по типу liveness, popularity

    df_to_graph = df.groupby(param_key, as_index=False)[param_number].mean()
    plt.figure(figsize=(15, 8))
    if type == "plot":
        plt.plot(df_to_graph[param_key], df_to_graph[param_number], color=color)
    elif type == "dot":
        plt.plot(df_to_graph[param_key], df_to_graph[param_number], "o", color=color)
    elif type == "bar":
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


# выполнено в ui
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


# TODO доп функционал
def average_artists_popularity(df):
    """
    Функция для получения списка средних популярностей артистов.
    Возвращает словарь: ключ - имя артиста, значение - средняя популярность
    """
    df_to_print = df.groupby("artist_name")["popularity"].mean()
    return df_to_print.to_dict()


# выполнено в ui
def count_of_tracks(param, bins, df, color="r"):
    """
    Функция для построения графика распределения
    треков по параметру
    """
    plt.figure(figsize=(15, 8))
    plt.hist(df[param], color=color, bins=bins)
    plt.xlabel(param, fontsize=14)
    plt.ylabel("Number of tracks", fontsize=14)
    plt.title(f"Distribution of tracks by {param}", fontsize=16)
    plt.show()


def polar_graph_for_all(df):
    """
    Функция для построения полярного графика
    для 100 самых популярных и для всех треков
    """
    df = df.sort_values("popularity", ascending=False)
    df1 = df[["acousticness", "danceability", "energy", "instrumentalness", "liveness", "speechiness", "valence"]]

    features = df1.mean().tolist()
    features_100 = df1.head(100).mean().tolist()

    labels = list(df1)[:]
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)

    plt.figure(figsize=(9, 9))

    ax = plt.subplot(111, polar=True)
    ax.plot(angles, features_100, '-o', color='blue', label="most popular tracks")
    ax.fill(angles, features_100, alpha=0.25, facecolor='blue')
    ax.set_thetagrids(angles * 180 / np.pi, labels, fontsize=14)

    ax = plt.subplot(111, polar=True)
    ax.plot(angles, features, '-o', color='red', label="all tracks")
    ax.fill(angles, features, alpha=0.25, facecolor='red')

    ax.set_rlabel_position(250)
    plt.title("Mean values", fontsize=16)
    plt.legend(loc="lower left")

    plt.show()


def polar_graph_for_artist(track_id, df):
    """
    Функция для построения полярного графика трека
    """
    d = df.loc[df["track_id"] == track_id]
    df1 = d[["acousticness", "danceability", "energy", "instrumentalness", "liveness", "speechiness", "valence"]]
    print(df1)
    features = df1.mean().tolist()
    labels = list(df1)[:]
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)

    plt.figure(figsize=(9, 9))
    ax = plt.subplot(111, polar=True)
    ax.plot(angles, features, '-o', color='blue')
    ax.fill(angles, features, alpha=0.25, facecolor='blue')
    ax.set_thetagrids(angles * 180 / np.pi, labels, fontsize=14)

    ax.set_rlabel_position(250)
    plt.show()

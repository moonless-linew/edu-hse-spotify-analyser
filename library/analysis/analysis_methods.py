"""
Файл с функциями анализа
"""
import matplotlib.pyplot as plt
import numpy as np


def average(param_key, param_number, data_frame, graph_type, color="r"):
    """
    Функция для построения графика зависимости
    среднего численного параметра от качественного параметра
    """
    # param_key - качественное значение по типу key, mode
    # param_number - количественное значение по типу liveness, popularity

    df_to_graph = data_frame.groupby(param_key, as_index=False)[param_number].mean()
    plt.figure(figsize=(15, 8))
    if graph_type == "plot":
        plt.plot(df_to_graph[param_key], df_to_graph[param_number], color=color)
    elif graph_type == "dot":
        plt.plot(df_to_graph[param_key], df_to_graph[param_number], "o", color=color)
    elif graph_type == "bar":
        plt.bar(df_to_graph[param_key], df_to_graph[param_number], color=color)
    plt.xlabel(param_key, fontsize=14)
    plt.xticks(rotation=45)
    plt.ylabel(param_number, fontsize=14)
    plt.title(f"Average {param_number} of {param_key}", fontsize=16)
    plt.show()


def describe_artist(name, param, data_frame):
    """
    Функция для описания параметра артиста.
    Возвращает словарь
    """
    return data_frame.loc[data_frame["artist_name"] == name, param].describe().to_dict()


def corr_matrix(data_frame):
    """
    Функция для построения матрицы корреляций
    """
    corr = data_frame.corr()
    fig, a_x = plt.subplots(figsize=(11, 9))
    i_m = a_x.imshow(corr, interpolation='nearest')
    fig.colorbar(i_m, orientation='vertical', fraction=0.05)

    plt.xticks(range(data_frame.select_dtypes(['number']).shape[1]),
               data_frame.select_dtypes(['number']).columns,
               fontsize=14, rotation=80)
    plt.yticks(range(data_frame.select_dtypes(['number']).shape[1]),
               data_frame.select_dtypes(['number']).columns,
               fontsize=14)

    for i in range(len(corr.columns)):
        for j in range(len(corr.columns)):
            a_x.text(j, i, round(corr.to_numpy()[i, j], 3),
                     ha="center", va="center", color="black")
    plt.title('Matrix of correlation', fontsize=16)
    plt.show()


# TODO исправить в ui
def top_tracks(data_frame, key, count, year_from=-1, year_to=-1, reverse=False):
    """
    Функция для получения топа треков по параметру.
    Возвращает лист названия столбцов и лист листов значений
    """
    # reverse = True -> по возрастанию
    # reverse = False -> по убыванию
    if year_from != -1 and year_to != -1:
        df1 = data_frame.loc[(data_frame["year"] >= year_from) & (data_frame["year"] <= year_to)]
    else:
        df1 = data_frame
    df_sorted = df1.sort_values([key, "artist_name", "track_name"],
                                ascending=[reverse, True, True]).head(count)
    df_sorted = df_sorted[["artist_name", "track_name", "genre", key]]
    out = []
    sorted_values_list = df_sorted.values.tolist()
    keys = df_sorted.keys()
    for i in range(len(sorted_values_list)):
        dict_of_vals = {}
        for j in range(len(keys)):
            dict_of_vals[keys[j]] = sorted_values_list[i][j]
        out.append(dict_of_vals)
    return out


def artist_evolution(artist, data_frame, param):
    """
    Функция для построения графика
    эволюции параметра артиста
    """
    df_sorted = data_frame.sort_values("release_date", ascending=True)
    df3 = df_sorted.loc[df_sorted["year"] > 0]
    df3 = df3.loc[df_sorted["artist_name"] == artist]
    if df3["release_date"].nunique() > 40:
        df1 = df_sorted.loc[df_sorted["artist_name"] == artist][[param, "year"]]
        df2 = df1.groupby("year", as_index=False)[param].mean()

        plt.figure(figsize=(15, 8))
        plt.plot(df2["year"], df2[param], "-o", color="r")

        plt.xlabel("Year", fontsize=14)
        plt.xticks(rotation=45)
        plt.ylabel(f"Mean {param}", fontsize=14)

        plt.title(f"Evolution of {artist} {param}", fontsize=16)
        plt.show()
    else:
        df1 = df_sorted.loc[df_sorted["artist_name"] == artist][[param, "release_date"]]
        df2 = df1.groupby("release_date", as_index=False)[param].mean()

        plt.figure(figsize=(15, 8))
        plt.plot(df2["release_date"], df2[param], "-o", color="r")

        plt.xlabel("Release date", fontsize=14)
        plt.xticks(rotation=45)
        plt.ylabel(f"Mean {param}", fontsize=14)

        plt.title(f"Evolution of {artist} {param}", fontsize=16)
        plt.show()


def genre_evolution(genre, data_frame):
    """
    Функция для построения графика
    эволюции жанра
    """
    df_sorted = data_frame.sort_values("release_date", ascending=True)
    df1 = df_sorted.loc[df_sorted["genre"] == genre][["popularity", "year"]]
    df3 = df1.loc[df1["year"] > 0]
    df2 = df3.groupby("year", as_index=False)["popularity"].mean()
    plt.figure(figsize=(15, 8))
    plt.plot(df2["year"], df2["popularity"], "-o", color="r")
    plt.xlabel("Year", fontsize=14)
    plt.ylabel("Mean popularity", fontsize=14)
    plt.title(f"Evolution of {genre} genre", fontsize=16)
    plt.show()


def average_artists_popularity(data_frame):
    """
    Функция для получения списка средних популярностей артистов.
    Возвращает словарь: ключ - имя артиста, значение - средняя популярность
    """
    df_to_print = data_frame.groupby("artist_name")["popularity"].mean()
    return df_to_print.to_dict()


def count_of_tracks(param, bins, data_frame, color="r"):
    """
    Функция для построения графика распределения
    треков по параметру
    """
    plt.figure(figsize=(15, 8))
    plt.hist(data_frame[param], color=color, bins=bins)
    plt.xlabel(param, fontsize=14)
    plt.ylabel("Number of tracks", fontsize=14)
    plt.title(f"Distribution of tracks by {param}", fontsize=16)
    plt.show()


def polar_graph_for_all(data_frame):
    """
    Функция для построения полярного графика
    для 100 самых популярных и для всех треков
    """
    data_frame = data_frame.sort_values("popularity", ascending=False)
    df1 = data_frame[
        ["acousticness", "danceability", "energy", "instrumentalness", "liveness", "speechiness",
         "valence"]]

    features = df1.mean().tolist()
    features_100 = df1.head(100).mean().tolist()

    labels = list(df1)[:]
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)

    plt.figure(figsize=(9, 9))

    a_x = plt.subplot(111, polar=True)
    a_x.plot(angles, features_100, '-o', color='blue', label="most popular tracks")
    a_x.fill(angles, features_100, alpha=0.25, facecolor='blue')
    a_x.set_thetagrids(angles * 180 / np.pi, labels, fontsize=14)

    a_x = plt.subplot(111, polar=True)
    a_x.plot(angles, features, '-o', color='red', label="all tracks")
    a_x.fill(angles, features, alpha=0.25, facecolor='red')

    a_x.set_rlabel_position(250)
    plt.title("Mean values", fontsize=16)
    plt.legend(loc="lower left")

    plt.show()


def polar_graph_for_track(track_id, data_frame, track_name):
    """
    Функция для построения полярного графика трека
    """
    df0 = data_frame.loc[data_frame["track_id"] == track_id]
    df1 = df0[
        ["acousticness", "danceability", "energy", "instrumentalness", "liveness", "speechiness",
         "valence"]]
    features = df1.mean().tolist()
    labels = list(df1)[:]
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)

    plt.figure(figsize=(9, 9))
    a_x = plt.subplot(111, polar=True)
    a_x.plot(angles, features, '-o', color='blue')
    a_x.fill(angles, features, alpha=0.25, facecolor='blue')
    a_x.set_thetagrids(angles * 180 / np.pi, labels, fontsize=14)

    plt.title(f"{track_name}", fontsize=16)
    a_x.set_rlabel_position(250)
    plt.show()

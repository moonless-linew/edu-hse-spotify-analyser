import pandas as pd
import matplotlib.pyplot as plt

def top_tracks(key, count):
    '''
    Функция для получения топа треков по параметру
    '''
    df_sorted = df.sort_values([key, "artist_name", "track_name"], ascending=[False, True, True]).head(count)
    return df_sorted[["artist_name", "track_name", "genre", key]]


df = pd.read_csv("data/SpotifyFeatures.csv")

df2 = df.loc[df["artist_name"] == "Ariana Grande"]["popularity"]
y = df2.values.tolist()
x = [k for k in range(len(y))]

plt.plot(x, y, '-o', color='r')
plt.xlabel("Номер трека")
plt.ylabel("Популярность")
plt.title("Популярность треков Ariana Grande")
plt.show()
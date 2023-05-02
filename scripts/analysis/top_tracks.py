import pandas as pd

def most_tracks(key, count):
    '''
    Функция для получения топа треков по параметру
    '''
    df = pd.read_csv("data/SpotifyFeatures.csv")
    df_sorted = df.sort_values([key, "artist_name", "track_name"], ascending=[False, True, True]).head(count)
    return df_sorted[["artist_name", "track_name", "genre", key]]

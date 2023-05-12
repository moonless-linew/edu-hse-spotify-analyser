import time
import numpy as np
import pandas as pd
import requests
from pandas import DataFrame
import requests as rq

token = "Bearer " + "YOUR_TOKEN_HERE"
data = pd.read_csv("SpotifyFeatures.csv")
extendedData = DataFrame(columns=["track_id", "release_date"])
# extendedData = pd.read_csv("result.csv")
chunk_size = 50
count = 0
for i in range(len(extendedData["track_id"]), len(data["track_id"]), chunk_size):
    chunk = list(data["track_id"][i:i + chunk_size])
    track_ids = ",".join(chunk)
    response = requests.get("https://api.spotify.com/v1/tracks", params={"ids": track_ids},
                            headers={"Authorization": token}).json()
    ans = ["null", "null"]
    for track in response["tracks"]:
        ans[0] = track["id"]
        ans[1] = track["album"]["release_date"]
        extendedData.loc[len(extendedData)] = ans
    print(count)
    count = count + 1
    if count == 150:
        count = 0
        extendedData.to_csv("result.csv")
        print(extendedData)
        time.sleep(30)



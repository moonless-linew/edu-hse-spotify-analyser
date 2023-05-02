import os
import pandas as pd

def readData():
    return pd.read_csv(os.path.dirname(__file__).replace("scripts", "data") + "\SpotifyFeatures.csv")


if __name__ == "__main__":
    data = readData()
    print(data.columns.values.tolist())
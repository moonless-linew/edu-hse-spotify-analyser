import pandas as pd
import os
df = pd.read_csv(os.path.dirname(__file__).replace("scripts", "data")
                       + "\SpotifyFeaturesLast.csv")
print(set(df["genre"]))
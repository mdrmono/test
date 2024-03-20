import requests
import pandas as pd
#prueba##


response = requests.get("https://covid-api.com/api/reports").json()
df = pd.DataFrame(response["data"])
df.to_csv("data.csv")
print(df)

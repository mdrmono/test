import requests
import pandas as pd
#jijiji


response = requests.get("https://covid-api.com/api/reports").json()
df = pd.DataFrame(response["data"])
df.to_csv("data_renato.csv")
print(df)

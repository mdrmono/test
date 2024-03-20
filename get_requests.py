import requests
import pandas as pd
#jijiji


response = requests.get("https://covid-api.com/api/reports").json()
df2 = pd.DataFrame(response["data"])
df2.to_csv("data_renato.csv")
print(df2)

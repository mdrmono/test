import requests
import pandas as pd
#jijiji


response = requests.get("https://covid-api.com/api/reports").json()
df1 = pd.DataFrame(response["data"])
df1.to_csv("data_renato.csv")
print(df1)

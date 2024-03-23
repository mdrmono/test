import requests
import pandas as pd
#Prueba Pull request

response = requests.get("https://covid-api.com/api/reports").json()
df2 = pd.DataFrame(response["data"])
df2.to_csv("data_renato123.csv")
print(df2)

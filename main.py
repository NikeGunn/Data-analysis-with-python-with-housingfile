import pandas as pd
from ydata_profiling import ProfileReport

#Reading a report & geting them int dataframe
df = pd.read_csv("housing.csv")

# print(df)

#Generate a report 
profile = ProfileReport(df)

profile.to_file("report2.html")



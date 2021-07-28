import pandas as pd
#read in Data
data=pd.read_csv("Resources/cities.csv")

weather_data = data.set_index("City_ID")

#convert data to html
weather_data.to_html('data.html')
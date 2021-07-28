import pandas as pd
#read in Data
data=pd.read_csv("WebVisualizations/Resources/cities.csv")

weather_data = data.set_index("City")

#convert data to html
weather_data.to_html('raw_data.html')
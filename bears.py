import pandas
from datetime import datetime
data = pandas.read_csv("weather_year.csv")
#print(data)

#print(data["Mean TemperatureF"].head())

data.columns = ["date", "max_temp", "mean_temp", "min_temp", "max_dew",
                "mean_dew", "min_dew", "max_humidity", "mean_humidity",
                "min_humidity", "max_pressure", "mean_pressure",
                "min_pressure", "max_visibilty", "mean_visibility",
                "min_visibility", "max_wind", "mean_wind", "min_wind",
                "precipitation", "cloud_cover", "events", "wind_dir"]



data.date = data.date.apply(lambda d: datetime.datetime.strftime(d, "%m/%d/%y"))
print(data.date.head())

import pandas

data = pandas.read_csv("weather_year.csv")
#print(data)

print(data[["EDT", "Mean TemperatureF"]])

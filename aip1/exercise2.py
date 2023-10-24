cloudcover = float(input("Cloudcover rate:"))
chanceofprecipitation = float(input("Chance of precipitation: "))
temperature = float(input("Temperature: "))

if chanceofprecipitation < 50:
    if cloudcover < 10:
        weather ='Sunny'
    elif cloudcover < 40:
        weather = 'Partly cloudy'
    elif cloudcover < 70:
        weather = 'Mostly cloudy'
    else:
        weather = 'Cloudy'

elif chanceofprecipitation >= 50:
    if temperature >= 0:
        if cloudcover < 40:
            weather = 'Sunshower'
        if cloudcover >= 40:
            weather = 'Rain'
    else:
        weather = 'Snow'

print(("Today's weather is: ") + weather)


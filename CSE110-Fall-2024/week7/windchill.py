air_temp= int(input('air temp: '))
wind_speed_mph = int(input('wind speed: '))
degree = u'\u00B0'
wind_chill_F = 35.74 + (0.6215*air_temp) - (35.75*(wind_speed_mph**.16)) + (0.4275*air_temp*(wind_speed_mph**.16))
print(f'The wind chill is {wind_chill_F:.0f}{degree}F at {air_temp}{degree}F and wind speed of {wind_speed_mph} MPH')
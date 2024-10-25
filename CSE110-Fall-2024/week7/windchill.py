# created by Matthew Rosenthal
# added the calculations in celsius and also add the wind speed in knots and KM/H 
# and figured out how to include the degree symbol

degree = u'\u00B0'

def C_to_F(C):
    F = C * (9/5) + 32
    return F

def F_to_C(F):
    C=(F - 32) / 1.8
    return C

#Wind chill of 0 to -19°F: Frostbite possible in 30 minutes to exposed skin.
#Wind chill of -20 to -39°F: Frostbite possible in 10 to 30 minutes.
#Wind chill of -40 to -59°F: Frostbite possible in 5 to 10 minutes.
#Wind chill of -60°F and below: Frostbite possible in less than 5 minutes.
def frostbite_risk(w):
    if 0 >= w >= -19:
        return 'Frostbite possible in 30 minutes to exposed skin'
    if -20 >= w >= -39:
        return 'Frostbite possible in 10 to 30 minutes.'
    if -40 >= w >=-59:
        return 'Frostbite possible in 5 to 10 minutes'
    if -60 >= w < -60:
        return'Frostbite possible in less than 5 minutes.'


def wind_chill(a , u):
    unit = u
    air_temp = a
    print('')
    if unit == 'C':
            air_temp_C = air_temp
            temp = C_to_F(air_temp)
            air_temp_F = temp
    elif unit == 'F':
            air_temp_F = air_temp
            temp = F_to_C(air_temp)
            air_temp_C = temp
    wind_speed_range = range(0,60,5)
    wind_speed_mph=5
    for wind_speed_mph in wind_speed_range:
        wind_speed_mph += 5
        wind_speed__km_h = wind_speed_mph * 1.60934
        wind_speed_knots = wind_speed_mph * 0.5144
        wind_chill_F = 35.74 + (0.6215*air_temp_F) - (35.75*(wind_speed_mph**.16)) + (0.4275*air_temp_F*(wind_speed_mph**.16))
        wind_chill_C = 13.12 + (0.6215 * air_temp_C) - (11.37 * wind_speed__km_h**0.16) + (0.3965 * air_temp_C * (wind_speed__km_h**0.16))
        frostbite = frostbite_risk(wind_chill_F)
        print(f'The Wind Chill is: {wind_chill_F:.2f}{degree}F at a Air temp. of: {air_temp_F:.1f}{degree}F and Wind Speed of: {wind_speed_mph} MPH or a wind speed of: {wind_speed_knots:.2f} knots')
        print(f'The Wind Chill is: {wind_chill_C:.2f}{degree}C at a Air temp. of: {air_temp_C:.1f}{degree}C and Wind Speed of: {wind_speed__km_h:.2f} KM/H\n')
        print(f'The risk of {frostbite} with a wind chill of: {wind_chill_F:.2f}{degree}F')
        print('---------------------------------------------------------------------------------------------------------------------------------')

def main():
    a = int(input('Air Temp: '))
    u = str(input(f'is the temp in {degree}F or {degree}C (C\F): ')).upper()
    wind_chill(a,u)
    
main()

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


def main():
    air_temp = int(input('Air Temp: '))
    unit = str(input(f'is the temp in {degree}F or {degree}C (C\F): ')).upper()
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
        
        print(f'The Wind Chill is: {wind_chill_F:.2f}{degree}F at a Air temp. of: {air_temp_F:.1f}{degree}F and Wind Speed of: {wind_speed_mph} MPH or a wind speed of: {wind_speed_knots:.2f} knots')
        print(f'The Wind Chill is: {wind_chill_C:.2f}{degree}C at a Air temp. of: {air_temp_C:.1f}{degree}C and Wind Speed of: {wind_speed__km_h:.2f} KM/H\n')
        print('---------------------------------------------------------------------------------------------------------------------------------')
main()

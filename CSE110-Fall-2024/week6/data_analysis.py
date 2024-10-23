#created by matthew rosenthal
def get_year():
    while True:
        try:
            year = int(input('Enter the year: '))
            return year
        except ValueError:
            print('Please enter a valid year')

def get_country():
    while True:
        try:
            country = str(input('Enter country of interest: ')).strip().lower()
            return country
        except ValueError:
            print('Please enter a valid country')

def main():
    find_year = get_year()
    find_country = get_country()
    
    with open("BYU-I code\\CSE110-Fall-2024\\week6\\life-expectancy.csv", "r") as file:
        lowest_life = float('inf')
        highest_life = float('-inf')
        lowest_year = None
        lowest_country = None
        highest_year = None
        highest_country = None
        total_life_year = 0
        count_year = 0
        total_life_country = 0
        count_country = 0
        year_min_life = float('inf')
        year_max_life = float('-inf')
        country_min_life = float('inf')
        country_max_life = float('-inf')
        year_min_country = None
        year_max_country = None
        country_min_year = None
        country_max_year = None
        
        next(file)  # Skip header

        for line in file:
            part = line.strip().split(',')
            year = int(part[2])
            country = part[0].strip().lower()
            life = float(part[3])
            
            if life < lowest_life:
                lowest_life = life
                lowest_year = year
                lowest_country = part[0]
                
            if life > highest_life:
                highest_life = life
                highest_year = year
                highest_country = part[0]
                
            if year == find_year:
                total_life_year += life
                count_year += 1
                if life < year_min_life:
                    year_min_life = life
                    year_min_country = part[0]
                if life > year_max_life:
                    year_max_life = life
                    year_max_country = part[0]
                    
            if country == find_country:
                total_life_country += life
                count_country += 1
                if life < country_min_life:
                    country_min_life = life
                    country_min_year = year
                if life > country_max_life:
                    country_max_life = life
                    country_max_year = year

        if count_year > 0:
            avg_life_year = total_life_year / count_year
            print(f'For the year {find_year}:')
            print(f'The avg. life expectancy was {avg_life_year:.2f}')
            print(f'The max was {year_max_life:.2f} in {year_max_country}')
            print(f'The min was {year_min_life:.2f} in {year_min_country}')
        else:
            print(f'No data found for the year: {find_year}')
        
        print('')
        
        if count_country > 0:
            avg_life_country = total_life_country / count_country
            print(f'For the country {find_country.capitalize()}:')
            print(f'The avg. life expectancy was {avg_life_country:.2f}')
            print(f'The highest life expectancy was {country_max_life:.2f} in {country_max_year}')
            print(f'The lowest life expectancy was {country_min_life:.2f} in {country_min_year}')
        else:
            print(f'No data found for the country: {find_country.capitalize()}')
        
        print('')
        
        print(f'The overall max life expectancy is: {highest_life:.2f} from {highest_country} in {highest_year}')
        print(f'The overall min life expectancy is: {lowest_life:.2f} from {lowest_country} in {lowest_year}')


main()
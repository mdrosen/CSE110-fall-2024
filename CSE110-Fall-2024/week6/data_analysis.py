def main():
    with open("BYU-I code\CSE110-Fall-2024\week6\life-expectancy.csv", "r") as file:
        lowest_life = float('inf')
        highest_life = float('-inf')
        lowest_year = None
        lowest_country = None
        highest_year = None
        highest_country = None
        find_year = None
        
        next(file)
        
        for line in file:
            part = line.strip().split(',')
            year = int(part[2])
            country = part[0]
            life = float(part[3])
            
            if life < lowest_life:
                lowest_life = life
                lowest_year = year
                lowest_country = country
            if life > highest_life:
                highest_life = life
                highest_year = year
                highest_country = country
            if not find_year:
                find_year = get_year()
            
            if year == find_year:
                total_life = 0
                count = 0
                year_min_life = float('inf')
                year_max_life = float('-inf')
                year_min_country = None
                year_max_country = None
                
                for line_data in file:
                    data_part = line_data.strip().split(',')
                    data_year = int(data_part[2])
                    if data_year == year:
                        data_life = float(data_part[3])
                        total_life += data_life
                        count += 1
                        if data_life < year_min_life:
                            year_min_life = data_life
                            year_min_country = data_part[0]
                        if data_life > year_max_life:
                            year_max_life = data_life
                            year_max_country = data_part[0]
                if count > 0:
                    avg_life = total_life / count
                    print(f'for the year {find_year}:')
                    print(f'The avg. life expectancy was {avg_life:.2f} ')
                    print(f'The max was in {year_max_country} with {year_max_life:.2f}')
                    print(f'The min was in {year_min_country} with {year_min_life:.2f}')
                else:
                    print(f'no data found for: {find_year}')
                find_year = None
        print(f'the overall max life is: {highest_life:.2f} from {highest_country} in {highest_year}')
        print(f'the overall min life is: {lowest_life:.2f} from {lowest_country} in {lowest_year}')
def get_year():
    while True:
        try:         
            year = int(input('Enter the year: '))
            return year
        except ValueError:
            print('Please enter a valid year')
main()
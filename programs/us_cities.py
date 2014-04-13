## Opens file in "read mode"
data_file = open('us_cities.txt', 'r')

# "Colon"-separated, apparently.
for line in data_file:
    city, population = line.split(':')            # Tuple unpacking
    city = city.title()                           # Capitalize city names
    population = '{0:,}'.format(int(population))  # Add commas to numbers
    print(city.ljust(15) + population)
data_file.close()

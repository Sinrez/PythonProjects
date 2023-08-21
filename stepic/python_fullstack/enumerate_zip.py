# countries = ['Switzerland', 'Estonia', 'Sweden', 'Latvia', 'Butan', 'Nepal']

# for index in range(len(countries)):
#     print(f'{index+1}, {countries[index]}')

# for item in enumerate(countries, start=1):
#     print(item)

# for index, country in enumerate(countries, start=1):
#     print(f'{index}, {country}')

#=============================================================================================

# from itertools import zip_longest

# countries = ['Switzerland', 'Estonia', 'Sweden', 'Latvia', 'Bhutan', 'Nepal']
# capitals = ['Bern', 'Tallin', 'Stockholm', 'Riga']

# for country, capital in zip_longest(countries, capitals, fillvalue='Unknown'):
#     print(f'{capital} is the capital of {country}')

# ============================================================================================

countries = ['Switzerland', 'Estonia', 'Sweden', 'Latvia', 'Bhutan', 'Nepal']
capitals = ['Bern', 'Tallin', 'Stockholm', 'Riga', 'Thimphu', 'Kathmandu']

destinations = list(zip(countries, capitals))
print(destinations)

country, capital = zip(*destinations)
print(country)
print(capital)
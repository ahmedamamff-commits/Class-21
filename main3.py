country_code = {'india' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}

#search dictionary for country code of india
print("Country code for india -")
print(country_code.get('india', 'Not found'))

#search dictionary for country code of Japan
print("Country code for Japan -")
print(country_code.get('Japan', 'Not found'))
cities = {
    'kirkland': {
        'coutry': 'usa',
        'population': '10000',
        'fact': 'lakeside',
        },
    'beijing': {
        'coutry': 'china',
        'population': '1000000000000',
        'fact': 'capital of China',
        },
    'guiyang': {
        'coutry':'China',
        'population': '100000000',
        'fact': 'cool in summer',
        },
    }

for city, facts in cities.items():
    print ("City name: " + city)
    for fact, value in facts.items():
        print ("\t" + fact + ": " + value)

cities = {
    'Lublin': {
        'country': 'Poland',
        'population': '350k',
        'fact': 'wild east',
        },
    'Wroclaw': {
        'country': 'Poland',
        'population': '750k',
        'fact': 'idk cool',
        },
    'Warsaw': {
        'country': 'Poland',
        'population': '1.5mil',
        'fact': 'snobby',
        },
    'London': {
        'country': 'UK',
        'population': '8mil',
        'fact': 'bigg',
        },
    }

for city, info in cities.items():
    print(f"{city} is located in {info['country']}, has a population of "
          f"{info['population']} and is very {info['fact']}!\n")

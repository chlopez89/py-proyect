import utils
import read_csv
import charts
import os

def run():
    
  print('Continents','\n','Asia','\n',
    'Europe','\n',
    'Africa','\n',
    'Oceania','\n',
    'Europe','\n',
    'North America','\n',
    'South America','\n')
  continent = input('Type Continent => ')
  data = read_csv.read_csv('./data.csv')
  data = list(filter(lambda item : item['Continent'] == continent,data))

  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  print('Contry =>')
  print(*countries, sep='\n')
  country = input('Type Country => ')
  print(f'Country seleccionado {country}')
  result = utils.population_by_country(data, country)

  bar, pie=f'./imgs/{country}_bar.png', f'./imgs/{continent}_pie.png'
  if os.path.exists(bar):
    os.remove(bar)
  if os.path.exists(pie):
    os.remove(pie)
  charts.generate_pie_chart(countries, percentages, continent)
  if len(result) > 0:
    country_data = result[0]
    labels, values = utils.get_population(country_data)
    charts.generate_bar_chart(labels, values, country)
if __name__ == '__main__':
  run()
import pandas as pd
def get_population(df):
  # print(type(df))
  # print('Dato 2022: ')
  # print(int(df['2022 Population'].values))
  population_dict = {
      '2022': int(df['2022 Population'].values),
      '2020': int(df['2020 Population'].values),
      '2015': int(df['2015 Population'].values),
      '2010': int(df['2010 Population'].values),
      '2000': int(df['2000 Population'].values),
      '1990': int(df['1990 Population'].values),
      '1980': int(df['1980 Population'].values),
      '1970': int(df['1970 Population'].values)
  }
  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values


def population_by_country(df, country):
  # result = list(filter(lambda item: item['Country'] == country, data))
  result = df[df['Country']==country]
  return result

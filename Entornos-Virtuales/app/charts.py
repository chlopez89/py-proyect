import matplotlib.pyplot as plt

def generate_bar_chart(labels, values, country):
  fig, ax = plt.subplots()
  bar_container=ax.bar(labels, values)
  ax.set_title(f'Poblacion de los ultimos años de {country}')
  ax.set_xlabel('Años')
  ax.set_ylabel('Poblacion')
  # ax.bar_label(bar_container,fmt='{:,.0f}')
  # ax.legend(values, labels)
  plt.savefig(f'./imgs/{country}_bar.png')
  plt.close()
  # plt.show()

def generate_pie_chart(labels, values, continent):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig(f'./imgs/{continent}_pie.png')
  plt.close()
  # plt.show()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 40, 800]
  # generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)
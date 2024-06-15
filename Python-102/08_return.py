def sum_with_range(min, max):
  print("Minimo:", f'{min},', "Maximo: ", max)
  sum = 0
  for x in range(min, max):
    sum += x
  return sum


result = sum_with_range(1, 10)
print("Resultado:", result)
result_2 = sum_with_range(result, result + 10)
print(result_2)

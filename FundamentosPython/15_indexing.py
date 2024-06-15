text = "Ella sabe Python"
print(text[0])
print(text[1], '\n')

# print(text[999])
size = len(text)
print('Size => ', size)
print(text[size - 1])
print(text[-1], '\n')

# slicing
print(text, '\n')
print('text[0:5] =>', text[0:5])
print('text[10:16] =>', text[10:16])
print('text[:10] =>', text[:10])
print('text[5:-1] =>', text[5:-1])
print('text[5:] =>', text[5:])
print('text[:] =>', text[:])
print('text[10:16:1] =>', text[10:16:1])
print('text[10:16:2] =>', text[10:16:2])
print('text[::2] =>', text[::2])

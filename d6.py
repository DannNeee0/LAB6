from random import randint
#1
def character(row):
    s = 0
    for elem in row:
      if elem > 0 and elem % 2 == 0:
        s += elem
    return s

def print_matrix(matrix):
  for row in matrix:
    for elem in row:
      print(elem, end=' ')
    print()

while True:
  try:
    m = int(input('Введите размер матрицы: '))
    if m <= 0:
      print('Размер матрицы должен быть больше 0')
    else:
      break
  except ValueError:
    print('Некорректный ввод, попробуйте ещё раз!')

A = [[randint(-20, 20) for i in range(m)] for j in range(m)]

characteristics = [character(row) for row in A]
print('Получившаяся матрица:')
print_matrix(A)
print('Характеристика для каждой строки: ')
for i in range(len(characteristics)):
  print('Для', i+1, 'строки:', characteristics[i])

for i in range(m - 1):
  for j in range(m - 1 - i):
    if character(A[j]) > character(A[j+1]):
      g = A[j]
      A[j] = A[j+1]
      A[j+1] = g
print('Матрица после сортировки: ')
print_matrix(A)
#-----------------------------------------------------------------------------
#2
rus_eng_dict= {
'а' : 'a',  'б' : 'b', 'в' : 'v',
'г' : 'g', 'д' : 'd', 'е' : 'e',
'ё' : 'jo', 'ж' : 'zh', 'з' : 'z',
'и' : 'i', 'й' : 'j', 'к' : 'k',
'л' : 'l', 'м' : 'm', 'н' : 'n',
'о' : 'o', 'п' : 'p', 'р' : 'r',
'с' : 's', 'т' : 't', 'у' : 'u',
'ф' : 'f', 'х' : 'kh', 'ц' : 'c',
'ч' : 'ch', 'ш' : 'sh', 'щ' : 'shch',
'ъ' : '', 'ы' : 'y', 'ь' : '',
'э' : 'e', 'ю' : 'ju', 'я' : 'ja'
}
while True:
    text = input('Введите строку на русском языке: ')
    if text == '':
      print('Строка не может быть пустой')
    else:
      break
eng = ''
for letter in text:
  low_let = letter.lower()
  if low_let in rus_eng_dict:
    a = rus_eng_dict[low_let]
    eng += a
  else:
    eng += low_let
print('Первоначальная строка:', text)
print('Преобразованная строка:', eng)
#-----------------------------------------------------------------------------



FILENAME = 'recipes.txt'
def get_shop_list_by_dishes(dishes, person_count):
  pass


with open(FILENAME) as f:
  for line in f:
    book_line = line.strip()
    # print(type(book_line))
    if type(book_line) == int():
      print('int', book_line)

# print(cook_book)
# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ]
#   }
# Омлет
# 3
# Яйцо | 2 | шт
# Молоко | 100 | мл
# Помидор | 2 | шт

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
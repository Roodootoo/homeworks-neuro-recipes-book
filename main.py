# Task 3
def result_file():
    file_book = []
    for filename in range(1, 4):
        with open('sort/'+str(filename)+'.txt') as file:
            file_book_item = {}
            lines = file.readlines()
            file_book_item['filename'] = str(filename)+'.txt'
            file_book_item['len'] = len(lines)
            file_book_item['lines'] = lines
        file_book.append(file_book_item)
    file_book_sort = sorted(file_book, key=lambda x: x['len'])
    result_file_text =''
    for file_book_item in file_book_sort:
        result_file_text += file_book_item['filename']+'\n'
        result_file_text += str(file_book_item['len'])+'\n'
        result_file_text += ''.join(file_book_item['lines'])+'\n'
    with open('sort/result.txt', 'w') as f:
        f.write(result_file_text)
        print('Записан файл sort/result.txt')

# Task 2
def get_shop_list_by_dishes(cook_book, dishes, person_count):
    cook_ingredients = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            cook_ingredients.setdefault(ingredient['ingredient_name'])
            dict_measure = cook_ingredients[ingredient['ingredient_name']]
            if type(dict_measure) == type(None):
                dict_measure = {}
                quantity = 0
            else:
                quantity = dict_measure.get('quantity')
            dict_measure['measure'] = ingredient['measure']
            dict_measure['quantity'] = int(ingredient['quantity']) * person_count + quantity
            cook_ingredients[ingredient['ingredient_name']] = dict_measure
    print('Task 2:', cook_ingredients)


# Task 1
def read_file(FILENAME):
    cook_book = {}
    with open(FILENAME) as file:
        for line in file:
            name_recipes = line.strip()
            list_ingredients = []
            number_ingredients = int(file.readline())
            for i_ingredient in range(number_ingredients):
                list_book_line = file.readline().strip().split(' | ')
                dict_ingredient = {}
                dict_ingredient['ingredient_name'] = list_book_line[0]
                dict_ingredient['quantity'] = list_book_line[1]
                dict_ingredient['measure'] = list_book_line[2]
                list_ingredients.append(dict_ingredient)
            cook_book[name_recipes] = list_ingredients
            file.readline()

    return cook_book

def main():
    cook_book = read_file('recipes.txt')
    print('Task 1:', cook_book)
    get_shop_list_by_dishes(cook_book, ['Фахитос', 'Омлет'], 2)
    result_file()


main()
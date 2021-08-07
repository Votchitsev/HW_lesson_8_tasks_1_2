with open("cook_book.txt", 'r', encoding='utf-8') as cook_book:
    cook_book_dict = {}
    d = []
    ingredient_names = ['ingredient_name', 'quantity', 'measure']

    for line in cook_book:
        dish = line.strip()
        cook_book_dict[dish] = []
        dish_record = int(cook_book.readline())
        d.append(dish_record)
        for i in range(dish_record):
            c = cook_book.readline().strip().split('|')
            ingredient_dict = dict(zip(ingredient_names, c))
            cook_book_dict[dish].append(ingredient_dict)
        cook_book.readline()
        print()


def get_shop_list_by_dishes(dishes, person_count):
    get_shop_list = {}
    for dish_name in dishes:
        for ingredients in cook_book_dict[dish_name]:
            if ingredients['ingredient_name'] not in get_shop_list.keys():
                get_shop_list[ingredients['ingredient_name']] = {'measure': ingredients['measure'],
                                                                 'quantity': int(ingredients['quantity']) * person_count
                                                                 }
            else:
                get_shop_list[ingredients['ingredient_name']]['quantity'] += int(ingredients['quantity']) * person_count
    return get_shop_list


a = get_shop_list_by_dishes(['Омлет', 'Омлет'], 2)
print(a)



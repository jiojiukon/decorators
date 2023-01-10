from loggers import logger

cook_book = {}

one_recipe = []

shop_list = {}

@logger
def good_output(dic):
    for k,v in dic.items():
        print(f'{k}:')
        if not isinstance(v,dict):
            for i in v:
                print(i)
        else:
            print(v)

@logger
def shoplist():
    with open('shoplist.txt','w') as shopping:
        for dish_name, ingredients in shop_list.items():
            shopping.writelines(f'{dish_name}:\n{ingredients}\n')

@logger
def get_shop_list_by_dishes(dishes, person_count): 
    for dish in dishes: 
        if dish in cook_book.keys():
            ingr_list = cook_book[dish]
            for ingredient in ingr_list:
                total_quantity = {}
                total_quantity['Количество'] = int(ingredient['Количество']) * person_count
                total_quantity['Единица измерения'] = ingredient['Единица измерения']
                if not ingredient['Название ингредиента'] in shop_list.keys():
                    shop_list[ingredient['Название ингредиента']] = total_quantity
                else:
                    total_quantity['Количество'] += shop_list[ingredient['Название ингредиента']]['Количество']
                    shop_list[ingredient['Название ингредиента']] = total_quantity
        else:
            print(f'Блюда {dish} нет в книге рецептов!')         
    return good_output(shop_list)


with open('recipes.txt', 'r', encoding ='utf8') as recipes_list:
    for line in recipes_list:
        dish = line.rstrip()
        count_of_products = recipes_list.readline()
        for i in range(int(count_of_products)):
            product = recipes_list.readline().rstrip()
            ingredient_name, quantity, measure = product.split('| ')
            one_ingredient = {'Название ингредиента' : ingredient_name, 'Количество' : quantity, 'Единица измерения': measure }
            if i !=int(count_of_products):
                one_recipe.append(one_ingredient)
        cook_book[dish] = (one_recipe)
        one_recipe = []
        recipes_list.readline()

good_output(cook_book)
get_shop_list_by_dishes(['Капитал', 'Запеченный картофель'], 4)

with open('shoplist.txt','w', encoding='utf8') as shopping:
    for ingr_name, ing_measure  in shop_list.items():
        amount = list(ing_measure.values())
        shopping.write(f'{ingr_name}: ')
        for i in amount:
            i = str(i) 
            shopping.write(f'{i}')
        shopping.write(f'\n')
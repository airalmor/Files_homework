#Задача 1

def cookbook_func(name_file):
    from pprint import pprint
    cook_book={}
    with open(name_file) as file_obj:
        dishes=[]
        ingridients=[]
        name=file_obj.readline().strip()
        dishes.append(name)
        for lines in file_obj:
            qty = int(lines.strip())
            dish_ingrid = []
            for i in range(qty):
                ingridient_dict={}
                data = file_obj.readline().strip()
                splitted_data = data.split('|')
                ingridient_dict['ingridient_name']=splitted_data[0]
                ingridient_dict['quantity'] = int(splitted_data[1])
                ingridient_dict['mesure']=splitted_data[2]
                dish_ingrid.append(ingridient_dict)
            file_obj.readline()
            name = file_obj.readline().strip()
            ingridients.append(dish_ingrid)
            dishes.append(name)
        cook_book=dict(zip(dishes,ingridients))
        pprint(cook_book)

cookbook_func()
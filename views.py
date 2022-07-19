from pprint import pprint
from models import Cars
from serializers import CarSerializer

def product_list():
    serializer = CarSerializer()
    products = serializer.serialize_queryset()
    return products

def product_create():
    type_ = input(f'Выберите тип кузова {Cars.type_}: ')
    brend = input('Введите марку: ')
    model = input('Введите модель: ')
    year = input('Год выпуска: ')
    engine = input('Объем двигателя: ')
    color = input('Цвет: ')
    mileage = input("Пробег: ")
    price = input("Цена: ")

    Cars(brend, model, year, engine, color, type_, mileage, price)
    return 'Машина создана'

def retrieve():
    id = input("Введите ID : ")
    id_ = Cars.object[int(id)]
    return id_



def product_update():
    id = input("Введите ID : ")
    c = input('Введите поле для изменения: ')
    d = input('Введите новое значение поля: ')
    for k in Cars.object:
        if int(id) == k['id']:
            k[c] = d
            print(f'Значение поля {k[str(c)]} изменено на {d}')
        else:
            print('Нет такого поля')
    return Cars.object

def product_delete():
    id_ = input("Введите ID : ")
    for k in Cars.object:
        if id_ == k[id_]:
            l = Cars.object.pop(k)

            print("Продукт успешно удален")
        else:
            return 'IDError'
    



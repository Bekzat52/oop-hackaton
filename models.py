

class Cars:

    object = []

    __id = 0
    type_ = ('седан', 'универсал', 'купе', 'хэтчбек', 'минивен', 'внедорожник', 'пикап')
    def __init__(self, brend:str, model:str, year:int, engine, color:str, type_:str, mileage:int, price):
        self.id = Cars.__id
        self.brend = brend
        self.model = model
        self.year = year
        self.engine = engine
        self.color = color
        if type_ in Cars.type_:
            self.type_ = type_
        else:
            raise Exception ('choose correct type')
        self.mileage = mileage
        self.price = price
        Cars.object.append([self])
        Cars.__id +=1

        with open ('bd.json', 'w+') as file:
            file.writelines(Cars.object)


print(Cars.object)



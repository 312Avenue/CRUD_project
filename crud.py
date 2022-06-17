from settings import settings
from pyairtable import Table


class CRUD:
    table = Table(settings.api_key, settings.TABLE_ID, settings.TABLE_NAME)

    def check_id(self, id_):
        table = Table(settings.api_key, settings.TABLE_ID, settings.TABLE_NAME)
        for i in table.all():
            if id_ == i['id']:
                return i
        return False


    def create(self):
        print('Create auto')
        req = self.table.create({
            'Marka': input('Введите марку машины: '),
            'Model': input('Введите модель машины: '),
            'Year': int(input('Введите годы выпуска машины: ')),
            'Volume': float(input('Введите объем двигателя машины: ')),
            'Color': input('Введите цвет машины: '),
            'Machine type': input('Введите тип кузова машины: '),
            'km': int(input('Введите пробег машины: ')),
            'Price': float(input('Введите стоимость машины: '))
            })
        
        return req
    

    def update(self, id_):
        if self.check_id(id_):
            car = self.check_id(id_)["fields"]
            print(f'Update auto: {car}')
            req = self.table.update(id_, {
                'Marka': input('Введите марку машины: ') or car["Marka"],
                'Model': input('Введите модель машины: ') or car["Model"],
                'Year': int(input('Введите годы выпуска машины: ')) or int(car["Year"]),
                'Volume': float(input('Введите объем двигателя машины: ')) or float(car["Volume"]),
                'Color': input('Введите цвет машины: ') or car["Color"],
                'Machine type': input('Введите тип кузова машины: ') or car["Machine type"],
                'km': int(input('Введите пробег машины: ')) or int(car["km"]),
                'Price': float(input('Введите стоимость машины: ')) or float(car["Price"])
                })
            
            return req


    def listining(self):
        return self.table.all()


    def retrieve(self, id_):
        if self.check_id(id_):
            return self.check_id(id_)
        else:
            return f'{id_} not found'


    def delete(self, id_):
        if self.check_id(id_):
            return self.table.delete(id_)
        else:
            return f'{id_} not found'


crud = CRUD()

class Automobile:
    def __init__(self, name: str, year_of_production: int = 2020, producer: str = None, 
                brand: str = None,
                fuel_consumption: float = 0.0): # I wrote it this way to make it easier to view the code
        self.name = name
        self.year_of_production = year_of_production
        self.producer = producer
        self.brand = brand
        self.mileage: float = 0.0
        self.fuel_consumption = fuel_consumption

    def __str__(self):
        if self.brand == None:
            raise NameError('The car has no brand!')
        return f'\nProducer: {self.producer}\nCar name: {self.name}\nCar Brand: {self.brand}'
    
    __repr__ = __str__

first_car = Automobile('Tesla')
second_car = Automobile('Nissan')

first_car.brand = 'Cybertruck'
second_car.brand = 'Juke'

first_car.fuel_consumption = 0.0 # because electric
second_car.fuel_consumption = 2.4

first_car.producer = 'Tesla'
second_car.producer = '日産自動車株式会社' # this is the first thing I found

# print(first_car)
# print(second_car)

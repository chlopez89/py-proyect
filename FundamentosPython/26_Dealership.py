class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True
        
    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"El coche {self.brand} - {self.model}, ha sido vendido.")
        else:
            print(f"el coche {self.brand} - {self.model} no esta disponible.")
    
    def check_availability(self):
        return self.is_available
    
    def get_price(self):
        return self.price

class Customer:
    def __init__(self, name:str):
        self.name = name
        self.cars_purchased = []
        
    def buy_car(self, car:Car):
        if car.check_availability():
            car.sell()
            self.cars_purchased.append(car)
        else:
            print(f"lo siento, {car.brand} - {car.model}, no esta disponible.")
    
    def inquire_car(self, car:Car):
        availability = "disponible" if car.check_availability() else "No esta disponible"
        print(f"El coche {car.brand} - {car.model} está {availability} y cuesta ${car.get_price()}")

class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_car(self, car:Car):
        self.inventory.append(car)
        print(f"El coche {car.brand} - {car.model}, ha sido añadido al inventario")
        
    def register_customer(self, customer:Customer):
        self.customers.append(customer)
        print(f"El cliente {Customer.name}, ha sido refistrado en la concesionaria.")
        
    def show_available_cars(self):
        print("Coches disponibles en la concesionaria:")
        contador_car=0
        for car in self.inventory:
            contador_car+=1
            if car.check_availability():
                print(f"{contador_car}.- {car.brand} - {car.model} por ${car.get_price()}")

# Crear instancias de coches.
print("# Crear instancias de coches.")
car_1 = Car("Totoya", "Corolla", 200000)
car_2 = Car("Honda", "Civic", 250000)
car_3 = Car("Nissan", "Xtrain", 285000)
car_4 = Car("Kia", "Rio", 230000)

# Crear instancias de cliente
print("# Crear instancias de cliente")
customer_1 = Customer("Christian")
customer_1 = Customer("Carlos")
customer_1 = Customer("Saul")

# Crear instancia de concecionario y registrar coches y clientes.
print("# Crear instancia de concecionario y registrar coches y clientes.")
dealership = Dealership()
dealership.add_car(car_1)
dealership.add_car(car_2)
dealership.add_car(car_3)
dealership.add_car(car_4)

# Mostrar coches disponibles.
print("# Mostrar coches disponibles.")
dealership.show_available_cars()

# Cliente consulta un coche
print("# Cliente consulta un coche")
customer_1.inquire_car(car_2)

# Cliente compra un coche
print("# Cliente compra un coche")
customer_1.buy_car(car_2)

# Mostrar coches disponibles.
print("# Mostrar coches disponibles.")
dealership.show_available_cars()

# Cliente intenta comprar un coche ya vendido.
print("# Cliente intenta comprar un coche ya vendido")
customer_1.buy_car(car_2)

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active=True
        self.message=""
        
    def deposito(self, amount:int):
        if self.is_active:
            self.balance += amount
            self.message=f"Se ha depositado ${amount}, Saldo actual ${self.balance}"
        else:
            self.message="No se puede depositar la cuenta no esta activa."
    def withdraw(self, amount:int):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                self.message=f"Se ha retirado ${amount}, Saldo actual ${self.balance}"
            else:
                self.message=f"No se puede retirar la cuenta no tiene fondos suficientes, Cuenta con ${self.balance}"
        else:
            self.message="No se puede retirar la cuenta no esta activa."
            
    def deactivate_account(self):
        self.is_active = False
        print(f"La cuenta ha sido desactivada: {self.is_active}", "\n")
        self.message=f"La cuenta ha sido desactivada: {self.is_active}"

    def activate_account(self):
        self.is_active= True
        print(f"La cuenta ha sido activada: {self.is_active}", "\n")
        self.message=f"La cuenta ha sido activada: {self.is_active}"
        
    def set_message(self, mensaje:str):
        self.message=mensaje

Cuenta=BankAccount("Christian", 500)
while True:
    print("Hola que transaccion desea realizar.")
    optiones=["1.- Deposito", "2.- Retiro", "3.- Desactivar Cuenta", "4.- Activar Cuenta", "5.- Salir"]
    print(*optiones, sep="\n")
    if Cuenta.message!="":
        print(f"\n==:{Cuenta.message}:==\n")
    option=input("Digite una opcion -->")
    match option:
        case "1":
            amount=input("Cuanto desea depositar: $")
            if amount.isnumeric():
                Cuenta.deposito(int(amount))
            else:
                Cuenta.set_message("Esta cantidad no es numerica.")
        case "2":
            amount=input("Cuanto desea retirar: $")
            if amount.isnumeric():
                Cuenta.withdraw(int(amount))
            else:
                Cuenta.set_message("Esta cantidad no es numerica")
        case "3":
            confirmacion=input("Seguro que desea desactivar la cuenta: confirma con (Si) ")
            if confirmacion=="Si":
                Cuenta.deactivate_account()
        case "4":
            confirmacion=input("Seguro que desea activar la cuenta: confirma con (Si) ")
            if confirmacion=="Si":
                Cuenta.activate_account()
        case "5":
            Cuenta.set_message("Gracias por su preferencia -->Saliendo....")
            break
        case _:
            Cuenta.set_message("Opcion no valida")
            
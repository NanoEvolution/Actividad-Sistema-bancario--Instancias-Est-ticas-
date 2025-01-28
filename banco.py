import time
import os

class CuentaBancaria:
    def __init__(self, saldo, titular):
        self.saldo = float(saldo)
        self.titular = titular

    def iniciar_cuenta(self):
        print(f"Cuenta '{self.titular}' creada. Saldo = {self.saldo}€")
    
    def obtener_saldo(self):
        print(f"Saldo de la cuenta '{self.titular}' = {self.saldo}€")

    def depositar(self, cantidad):
        print("Depositando saldo...")
        time.sleep(2)
        self.saldo += cantidad
        print(f"Deposito de '{cantidad}€' completado.")
        print(f"Saldo actualizado a {self.saldo}€")
    
    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            print("Retirando saldo...")
            time.sleep(2)
            self.saldo -= cantidad
            print(f"Retiro de {cantidad}€ completado.")
            print(f"Saldo actualizado a {self.saldo}€")
        else:
            print(f"Retiro interrumpido. Lo siento, la cuenta '{self.titular}' solo tiene un saldo de {self.saldo}€")
    
    def transferir(self, cantidad, cuenta):
        if cantidad <= self.saldo:
            print("Iniciando transferencia...")
            time.sleep(2)
            self.saldo -= cantidad
            cuenta.saldo += cantidad
            print(f"Se ha transferido {cantidad} con éxito a la cuenta de {cuenta.titular}")
            print(f"Saldo actualizado a {self.saldo}€")
            print(f"Saldo de la cuenta '{cuenta.titular}' actualizado a {cuenta.saldo}")
        else:
            print(f"Retiro interrumpido. Lo siento, la cuenta '{self.titular}' solo tiene un saldo de {self.saldo}€")

class CuentaAhorros(CuentaBancaria):
    def __init__(self, saldo, titular):
        super().__init__(saldo, titular)
    
    def iniciar_cuenta(self):
        super().iniciar_cuenta()

    def obtener_saldo(self):
        super().obtener_saldo()

    def depositar(self, cantidad):
        print("Depositando saldo...")
        time.sleep(2)
        self.saldo += cantidad * 1.05
        print(f"Deposito de '{cantidad}€' completado con recompensa del 5% de interés.")
        print(f"Saldo actualizado a {self.saldo}€")

    def retirar(self,cantidad):
        super().retirar(cantidad)

    def transferir(self, cantidad, cuenta):
        super().transferir(cantidad, cuenta)
     

class CuentaRecompensas(CuentaBancaria):
    def __init__(self, saldo, titular):
        super().__init__(saldo, titular)
    
    def iniciar_cuenta(self):
        super().iniciar_cuenta()

    def obtener_saldo(self):
        super().obtener_saldo()

    def depositar(self, cantidad):
        super().depositar(cantidad)

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            print("Retirando saldo...")
            time.sleep(2)
            self.saldo -= cantidad + 5
            print(f"Retiro de {cantidad}€ completado con tarifa de 5€.")
            print(f"Saldo actualizado a {self.saldo}€")
        else:
            print(f"Retiro interrumpido. Lo siento, la cuenta '{self.titular}' solo tiene un saldo de {self.saldo}€")

    def transferir(self, cantidad, cuenta):
        super().transferir(cantidad, cuenta)

os.system('cls')

print(" --- CUENTA 1 ---")
Cuenta1 = CuentaBancaria(1000, "Cliente1")
time.sleep(0.2)
Cuenta1.iniciar_cuenta()
time.sleep(0.2)
Cuenta1.obtener_saldo()
time.sleep(0.2)
Cuenta1.retirar(10000)
time.sleep(0.2)
Cuenta1.retirar(10)
time.sleep(0.2)

print("\n --- CUENTA 2 ---")
Cuenta2 = CuentaBancaria(2000, "Cliente2")
time.sleep(0.2)
Cuenta2.obtener_saldo()
time.sleep(0.2)
Cuenta2.depositar(500)
time.sleep(0.2)

print("\n --- TRANSFERENCIA DE 1 A 2 ---")
Cuenta1.transferir(10000, Cuenta2)
time.sleep(0.2)

print("\n --- TRANSFERENCIA DE 2 A 1 ---")
Cuenta2.transferir(100, Cuenta1)
time.sleep(0.2)

print("\n --- CUENTA CON RECOMPENSAS ---")
CuentaIntereses = CuentaRecompensas(1000, "CuentaIntereses")
time.sleep(0.2)
CuentaIntereses.iniciar_cuenta()
time.sleep(0.2)
CuentaIntereses.obtener_saldo()
time.sleep(0.2)
CuentaIntereses.depositar(100)
time.sleep(0.2)

print("\n --- CUENTA AHORROS ---")
Cuenta_Ahorros = CuentaAhorros(1000, "CuentaAhorros")
time.sleep(0.2)
Cuenta_Ahorros.iniciar_cuenta()
time.sleep(0.2)
Cuenta_Ahorros.obtener_saldo()
time.sleep(0.2)
Cuenta_Ahorros.depositar(100)
time.sleep(0.2)
Cuenta_Ahorros.transferir(10000, Cuenta2)
time.sleep(0.2)
Cuenta_Ahorros.transferir(1000, Cuenta2)
time.sleep(0.2)
import time
import os

class CuentaBancaria:
    def __init__(self, saldo, titular):
        self.saldo = float(saldo)
        self.titular = titular

    def obtener_saldo(self):
        print(f"Saldo de la cuenta '{self.titular}': {self.saldo}€")

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Depósito de {cantidad}€ completado. Saldo actualizado: {self.saldo}€")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro de {cantidad}€ completado. Saldo actualizado: {self.saldo}€")
        else:
            print(f"Fondos insuficientes. Saldo actual: {self.saldo}€")

    def transferir(self, cantidad, cuenta):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            cuenta.saldo += cantidad
            print(f"Transferencia de {cantidad}€ a {cuenta.titular} completada.")
        else:
            print(f"Fondos insuficientes. Saldo actual: {self.saldo}€")

class CuentaAhorros(CuentaBancaria):
    def depositar(self, cantidad):
        self.saldo += cantidad * 1.05
        print(f"Depósito de {cantidad}€ con un 5% de interés. Saldo actualizado: {self.saldo}€")

class CuentaRecompensas(CuentaBancaria):
    def retirar(self, cantidad):
        if cantidad + 5 <= self.saldo:
            self.saldo -= cantidad + 5
            print(f"Retiro de {cantidad}€ con una tarifa de 5€. Saldo actualizado: {self.saldo}€")
        else:
            print(f"Fondos insuficientes. Saldo actual: {self.saldo}€")

def menu():
    cuentas = {
        "Cliente1": CuentaBancaria(1000, "Cliente1"),
        "Cliente2": CuentaBancaria(2000, "Cliente2"),
        "CuentaAhorros": CuentaAhorros(1500, "CuentaAhorros"),
        "CuentaRecompensas": CuentaRecompensas(1800, "CuentaRecompensas")
    }
    
    cuenta_actual = None

    while True:
        os.system('cls')
        print("\n--- Menú del Sistema Bancario ---")
        print("1. Ver cuentas disponibles")
        print("2. Seleccionar cuenta")
        print("3. Ver saldo")
        print("4. Depositar dinero")
        print("5. Retirar dinero")
        print("6. Transferir dinero")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            print("Cuentas disponibles:")
            for titular in cuentas:
                print(f"- {titular}")
        elif opcion == "2":
            nueva_cuenta = input("Ingrese el titular de la cuenta a seleccionar: ")
            if nueva_cuenta in cuentas:
                cuenta_actual = cuentas[nueva_cuenta]
                print(f"Se ha cambiado a la cuenta de {cuenta_actual.titular}.")
            else:
                print("Cuenta no encontrada.")
        elif opcion in ["3", "4", "5", "6"] and cuenta_actual is None:
            print("Debe seleccionar una cuenta antes de realizar operaciones.")
        elif opcion == "3":
            cuenta_actual.obtener_saldo()
        elif opcion == "4":
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cuenta_actual.depositar(cantidad)
        elif opcion == "5":
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cuenta_actual.retirar(cantidad)
        elif opcion == "6":
            destinatario = input("Ingrese el titular de la cuenta destino: ")
            if destinatario in cuentas:
                cantidad = float(input("Ingrese la cantidad a transferir: "))
                cuenta_actual.transferir(cantidad, cuentas[destinatario])
            else:
                print("Cuenta no encontrada.")
        elif opcion == "7":
            print("Saliendo del sistema bancario.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
        
        input("Presione 'Enter' para continuar...")
        os.system('cls')

menu()

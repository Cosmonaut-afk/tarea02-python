from FinancieroApp import (
    FinancieroApp,
    IngresosBA_app,
    EgresosBA_app,
)

print("Inicializando la aplicación de finacias: \n")

# Creamos la instancia
financieroAppObj = FinancieroApp()
IngresosAppObj = IngresosBA_app()
EgresosAppObj = EgresosBA_app()


def nuevoIngreso():
    print("** Haciendo un ingreso a su cuenta ** \n")
    monto = int(input("Cuanto es el monto que desea ingresar? : "))
    financieroAppObj.ingresoACuenta(monto)
    IngresosAppObj.realizarIngreso(monto)


def nuevoEgreso():
    print("** Haciendo un egreso a su cuenta ** \n")
    monto = int(input("Cuanto es el monto que desea sacar? : "))
    financieroAppObj.egresoACuenta(monto)
    EgresosAppObj.realizarEgreso(monto)


def reporteTransacciones():
    print("** Realizando reporte de todas la transacciones de cuenta ** \n")
    print(f"Transacciones : {financieroAppObj.transactionNumber()} \n")
    transactionList = financieroAppObj.totalTransacciones()
    print("\n")
    if len(transactionList) > 0:
        for transaction in transactionList:
            print(transaction)
        print("\n")
    else:
        print("\n ** No hay transacciones de momento ** ")


def reporteTotal():
    print("** Realizando reporte total de su la cuenta financiera ** \n")
    financieroAppObj.totalCuenta()


def reporteIngresos():
    print("** Realizando reporte de todos los ingresos de la cuenta ** \n")
    print(f"Ingresos : {IngresosAppObj.numeroDeIngresos()} \n")
    ingresosList = IngresosAppObj.todosLosIngresos()
    print("\n")
    if len(ingresosList) > 0:
        for ingreso in ingresosList:
            print(ingreso)
        print("\n")
    else:
        print("\n ** No hay ingresos de momento **")


def reporteEgresos():
    print("** Realizando reporte de todos los ingresos de la cuenta ** \n")
    print(f"Ingresos : {EgresosAppObj.numeroDeEgresos()} \n")
    egresosList = EgresosAppObj.todosLosEgresos()
    print("\n")
    if len(egresosList) > 0:
        for egreso in egresosList:
            print(egreso)
        print("\n")
    else:
        print("\n ** No hay egresos de momento **")


while True:
    print("Menu de cuenta financiera: \n")
    print("(0) salir")
    print("(1) Registrar un ingreso")
    print("(2) Registrar un egreso")
    print("(3) reporte de todos los ingresos")
    print("(4) reporte de todos los egresos")
    print("(5) reporte de todas las transacciones")
    print("(6) reporte del total de la cuenta")
    option = int(input("opcion: "))

    if option == 0:
        print("Usted ha finalizado FinancieroApp\n")
        break
    elif option == 1:
        nuevoIngreso()
    elif option == 2:
        nuevoEgreso()
    elif option == 3:
        reporteIngresos()
    elif option == 4:
        reporteEgresos()
    elif option == 5:
        reporteTransacciones()
    elif option == 6:
        reporteTotal()

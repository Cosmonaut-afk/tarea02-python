class FinancieroApp:
    def __init__(self):
        self.saldo = 0.0
        self.transaccionesCounter = 0
        self.transactionList = []

    def ingresoACuenta(self, monto):
        self.transaccionesCounter += 1
        transactionID = self.transaccionesCounter
        trasnactionDict = {"Id": transactionID, "Ingreso": monto}
        self.transactionList.append(trasnactionDict)
        self.saldo += monto
        IngresosObj.realizarIngreso(monto)
        print(
            "Este es el saldo que tienes luego de ingresar saldo : "
            + str(self.saldo)
            + "\n"
        )

    def egresoACuenta(self, monto):
        if self.saldo >= monto:
            self.transaccionesCounter += 1
            transactionID = self.transaccionesCounter
            trasnactionDict = {"Id": transactionID, "Egreso": monto}
            self.transactionList.append(trasnactionDict)
            self.saldo -= monto
            EgresosObj.realizarEgreso(monto)
            print(
                "Este es el saldo que tienes luego de egresar saldo: "
                + str(self.saldo)
                + "\n"
            )

        else:
            print("NO SE PUEDE RETIRAR MAS DEL MONTO QUE TIENES, INTENTALO DE NUEVO.")
            print("Este es el saldo que tienes: " + str(self.saldo) + "\n")

    def totalCuenta(self):
        result = print(" ** EL SALDO TOTAL DE LA CUENTA ES: " + str(self.saldo) + "\n")
        return result

    def totalTransacciones(self):
        return self.transactionList

    def transactionNumber(self):
        return len(self.transactionList)

    def totalIngresos(self):
        IngresosObj.todosLosIngresos

    def totalEgresos(self):
        IngresosObj.todosLosEgresos


class IngresosBA_app:
    def __init__(self):
        self.ingresoCounter = 0
        self.ingresosList = []

    def realizarIngreso(self, monto):
        self.ingresoCounter += 1
        ingresosID = self.ingresoCounter
        ingresosDict = {
            "IDingreso ": ingresosID,
            "Monto ": monto,
        }
        self.ingresosList.append(ingresosDict)

    def todosLosIngresos(self):
        return self.ingresosList

    def numeroDeIngresos(self):
        return len(self.ingresosList)


class EgresosBA_app:
    def __init__(self):
        self.egresoCounter = 0
        self.egresosList = []

    def realizarEgreso(self, monto):
        self.egresoCounter += 1
        egresosID = self.egresoCounter
        egresosDict = {
            "IDegreso ": egresosID,
            "Monto ": monto,
        }
        self.egresosList.append(egresosDict)

    def todosLosEgresos(self):
        return self.egresosList

    def numeroDeEgresos(self):
        return len(self.egresosList)


IngresosObj = IngresosBA_app()
EgresosObj = EgresosBA_app()
FinancieroObj = FinancieroApp()
#!/usr/bin/python3
import json
import os.path

class Restaurante:

    def __init__(self, total_comida, propina):
        self.comida = total_comida 
        self.propina = propina

    def calcular_propina(self):
        total = self.comida * (self.propina / 100)
        return total

class Total(Restaurante):
    def __init__(self, total_comida, propina):
        super().__init__(total_comida, propina)

    def calcular_total(self):
        propina = self.calcular_propina()
        total_pagar = self.comida + propina
        return {"total": total_pagar}

class Registro(Total):
    def registrar(self, filename, data):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                if os.stat(filename).st_size > 0:
                    obj_list = json.load(file)
                else:
                    obj_list = []
        else:
            obj_list = []

        obj_list.extend([
            {
                "comida": self.comida,
                "propina": self.propina,
                "total_pagar": self.calcular_total()["total"]
            }
        ])

        with open(filename, "w") as file:
            json.dump(obj_list, file, indent=2)
            file.write('\n')

def main():
    total_comida = float(input("Ingrese el total de la comida: "))
    porcentaje_propina = float(input("Ingrese el porcentaje de propina: "))
    data = [{
        "comida": total_comida,
        "propina": porcentaje_propina,
        "total_pagar": Total(total_comida, porcentaje_propina).calcular_total()["total"]
    }]

    t = Total(total_comida, porcentaje_propina)
    print("el total es:", t.calcular_total()["total"])

    r = Registro(total_comida, porcentaje_propina)
    r.registrar("base.json", data)

if __name__ == "__main__":
    main()

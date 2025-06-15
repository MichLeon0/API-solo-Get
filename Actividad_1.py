from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

#Ceamos un objetos a paryor de la clase de FatAPi 
app= FastAPI()

class User(BaseModel):
    Nombre:str
    Semestre: int
    Porcentaje: int
    

alumnos_list = [
                User(Nombre="ANGEL AGUILAR SALDIVAR", Semestre=6, Porcentaje=58),
                User(Nombre="ALEJANDRO AMADOR LAGUNES", Semestre=6, Porcentaje=58),
                User(Nombre="ERWIN AVENDAÑO VEGA", Semestre=6, Porcentaje=52),
                User(Nombre="DIEGO CANNATA CARDENAS", Semestre=7, Porcentaje=58),
                User(Nombre="CARLOS CASTRO GASPAR", Semestre=6, Porcentaje=58),
                User(Nombre="ANDRES CRUZ ORTIZ", Semestre=6, Porcentaje=64),
                User(Nombre="HECTOR ESCOBAR MARISCAL", Semestre=6, Porcentaje=58),
                User(Nombre="KEIRA GARRIDO AGUIRRE", Semestre=6, Porcentaje=58),
                User(Nombre="JOE GONZALEZ HERRERA", Semestre=6, Porcentaje=58),
                User(Nombre="PABLO IBARRA VALENCIA", Semestre=6, Porcentaje=58),
                User(Nombre="EDUARDO JUAREZ CORTES", Semestre=6, Porcentaje=58),
                User(Nombre="MICHELL LEON PAREDES", Semestre=6, Porcentaje=58),
                User(Nombre="JOHAN MARTINEZ GARCIA", Semestre=7, Porcentaje=58),
                User(Nombre="HECTOR MENDOZA MERINO", Semestre=6, Porcentaje=58),
                User(Nombre="FERNANDO MORALES CILIA", Semestre=6, Porcentaje=58),
                User(Nombre="DIEGO NAVA RIVERA", Semestre=6, Porcentaje=58),
                User(Nombre="ALFREDO NAVARRETE MONTES", Semestre=6, Porcentaje=58),
                User(Nombre="ANDY PEREZ PAVON", Semestre=6, Porcentaje=58),
                User(Nombre="GABRIEL RAMIREZ BAÑUELOS", Semestre=6, Porcentaje=64),
                User(Nombre="JOSELYN RAMIREZ LIMA", Semestre=6, Porcentaje=58),
                User(Nombre="GUILLERMO SANCHEZ ORTEGA", Semestre=7, Porcentaje=58),
                User(Nombre="NELSON SOSA FRANCISCO", Semestre=6, Porcentaje=58),
                User(Nombre="JULIAN TENAHUA OLAYA", Semestre=6, Porcentaje=58),
                User(Nombre="LUIS TORRALBA CEREZO", Semestre=6, Porcentaje=58),
                User(Nombre="AARON TORRES CORTE", Semestre=7, Porcentaje=64),
                User(Nombre="JOSUE TORRES ZAMORA", Semestre=6, Porcentaje=58),
                User(Nombre="ESMERALDA URBINA CINTO", Semestre=6, Porcentaje=58),
                User(Nombre="BRANDON VEGA RAMIREZ", Semestre=6, Porcentaje=64),
                User(Nombre="JONATHAN VERGARA NAVARRO", Semestre=6, Porcentaje=58),
                User(Nombre="KALTUM VIVEROS GOMEZ", Semestre=7, Porcentaje=58),
                User(Nombre="MARCO BARBOSA CABRERA", Semestre=6, Porcentaje=58),
                User(Nombre="LUIS CLEMENTE CRUZ", Semestre=7, Porcentaje=58),
                User(Nombre="JORGE DAMIAN COCONE RAMIREZ", Semestre=6, Porcentaje=58),
                User(Nombre="JOSE ANTONIO DANIEL JIMENEZ", Semestre=6, Porcentaje=58),
                User(Nombre="ALEJANDRO GARCIA CONTRERAS", Semestre=6, Porcentaje=52),
                User(Nombre="ERNESTO GONZALEZ LOZADA", Semestre=7, Porcentaje=58),
                User(Nombre="ARANTZA GORRAEZ REYES", Semestre=8, Porcentaje=58),
                User(Nombre="JOSUE GUZMAN LOPEZ", Semestre=6, Porcentaje=58),
                User(Nombre="ERIK LOPEZ ABUSTOS", Semestre=6, Porcentaje=58),
                User(Nombre="EVER LOPEZ RAMIREZ", Semestre=6, Porcentaje=58),
                User(Nombre="SOSTENES LUCAS SOSA", Semestre=6, Porcentaje=58),
                User(Nombre="MOISES MACHORRO PORTILLA", Semestre=7, Porcentaje=58),
                User(Nombre="DANIELA MANNY TOXQUI", Semestre=6, Porcentaje=58),
                User(Nombre="DIEGO ARMANDO MEJIA ARENAS", Semestre=6, Porcentaje=58),
                User(Nombre="VICTOR MENDOZA SAINZ", Semestre=6, Porcentaje=52),
                User(Nombre="CRISTIAN PULIDO HERNANDEZ", Semestre=6, Porcentaje=58),
                User(Nombre="ROCIO RAMIREZ FABIAN", Semestre=6, Porcentaje=58),
                User(Nombre="ALDO RAMIREZ JARILLO", Semestre=6, Porcentaje=52),
                User(Nombre="JOSE ARMANDO RAMOS RAMOS", Semestre=6, Porcentaje=58),
]


@app.get("/alumnos")
async def alumnos():
    return (alumnos_list)


@app.get("/alumnos/septimo_semestre", response_model=List[User])
async def alumnos_septimo_semestre():
    return [alumno for alumno in alumnos_list if alumno.Semestre == 7]


@app.get("/alumnos/porcentaje_academico", response_model=List[User])
async def porcentaje_mayor_60():
    return [alumno for alumno in alumnos_list if alumno.Porcentaje > 60]

#En el explorador colocamos la razis de la ip http://127.0.0.1:8000/usersclass


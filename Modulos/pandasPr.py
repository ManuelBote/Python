import pandas as pd

mydataset = {'cars':['BMW','Volvo','Ford'], 'prices':[60000,40000,20000]}
midataframe = pd.DataFrame(mydataset)
print(midataframe)

print()
print("==========================================================")
print()

a = [1,7,2]
miserie = pd.Series(a)
print(miserie)
print(miserie[0])

print()
print("==========================================================")
print()

b = [23,45,67]
miserie2 = pd.Series(b, index = ["x","y","z"])
print(miserie2)
print(miserie2["y"])

print()
print("==========================================================")
print()

diccionario = {"dia1": 420, "dia2": 380, "dia3": 390}
miserie3 = pd.Series(diccionario)
print(miserie3)

miserie3 = pd.Series(diccionario, index = ["dia1", "dia2"])
print(miserie3)

print()
print("==========================================================")
print()

dieta = pd.read_csv("Python\Modulos\data.csv")
print(dieta)

print()
print("==========================================================")
print()

dieta2 = pd.read_json("Python\Modulos\data.json")
print(dieta2.to_string())

print()
print("==========================================================")
print()


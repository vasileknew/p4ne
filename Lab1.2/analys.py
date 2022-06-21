from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook("data_analysis_lab.xlsx")
sheet = wb['Data']

def getvalue(x):
    return x.value

years = list(map(getvalue, sheet["A"][1:]))
temps = list(map(getvalue, sheet["C"][1:]))
acts = list(map(getvalue, sheet["D"][1:]))

pyplot.plot(years, temps, label="Температура")
pyplot.plot(years, acts, label="Активность")

pyplot.xlabel("Год")
pyplot.ylabel("Изменения")

pyplot.show()


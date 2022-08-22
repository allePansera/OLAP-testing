from __future__ import print_function
from cubes import Workspace, Cell, PointCut

# 1. Create a workspace
workspace = Workspace()
workspace.register_default_store("sql", url="sqlite:///data.sqlite")
workspace.import_model("model_data_fotografia.json")

# 2. Get a browser
browser = workspace.browser("irbd_fotografie")

# 3. Play with aggregates
result = browser.aggregate()

print("Total\n"
      "----------------------")

print("Record count : %8d" % result.summary["record_count"])
print("Voto avg : %8d" % result.summary["voto_avg"])



print("\nDrill Down by Fotografia (top-level Item hierarchy)\n==================================================")

result = browser.aggregate(drilldown=["item"])
print(("%-20s%-20s%10s%10s\n"+"-"*50) % ("Fotografia", "Des. Fotografia","Count", "Avg"))
for row in result.table_rows("item"):
    #print(row)
    print("%-20s%-20s%10d%10d" % ( row.record["item.id_fotografia"],row.record["item.fotografia"],row.record["record_count"],row.record["voto_avg"]))


print("\nDrill Down by Fotografo (middle-level Item hierarchy)\n==================================================")

result = browser.aggregate(drilldown=["item:fotografo"])
print(("%-20s%-20s%-20s%-30s%10s%10s\n"+"-"*150) % ("Fotografia", "Des. Fotografia","Fotografo","Des. Fotografo", "Count", "Avg"))
for row in result.table_rows("item"):
    #print(row)
    print("%-20s%-20s%-20s%-30s%10d%10d" % (  row.record["item.id_fotografia"],row.record["item.fotografia"],row.record["item.id_fotografo"],row.record["item.fotografo"],row.record["record_count"],row.record["voto_avg"]))


print("\nCut by Concorso & Year (bottom-level Item hierarchy)\n==================================================")
#concorso n.1 anno 2008
#mostro tutti i fotografi che partecipano a quel concorso
cuts = [PointCut("item", [1], hierarchy="reverse"),PointCut("year", [2008])]
cell = Cell(browser.cube, cuts = cuts)

result = browser.aggregate(cell, drilldown=["item@reverse:fotografo"])
print(("%-20s%-30s%10s\n"+"-"*50) % ("Fotografo","Des. Fotografo", "Voto Avg."))

for row in result.table_rows("item"):
	#print(row)
	print("%-20s%-30s%10d" % ( row.record["item.id_fotografo"],row.record["item.fotografo"],row.record["voto_avg"]))


#LA BASE DI DATI NON è CONSISTENTE IN QUANTO IL SOTTOLIVELLO NON E' UNA SPECIALIZZAZIONE DEL PRIMO LIVELLO
#QUINDI SERVIREBBE UNA BASE DI DATI DIVERSA

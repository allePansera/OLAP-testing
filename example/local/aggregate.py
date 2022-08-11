from __future__ import print_function
from cubes import Workspace, Cell, PointCut

# 1. Create a workspace
workspace = Workspace()
workspace.register_default_store("sql", url="sqlite:///data.sqlite")
workspace.import_model("model.json")

# 2. Get a browser
browser = workspace.browser("irbd_balance")

# 3. Play with aggregates
result = browser.aggregate()

print("Total\n"
      "----------------------")

print("Record count : %8d" % result.summary["record_count"])
print("Total amount : %8d" % result.summary["amount_sum"])
print("Double amount: %8d" % result.summary["double_amount_sum"])

#
# 4. Drill-down through a dimension
#

print("\n"
      "Drill Down by Sub-Category (top-level Item hierarchy)\n"
      "==================================================")
#
#STAMPA A LIVELLO 1 -> QUINDI CATEGORY
#result = browser.aggregate(drilldown=["item"])
#STAMPA A LIVELLO 2 -> QUINDI SUBCATEGORY
result = browser.aggregate(drilldown=["item:subcategory"])
#
print(("%-20s%10s%10s%10s\n"+"-"*50) % ("Sub - Category", "Count", "Total", "Double"))
#
#STAMPA DIRETTAMENTE LA LABEL -> PER VERIFICARE LA STRUTTURA CONSULTARE L'OUTPUT DI ROW
"""for row in result.table_rows("item"):
    print(row)
    print("%-20s%10d%10d%10d" % ( row.label,
                              row.record["record_count"],
                              row.record["amount_sum"],
                              row.record["double_amount_sum"])
                              )"""

for row in result.table_rows("item"):
    #print(row)
    print("%-20s%10d%10d%10d" % ( row.record["item.subcategory_label"],
                              row.record["record_count"],
                              row.record["amount_sum"],
                              row.record["double_amount_sum"])
                              )


print("\n"
      "Cell cuts by date (Drill - down by category & cuts by range in 2010)\n"
      "==================================================")
cut = PointCut("year", [2010]) #POTREI USARE UNA DATA E FILTRARE PER MESE O GIORNO
cell = Cell(browser.cube,[cut])
result = browser.aggregate(cell, drilldown=["item"])
print(("%-20s%10s%10s%10s\n"+"-"*50) % ("Category", "Count", "Total", "Double"))
for row in result.table_rows("item"):
    #print(row)
    print("%-20s%10d%10d%10d" % ( row.label,
                              row.record["record_count"],
                              row.record["amount_sum"],
                              row.record["double_amount_sum"])
                              )

print("\n"
      "Slice where Category = Equity (code e)\n"
      "==================================================")

cut = PointCut("item", ["e"])
cell = Cell(browser.cube, cuts = [cut])

result = browser.aggregate(cell, drilldown=["item"])

print(("%-20s%10s%10s%10s\n"+"-"*50) % ("Sub-category", "Count", "Total", "Double"))

for row in result.table_rows("item"):
    print("%-20s%10d%10d%10d" % ( row.label,
                              row.record["record_count"],
                              row.record["amount_sum"],
                              row.record["double_amount_sum"],
                              ))

#test di uno slice per sotto categoria
#row.record["item.subcategory_label"]

print("\n"
      "Slice where Sub-Category = (code 'cs' and year 2009)\n"
      "==================================================")

#cuts = [PointCut("item", ["e","cs"]),PointCut("item", ["a","rcv"])]
cuts = [PointCut("item", ["e","cs"]),PointCut("year", [2009])]
cell = Cell(browser.cube, cuts = cuts)

result = browser.aggregate(cell, drilldown=["item"])

print(("%-20s%10s%10s%10s\n"+"-"*50) % ("Sub-category", "Count", "Total", "Double"))

for row in result.table_rows("item"):
    print("%-20s%10d%10d%10d" % ( row.record["item.subcategory_label"],
                              row.record["record_count"],
                              row.record["amount_sum"],
                              row.record["double_amount_sum"],
                              ))

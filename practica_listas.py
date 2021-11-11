cochesLista=["FORD", "RENAULT", "FERRARI", "VOLVO", "FIAT", "BUGATTI",
"BMW", "AUDI", "SEAT", "CITRÖEN", "ACURA", "MG"]

cochesLista.append("ROVER")
cochesLista.insert(0,"AUSTIN")
cochesLista.extend(["PIAGGIO","CHEVROLET","LAMBORGINI"])

cochesLista.remove("PIAGGIO")

print(cochesLista.index("FORD"))
print(cochesLista[:9])
print("AUDI" in cochesLista)
print("cochesLista[:]")
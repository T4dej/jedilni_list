#-*- coding: utf-8 -*-

print("Danes vam v pomoč pri sestavi menuja.")

menu = {}

datoteka = open("menu.txt", "w+")
datoteka.write("Današnji meni: \n")

while True:
    jed = raw_input("Vnesite jed: ")
    datoteka.write("- " + jed + " ")
    cena = raw_input("Vnesite ceno za '%s': "%jed)
    cena = str(cena)
    datoteka.write(cena + " €\n")
    menu[jed] = cena

    odg = raw_input("Želite vnestni naslednjo jed? (da/ne)")
    if odg != "da":
        break

print("Izpis dnevnega menija v datoteki: ")

datoteka.close()
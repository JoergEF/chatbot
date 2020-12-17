#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ein einfacher ChatBot
# (c) 2020 by me, Lizenz GPLv3

import random

# zufällige Antworten
zufallsantworten = ["Oh wirklich...", "Interessant", "Das kann man so sehen.", "Ich verstehe..."]

# Stopwörter
reaktionen = {"hallo": "aber hallo",
              "geht": "Was verstehst Du darunter",
              "schmeckt": "Ich habe keinen Geschmackssinn"}

# Ausgabe Head..
print("Willkommen beim ChatBot (v1)")
print("Worüber wollen Sie sprechen")
print("Zum Beenden geben Sie bye ein...")
print("")

# main
nutzereingabe = ""
while nutzereingabe != "bye":
    nutzereingabe = ""
    while nutzereingabe == "":
        nutzereingabe = input("Ihre Frage oder Antwort: ")
    nutzereingabe = nutzereingabe.lower()
    nutzerwoerter = nutzereingabe.split()

    intelligentAntworten = False
    for einzelwoerter in nutzerwoerter:
        if einzelwoerter in reaktionen:
            print(reaktionen[einzelwoerter])
            intelligentAntworten = True
    if not intelligentAntworten:
        print(random.choice(zufallsantworten))
print("einen schönen Tag.")

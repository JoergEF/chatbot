#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ein einfacher ChatBot
# (c) 2020 by me, Lizenz GPLv3

import random
zufallsantworten = ["Oh wirklich...", "Interessant", "Das kann man so sehen.", "Ich verstehe..."]

print("Willkommen beim ChatBot (v1)")
print("Worüber wollen Sie sprechen")
print("Zum Beenden geben Sie bye ein...")
print("")

nutzereingabe = ""
while nutzereingabe != "bye":
    nutzereingabe = ""
    nutzereingabe = input("Ihre Frage oder Antwort: ")
    print(random.choice(zufallsantworten))
print("einen schönen Tag.")

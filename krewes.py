# Ari Schechter, Dragos Lup and Jessica Yeung (Team Ohala)
# Soft Dev
# K06: Learnination Through Amalgamation
# 2020-10-02

import random
KREWES = {
    'orpheus': ['ERIC', 'SAUVE', 'JONATHAN', 'PAK', 'LIAM', 'WINNIE', 'KELLY', 'JEFFREY', 'KARL', 'ISHITA', 'VICTORIA', 'BENJAMIN', 'ARIB', 'AMELIA', 'CONSTANCE', 'IAN'],
    'rex': ['ANYA', 'DUB-Y', 'JESSICA', 'ALVIN', 'HELENA', 'MICHELLE', 'SHENKER', 'ARI', 'STELLA', 'RENEE', 'MADELYN', 'MAC', 'RYAN', 'DRAGOS'],
    'endymion': ['JASON', 'DEAN', 'MADDY', 'SAQIF', 'CINDY', 'YI LING', 'RUOSHUI', 'FB', 'MATTHEW', 'MAY', 'ERIN', 'MEIRU']
}
#Final version, first takes just the values from KREWES (the three lists), and turns that into a list.
#Then it randomly chooses between the three lists, and then it randomly chooses between all the values in the list.
print(random.choice(random.choice(list(KREWES.values()))))

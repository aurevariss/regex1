import re

lpp = open("le ptit prince.txt", "r", encoding="utf-8")
text_lpp = lpp.read()
text_lpp = text_lpp.lower()

masculins_back = []
masculins = []
masculins_pronoms_adj = []
masculins_back.extend(re.findall(r"\ble\s\w+|\bdu\s\w+|\bau\s\w+|\bun\s\w+", text_lpp))
masculins_pronoms_adj.extend(re.findall(r"\b(?:m|t|s)on\s\w+|(?:n|v)otre\s\w+|leur\s\w+", text_lpp)).extend(re.findall(r"petit\sw+|vieux\s\w+|grand\sw+|ancien\s\w+|nouveau\s\w+|nouvel\s\w+", text_lpp))
masculins_back = list(dict.fromkeys(masculins_back))
masc_pronoms_adj = list(dict.fromkeys(masc_plus_adj))

for i in masculins_back:
    j = i[3:]
    masculins.append(j)

masculins = list(dict.fromkeys(masculins))
masculins.extend(masc_pronoms_adj)
print(masculins)

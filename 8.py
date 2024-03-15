import re

lpp = open("le ptit prince.txt", "r", encoding="utf-8")
text_lpp = lpp.read()
text_lpp = text_lpp.lower()

masculins_back = []
masculins = []
masculins_pronoms_adj = []
masculins_back.extend(re.findall(r"\ble\s\w+|\bdu\s\w+|\bau\s\w+|\bun\s\w+", text_lpp))
masculins_pronoms_adj.extend(re.findall(r"\b(?:m|t|s)on\s\w+|(?:n|v)otre\s\w+|leur\s\w+", text_lpp))
masculins_pronoms_adj.extend(re.findall(r"petit\sw+|vieux\s\w+|grand\sw+|ancien\s\w+|nouveau\s\w+|nouvel\s\w+|premier\s\w+", text_lpp))
masculins_back = list(dict.fromkeys(masculins_back))
masculins_pronoms_adj = list(dict.fromkeys(masculins_pronoms_adj))

for i in masculins_back:
    j = i[3:]
    masculins.append(j)

masculins = list(dict.fromkeys(masculins))
print(masculins)
print(masculins_pronoms_adj)

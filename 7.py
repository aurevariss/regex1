import re

def remover (lst_part, lst_all):
    for j in lst_part:
        if j in lst_all:
            lst_all.remove(j)
    return lst_all

lpp = open("le ptit prince.txt", "r", encoding="utf-8")
text_lpp = lpp.read()

all_capitals = []
list_of_common_words = ["Elles", "Voilà", "Aussi", "Quand", "Pourquoi", "Chapitre", "Comme", "Ainsi", "Combien", "Pardon", "Alors", "Lorsque", "Ensuite", "Comment", "Celui", "Celle", "Quelle", "Quels", "Quel", "Quant", "Bonjour", "Cette"]

all_capitals.extend(re.findall(r"[A-Z]\w{4,}\s?-?[A-Z]\w+|[A-Z]\w{4,}", text_lpp))
all_capitals = list(dict.fromkeys(all_capitals))
not_names = []

for i in all_capitals:
    if re.search(r"\w+ez", i) or re.search(r"\w+ment", i) or re.search(r"\w+ons", i) or re.search(r"\w+iens", i):
        not_names.append(i)

all_capitals = remover(not_names, all_capitals)
all_capitals = remover(list_of_common_words, all_capitals)

print(all_capitals)

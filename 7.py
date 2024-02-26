import re

lpp = open("le ptit prince.txt", "r", encoding="utf-8")
text_lpp = lpp.read()

all_capitals = []
list_of_common_words = ["Elles", "Voilà", "Aussi", "Quand", "Pourquoi", "Chapitre", "Comme", "Ainsi", "Combien", "Pardon", "Alors", "Lorsque", "Ensuite", "Comment", "Celui", "Celle", "Quelle", "Quels", "Quel", "Quant", "Bonjour", "Cette"]

all_capitals.extend(re.findall(r"[A-Z]\w{4,}\s?-?[A-Z]\w+|[A-Z]\w{4,}", text_lpp))
all_capitals = list(dict.fromkeys(all_capitals))

for i in all_capitals:
    if re.search(r"\w+ez", i) or re.search(r"\w+ment", i) or re.search(r"\w+ons", i) or re.search(r"\w+iens", i):
        all_capitals.remove(i)

for j in list_of_common_words:
    if j in all_capitals:
        all_capitals.remove(j)

print(all_capitals)

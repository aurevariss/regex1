import re

string_1 = "ai, as, a, avons, avez, ont, aie, aies, ait, ayons, ayez, aient, avais, avais, avait, avions, aviez, avaient, aurai, auras, aura, aurons, aurez, auront, aurais, aurais, aurait, aurions, auriez, auraient, eus, eus, eut, eûmes, eûtes, eurent, eusse, eusses, eut, eussions, eussiez, eussent"

result1 = re.findall(r"\b(a|ont)\b", string_1)
result2 = re.findall(r"\b[ai|av|ay|aur]\w+?\b", string_1)

print(result1, result2)
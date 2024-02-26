import re

words = "avec, Âge, à, âne, Alors, À"
result = re.findall(r"[aàâAÂÀ]", words)

print(result)
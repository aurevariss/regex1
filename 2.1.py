import re

string = "foot - feet, goose - geese, tooth - teeth, man - men"
result = re.findall(r"\b(\w+e\w+)\b", string)

print(result)
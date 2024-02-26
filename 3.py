import re

regexp = re.compile(r"(.)\1")
data = ["странный", "апелляция", "верно", "профессор", "союз", "эффект", "сольный", "фарватер"]

for str in data:
    match = re.search(regexp, str)
    if match:
        print(str, end=" ")
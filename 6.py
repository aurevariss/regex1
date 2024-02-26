import re


def change(str):
    str = re.sub(r"[-! ]", "", str)
    return str


str1 = "perro-"
str2 = "gato"
str3 = "caballo"
str4 = "pájaro!"
str5 = " "
str6 = "tiburón"
str7 = "león"
line = [str1, str2, str3, str4, str5, str6, str7]
new_line = ""
new_list = []

for i in line:
    if i != " ":
        i = change(i)
        new_list.append(i)

new_line = ", ".join(new_list)
print(new_line)
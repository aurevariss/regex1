import re

def spaceremover (str):
    str = " ".join(str.split())
    return str

str1 = "Le cinqui$me jour     , toujours"
str2 = "gr&ce au mouton ,    ce sec- ret de la vie du petit prince"
str3 = "me fut r?v??  . Il me demanda avec brus- querie, sans pr?ambule ,  comme le fruit        d’un probl$me"
str4 = "long- temps m?dit? en silence :"
text = [str1, str2, str3, str4]
new_line = ""

for i in text:
    i = spaceremover(i) + " "
    i = i.replace("$", "è").replace("?", "é").replace("&", "â").replace("- ", "")
    i = re.sub(r'\s([?.!",:;](?:\s|$))', r'\1', i)
    new_line += i
print(new_line)


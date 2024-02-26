import re

string = "kitab (книга), kutub (книги), rasūl (посланник), rusul (посланники), sabīl (путь), subul (пути), ʾasās (основание), 'usus (основания)"
result = re.findall(r".u\w+\b", string)

print(result)
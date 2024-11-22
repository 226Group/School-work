import re

#from re import *

# email = r"\b\w+@\w+\.com\b"
email = re.compile(r"\b\w+@\w+\.com\b")
print (f"email {email.search('group mail kitgroup126@gmail.com. Goodbye')}")


# print (re.findall (r"\d+(\.\d+)", '8800, 555 3 5 3 5, лучше позвонить чем 0.05 занимать!'))
numbers = re.compile(r"\d+|\d*\.\d+")
print (f"numbers {numbers.findall('8800, 555 3 5 3 5, лучше позвонить чем .05 занимать!')}")

words = re.compile("[А-Я][а-я]+")
print (f"words {words.findall('Истоки регулярных выражений лежат в теории автоматов, теории формальных языков и классификации формальных грамматик по Хомскому[3].')}")




"""
var_name = r"[\\w-]"
# var_name = r"[A-Z0-9][A-Z0-9_-]*"   
protocol = r"(http|https|ftp):\\/\\/"
def intersperse (sep, word):
    return f"{word}({sep}{word})*"

url = re.compile(r"((http|https|ftp):\\/\\/)?([A-Z0-9][A-Z0-9_-]*)(\\.[A-Z0-9][A-Z0-9_-]*)+")
url = re.compile(protocol+"?" + intersperse (r"\\.", var_name))

print (f"url {url.findall('Я пишу этот код на онлайн компиляторе https://www.online-python.com/')}")




print ("\n\n\n")
match = re.search(r'\\d\\d\\D\\d\\d', r'Телефон 123-12-12') 
print(match[0] if match else 'Not found') 
# -> 23-12 
match = re.search(r'\\d\\d\\D\\d\\d', r'Телефон 1231212') 
print(match[0] if match else 'Not found') 
# -> Not found 

match = re.fullmatch(r'\\d\\d\\D\\d\\d', r'12-12') 
print('YES' if match else 'NO') 
# -> YES 
match = re.fullmatch(r'\\d\\d\\D\\d\\d', r'Т. 12-12') 
print('YES' if match else 'NO') 
# -> NO 

print(re.split(r'\\W+', 'Где, скажите мне, мои очки??!')) 
# -> ['Где', 'скажите', 'мне', 'мои', 'очки', ''] 

print(re.findall(r'\\d\\d\\.\\d\\d\\.\\d{4}', 
                 r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017')) 
# -> ['19.01.2018', '01.09.2017'] 

for m in re.finditer(r'\\d\\d\\.\\d\\d\\.\\d{4}', r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017'): 
    print('Дата', m[0], 'начинается с позиции', m.start()) 
# -> Дата 19.01.2018 начинается с позиции 20 
# -> Дата 01.09.2017 начинается с позиции 45 

print(re.sub(r'\\d\\d\\.\\d\\d\\.\\d{4}', 
             r'DD.MM.YYYY', 
             r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017')) 
# -> Эта строка написана DD.MM.YYYY, а могла бы и DD.MM.YYYY 
"""
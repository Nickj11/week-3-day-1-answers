import re

string = """
Hawkins, Derek	derek@codingtemple.com	(555) 555-5555	Teacher, Coding Temple	@derekhawkins"""



pattern = re.compile('(?P<first>[A-Z][a-z-A-Z]+), (?P<last>[A-Z][a-z-A-Z-]+)(?P<op>[\w\W]+)(?P<twitter>@[a-z]+)')


matches = pattern.finditer(string)

with open('names.txt' , 'r' ) as f:
        contents = f.read()
    
        matches = pattern.finditer(contents)

for match in matches:
    print(match.group("first"))
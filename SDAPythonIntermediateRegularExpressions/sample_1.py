import re

pattern = '.la'
text = 'my name is bla also bla'

result = re.search(pattern, text)

print(result)
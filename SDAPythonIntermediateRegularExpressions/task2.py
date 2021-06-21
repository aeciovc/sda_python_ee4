import re

pattern = '[\w\.]+@gmail.com'
text = input("Type your email:")

result = re.fullmatch(pattern, text)

print(result is not None)

# aecio.costa@gmail.com              - True
# my email is aecio.costa@gmail.com  - False
# aecio.costa@mac.com                - False


import re

email = 'my email is aecio.costa@gmail.com'

print(re.search(r"[A-Z]la", "Ela"))
print(re.fullmatch(r"[A-Z]la", "Ela"))

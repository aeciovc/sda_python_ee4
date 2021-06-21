
# Write a python program that is able to identify first and last names in a text.
# Aecio Costa  - True
# John Doe     - True
# Maria Julia  - True

"""
Aecio Costa is a Software developer, John Doe is his friend. His sister calls Maria Julia.
"""

import re

pattern = '([A-Z][a-z]+)\s([A-Z][a-z]+)'
text = 'Aecio Costa is a Software developer, John Doe is his friend. His sister calls Maria Julia.'

#full_names = re.findall(pattern, text)
#print("Full names ", full_names)
#print("First names", [n[0] for n in full_names])
#print("Last names", [n[1] for n in full_names])

full_names = re.finditer(pattern, text)
for name in full_names:
    name.groups()
import re

print(re.findall(r".la", "Ola ala Ela alaalaala"))

print(re.split(r",|\.", "apple,pear,grapes,carrot.cabbage,veggies.fruit,yard"))
print(re.findall(r",|\.", "apple,pear,grapes,carrot.cabbage,veggies.fruit,yard"))
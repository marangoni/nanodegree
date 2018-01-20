# Problem 01 - random Lists
# Utilizar o while para popular uma lista com 20 elementos aleatrios

import random

random_list = []
list_length = 20
i=0
while len(random_list) < list_length:
    random_list.append(random.randint(0,10))
    
print random_list

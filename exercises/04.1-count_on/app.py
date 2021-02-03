import re

my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]


#your code go here:
#list, dic

#new_list = [type(x) == "towel" for x in my_list]
new_list = [i for i, n in my_list if str(type(n)) == "*list*"]

print(new_list)

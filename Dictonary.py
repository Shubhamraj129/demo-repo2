# Dictonary is nothing but key and value pair

di={'fruit':"apple,babana,orange",'color':'red ,yellow,black,white'}
print(di)
print(di['color'])## to print the specific data into the using key
di['newcolor']='Orange,green'  ## To add the new key and value into the dictionary
di.update({"number":'1,2,3,4'})  # Using UPDATE o add the new key and value into the dictionary
print(di)
del di['newcolor']  ## To the delete a specific keys and values
print(di)
## Functions

d2=di.copy()  ## copy the all data into the d2  if you chANGE INTO d2 not apply in di
print(d2)
print(di.keys())   ## It pRINTS ALL KEYS IN THE DICTIONARY
print(di.items())    ## It pRINTS aLL IN THE DICTIONARY

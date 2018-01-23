

world={'Afghanistan': 30.55, 'Albania':2.81, 'Algeria':39.21

>>> world['Sealand']=.00027
>>> world
{'Algeria': 39.21, 'Albania': 2.81, 'Afghanistan': 30.55, 'Sealand': 0.00027}
>>> 

>>> world.keys()
dict_keys(['Algeria', 'Albania', 'Afghanistan', 'Sealand'])
>>> 

>>> world.items()
dict_items([('Algeria', 39.21), ('Albania', 2.81), ('Afghanistan', 30.55), ('Sealand', 0.00027)])
>>> 

>>> world.values()
dict_values([39.21, 2.81, 30.55, 0.00027])

del(world['Sealand'])




europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe

europe['italy'] = 'rome'
# Print out italy in europe

print('italy' in europe)
# Add poland to europe

europe['poland'] = 'warsaw'
# Print europe
print(europe)

europe['australia'] = 'vienna'

>>> europe
{'spain': 'madrid', 'norway': 'oslo', 'australia': 'vienna', 'italy': 'rome', 'france': 'paris', 'poland': 'warsaw', 'germany': 'berlin'}



# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
>>> europe['france']['capital']
'paris'
>>> 

# Create sub-dictionary data

data = { 'capital':'rome', 'population':59.83 } 
# Add data to europe under key 'italy'
europe['italy']=data

# Print europe

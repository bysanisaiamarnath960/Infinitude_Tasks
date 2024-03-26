dict={"bike":"yamaha","car":"tata","boat":"ship1","plane":"airway","train":"indian railways"}

print("The keys of the Dictionary is: ",dict.keys())
print("The values of the Dictionary is: ",dict.values())

dict.pop("train")
print(dict)

dict["car"]="benz"
print(dict)

print("The Dictionary keys is converted to list: ",list(dict.keys()))
print("The Dictionary values is converted to list: : ",list(dict.values()))



pets=['sheru','ogggy','galahad']
print("Enter the pet name:")
name = input()
if name not in pets:
    print(" I donot have a pet named "+name)
else:
    print(name+" is my pet.")
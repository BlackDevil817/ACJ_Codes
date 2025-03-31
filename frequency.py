import pprint
message = "My name is atharva joshi"
count={}
for i in message:
    count.setdefault(i,0)
    count[i]=count[i]+1

pprint.pprint(count)
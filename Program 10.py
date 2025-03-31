C=[]
d={}
content = "red black red grey green black red"
c=content.split()
print(c)
for i in c:
    count=0
    for j in c:
        if i==j:
            count+=1
    d[i]=count
sortd=sorted(d.items(),key=lambda x:x[1],reverse=True)
print(sortd[0:10])
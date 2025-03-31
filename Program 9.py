ifile=open('s.txt')
w1=[]
w2=[]
for line in ifile:
    w=line.split()
    w2.append(w)
for item in w2:
    w1.append(item)
w1.sort()
print(w1)
ofile=open('sa.txt','w')
for item in w1:
    item=str(item)
    ofile.write(item)
ofile.close
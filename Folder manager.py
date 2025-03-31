import os
for a,b,c in os.walk('.'):
    print('Current folder is:' + a)
for i in b:
    print('Subfolders of '+a+ ':' + i)
for j in c:
    print('Files inside '+a+ ':' + j)
print('')
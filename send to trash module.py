import send2trash
a=open('b.txt','a')
a.write('Hello world!') 
a.close()
send2trash.send2trash('b.txt')

print("Starting cmd ...")
f = open('catch.txt', 'r')
string = f.read()
#print(string)
f. close()
string = string.replace("cmd=0", "cmd=1")
#print(string)
f = open('catch.txt', 'w')
f.write(string)
f. close()
print("Finished cmd.")
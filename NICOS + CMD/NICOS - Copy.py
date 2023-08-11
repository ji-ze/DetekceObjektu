print("Starting NICOS ...")
f = open('catch.txt', 'r')
string = f.read()
f. close()
#print(string)
string = string.replace("nicos=0", "nicos=1")
f = open('catch.txt', 'w')
f.write(string)
#print(string)
f. close()
print("Wait for cmd ...")

while True:
    f = open('catch.txt', 'r')
    value = f.read()
    #print(value)
    try:
        if value[4] == "0":
            f.close()
            print("OK")
        else:
            print("cmd complete ...")
            f.close()
            break
    except:
        continue
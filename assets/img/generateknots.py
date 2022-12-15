f = open("demofile2.txt", "a")
buchstabe = "b"
bilder = 28
knoten = "4"
begin = 107
for x in range(bilder):
    y = str(x+1)
    first = str(x+1 + begin) 
    if x < 9:
        y= "0" + str(x+1)
    string = '''.slide-{first}-knot-{knoten} {{
    background: url('../assets/img/knoten{knoten}/{buchstabe}/{y}.jpg');
    }}
    '''.format(first= first, knoten = knoten,buchstabe=buchstabe, y= y)
    print(string)
    f.write(string)

f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
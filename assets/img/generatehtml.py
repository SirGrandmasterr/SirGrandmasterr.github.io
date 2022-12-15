f = open("demohtml.txt", "a")
folien=135
knoten="4"
for x in range(folien):
    string = '''<div class="slide slide-{first}-knot-{knoten}">
        </div>
    '''.format(first= str(x+1), knoten = "2")
    print(string)
    f.write(string)

f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
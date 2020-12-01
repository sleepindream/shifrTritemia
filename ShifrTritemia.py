def key(number):
    return 4*number+9
f=open('text.txt')
text=f.read()
text=text.replace(' ', '')
text=text.replace('\n', '')
text=text.lower()
alphabet="abcdefghijklmnopqrstuvwxyz";
chifrtext=''
for i in range(len(text)):
     chifrtext+=alphabet[key(alphabet.index(text[i]))%len(alphabet)]
print(chifrtext)
d=open("code.txt","w")
d.write(chifrtext)
f.close()
d.close()

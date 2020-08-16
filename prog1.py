# Problem statement : WAP to print the below string in desired below output:
#i/p : "abc xyz "Rutuja Joshi" jhg "Atharva Joshi" kjh"
#o/p:   abc
#        xyz
#        "Rutuja Joshi"
#        jhg
#        "Atharva Joshi"
#        kjh

ipstr='xyz abc fgh "jigisha joshi" "mugdha joshi" cfd gft "Rutuja joshi" mm "Atharva Joshi"'
a=ipstr.split(' ')
str2 = []
print(a)
for i in range(len(a)):
    if a[i].startswith('"'):
        str2.append(a[i]+' '+a[i+1])
    elif a[i].endswith('"'):
        pass
    else:
        str2.append(a[i])
print(str2)
for i in str2:
    print(i)
    print("\n")


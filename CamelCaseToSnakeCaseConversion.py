#i/p: HakerEarth
#O/p : haker_earth


ipstr= "HakerEarth"
str2=ipstr[0].lower()

for i in range(1,len(ipstr)):
    
    if(ipstr[i].isupper()):
        str2 +="_"+ipstr[i].lower()
    else:
        str2 += ipstr[i]
print(str2)


HakerEarth
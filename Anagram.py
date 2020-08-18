#WAP to accept 2 nos and return True / False acoordingly after checking if they are anagram
def Anagram(input1,input2):
    temp={}
    if(len(input1)!=len(input2)):
        return False
    for i in range(len(input1)):
        if input1[i] in temp:
            temp[input1[i]]+=1
        else:
            temp[input1[i]]=1
    for i in range(len(input2)):
        if input2[i] in temp:
            temp[input2[i]]-=1
        else:
            temp[input2[i]]=1
    for i in temp.values():
        if i==1:
            return False
    return True

def main():
    print(Anagram("7427","4277"))

if __name__ == "__main__":
    main()
        


     


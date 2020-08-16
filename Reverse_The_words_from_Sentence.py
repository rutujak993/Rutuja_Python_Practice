def SentenceConversion(sentence):
    l1 = sentence.split(' ')
    for i in range(0,len(l1)):   
        l1[i] = l1[i][::-1] 
    return ' '.join(l1)
            

def main():

    String1 = input("Enter a sentance : ")
    print(SentenceConversion(String1))

if __name__=="__main__":
    main()



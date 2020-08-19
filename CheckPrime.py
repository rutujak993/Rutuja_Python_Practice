#WAP to check if the given number is a prime number

def checkPrime(inputnum):
    flag=0
    for i in range(2,inputnum):
        if inputnum%i == 0:
            flag=1
    if flag == 1:
        return False
    else:
        return True
def main():
    inputNum = int(input("Please enter a number: "))
    print(checkPrime(inputNum))

if __name__ == "__main__":
    main()

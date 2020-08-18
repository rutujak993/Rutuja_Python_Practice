#WAP to check whether the given number is a perfect square

def CalculateSqrt(sqr, index):
    if index*index == sqr:
        return index
    elif index*index > sqr:
        return 0
    else:
        return CalculateSqrt(sqr, index+1)

def main():
    inputNum = int(input("Please enter a number: "))
    sqrt = CalculateSqrt(inputNum, 0)
    if sqrt == 0:
        print("Number is not perfect square!")
    else:
        print("Square root is : {0}".format(sqrt))
    
if __name__ == "__main__":
    main()
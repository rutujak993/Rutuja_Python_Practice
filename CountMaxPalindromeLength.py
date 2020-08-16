# WAP to return the max length of a word which is a palindrome from a sentence.

def MaxLenPalindrome(inputStr):
    maxLen = 0
    lstInput = inputStr.split(' ')

    for i in lstInput:
        if i == i[::-1]:
            if len(i) > maxLen:
                maxLen = len(i)
        else:
            pass

    return maxLen

def main():
    inputStr = input("Enter a sentence: ")
    print(MaxLenPalindrome(inputStr))

if __name__ == "__main__":
    main()
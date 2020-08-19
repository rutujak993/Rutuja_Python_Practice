#WAP to print the below pattern
# * * * *
#   * * *
#     * * 
#       *


def printPattern(n):

    for i in range(n):
        for j in range(n):
            if j>=i:
                print('* ',end='')
            else:
                print('  ',end='')
        print("\n")

def main():
    printPattern(4)

if __name__ == "__main__":
    main()
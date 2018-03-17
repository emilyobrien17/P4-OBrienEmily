def testGetCoin():
    # define total to be zero to start with
    total = 0
    # user enters change in a comma delimited format. e.g. n,n,q,d
    userInput = eval(input("Enter your change:  "))
    # Store the input length to be used in the for loop
    length = len(userInput)
    # Loop over each input and add it to total
    for i in range(0, length):
        total += userInput[i]
    # Divide total by 100 to get the correct value of all the coins
    total /= 100
    return total

def main():
    # Print result with 2 decimal places so it looks like real money
    print("$", "%.2f" % testGetCoin())

main()
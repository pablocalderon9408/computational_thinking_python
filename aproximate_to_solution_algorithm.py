def aproximate_to_solution():
    number = int(input("Please enter a number to calculate its square root: " + "\n" + "\n"))
    ERROR = 0.01
    result = 0
    paso = ERROR ** 2

    while abs(result**2-number) >= ERROR and result<number:
        print(result**2-number, result)
        result += paso

    print("The square root of {number} is {result}".format(number=number, result=result))

if __name__=="__main__":
    aproximate_to_solution()

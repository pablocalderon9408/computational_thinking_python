def exhaustive_search_algorithm():
    """ Calculate the square root to a number given by the user"""
    answer = 0
    try:
        number = int(input("Please enter a number to check if it has an exact square root: " + "\n"))
    except:
        pass

    while answer ** 2 < number:
        answer += 1

    if answer ** 2 == number:
        print("The number has an exact square root and it is: {answer}".format(answer=answer))
    else:
        print("The number {number} has not an exact square root.".format(number=number))
    
if __name__ == "__main__":
    exhaustive_search_algorithm()

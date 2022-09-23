# Taken From
# Iterating Over Data
# Problem-Set While Loops #11
def silly_sum():
    """ reads numbers from the user (use input_int) 
        summing as we go until either
        the user enters 0, or
        the sum reaches or exceeds 1000
    """
    num = int(input("Please enter a number => "))
    total = 0

    while num != 0:
        total += num
        if total >= 1000:
            break
        num = int(input("Please enter a number => "))

    return total



if __name__ == "__main__":
    print(f"Answer = {silly_sum()}")

def is_prime_number(n) -> bool:
    """
    prime number determination function
    :param n: positive integer
    :return: Returns True if it is a prime number, and returns False if it is not a prime number.
    """

    #is_prime_number = True
    if k<2:
        #is_prime_number = False
        return False
    else:
        i=2
        while i * i <= k:
            if k%i == 0:
                #is_prime_number = False
                #break
                return False
            i = i+1
        return True

def power(b, e) -> int:
    """

    :param b: base number
    :param e: exponent number
    :return: power result value
    """

while True:
    menu = input("1) prime number 2) power 3) divmod 4)quit")
    if menu=='1':
        start, end = list(map(int, input("Input start & end number: ").split()))
    for k in range(start, end+1):
        if is_prime_number(k): print(k, end=' ')
        elif menu=='2':
            base, exponent = map(int, input("Input base & exponent number: ").split())
            print(f"{base}^{exponent} = {base ** exponent}")  # operator
        elif menu=='3':
            print(f"{dividend}//{divisor} = {divmod(dividend,divisor)[0]}")
            print(f"{dividend}//{divisor} = {divmod(dividend, divisor)[1]}")
        elif menu =='4':
            print("exit program...")
        break

    else:
        print("Please choose from the menu")






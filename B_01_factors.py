def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration}")


# Display instructions

def instructions():
    statement_generator("instructions", "-")

    print('''
To use this program, simply enter an integer between 
1 and 200 (inclusive). The program will show the factors of 
your chosen integer.

It will also tell you if your chosen number ...
- is unity (1) as it only has one factor
- is a prime number (i.e. it has two factors)
- is a perfect square

To exit the program, please type 'xxx' 
    ''')


# Ask the user for an integer between 1 and 200.
def num_check(question):

        error = "Please a number that is between 1 and 200 inclusive\n"
        while True:

            response = input(question). lower()
            if response == "xxx":
                return response


            try:
                # ask the user for a number
                response = int(response)


                # check that the number is more than zero

                if 1 <= response <= 200:
                    return response
                else:
                    print(error)


            except ValueError :
                print(error)


# Works out factors, returns sorted list
def factor(to_factor):
    factors_list =[]

    # square root the number to work out when to stop looping.
    stop = to_factor ** 0.5
    stop = int(stop)

    for item in range(1, stop +1):

        # if modulo is zero, then the number is a factor
        if to_factor % item ==0:
            # Add first factor to list
            factors_list.append(item)

            # find second factor by dividing ' to factor ' by the first factor
            partner = to_factor // item

            # check second factor is not on list and add it
            if partner not in factors_list:
                factors_list.append(partner)
    # output
    factors_list.sort()
    return factors_list


# Main Routine Goes Here
# Heading
statement_generator("The ultimate Factor Finder", "*")

# Display instructions if user has not used the program before
want_instructions = input("press<enter> to read the instructions or any key to continue")

if want_instructions == "":
    instructions()

while True:

    comment = ""

    # ask user for number to be factorised...
    to_factor = num_check("\nEnter an integer (or xxx to quit):" )

    if to_factor == "xxx":
        break

    # Get factors for integers that are 2 or more
    elif to_factor != 1:
        factor_list = 'get_factors(to_factor)'

    # set up comment for unity
    else:
        all_factors = ""
        comment = "One is UNITY! It only has one factor. Itself :)"
        factor_list = ""

    # comments for squares / primes

    # prime numbers have only two factors
    if len (factor_list) == 2:
        comment = "{} is a prime number. "".format(to_factor)"

    # check if the list has an odd number of factors
    elif len(factor_list) % 2 ==1:
        comment = "{} is a perfect square".format(to_factor)
    # output factors and comment
    if to_factor >1:
        heading = f"Factors of {to_factor}"
    else:
        heading = "one is special..."

    # output factors and comment
    print()
    statement_generator(heading, "*")
    print(factor_list)
    print(comment)

print("Thank you for using the factors calculators")
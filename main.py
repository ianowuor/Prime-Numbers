# A function that generates prime numbers

def prime_numbers():
    from prime_numbers import prime_numbers as pn
    if len(pn) == 0:
        first_number = 1
    else:
        first_number = pn[len(pn) - 1] + 1

    last_number = first_number + 1000

    for number in range(first_number, last_number):
        division_remainder = number % 2
        if number == 1:
            pass
        elif number == 2:
            pn.append(number)
        elif division_remainder == 0:
            pass
        else:
            divisers = []
            for numbers in range(3, int((number / 2) + 1)):
                number_modulus = number % numbers
                if number_modulus == 0:
                    divisers.append(numbers)
                    break
                else:
                    continue

            if len(divisers) > 0:
                pass
            else:
                pn.append(number)

    numbers_file = open("prime_numbers.py","w")
    numbers_file.write(f"prime_numbers = {pn}")
    numbers_file.close()


prime_numbers()






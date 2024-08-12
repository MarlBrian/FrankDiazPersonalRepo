import re

def is_interesting(number, awesome_phrases):
    # Regex scenarios: [0] 1 digit then zeroes. [1] same number, note the backlash 1, which matches the same text as
    # most recently matched by the 1st capturing group.

    regex_cases = ('^[1-9][0]+$', '^(\d)\1+$')

    def mileage_near_numbers(number):
        number = int(number)
        return (number, number + 1, number + 2)

    def one_or_two(test, number):
        if test == number:
            return 2
        else:
            return 1

    def regex_match(test):
        # For case [0] and [1]
        for regex_case in regex_cases:
            if re.search(regex_case, str(test)):
                return one_or_two(test, number)
            else:
                return 0

    def incremental_number(test):
        test = str(test)
        for x in range(len(test)):
            if x + 1 == len(test):
                return one_or_two(int(test), number)
            if int(test[x]) == 9:
                if int(test[x + 1]) != 0:
                    break
            elif int(test[x + 1]) - 1 != int(test[x]):
                break
        return 0

    def decremental_number(test):
        test = str(test)
        for x in range(len(test)):
            if x + 1 == len(test):
                return one_or_two(int(test), number)
            if int(test[x]) == 1:
                if int(test[x + 1]) != 0:
                    break
            elif int(test[x]) - 1 != int(test[x + 1]):
                break
        return 0

    def palindrome(test):
        test = str(test)
        if test == test[::-1]:
            return one_or_two(int(test), number)
        else:
            return 0

    def is_in_array(test, array):
        if test in array:
            return one_or_two(test, number)
        else:
            return 0

    if number < 98:
        return 0

    for number_test in mileage_near_numbers(number):
        if number_test < 100:
            continue
        if regex_match(number_test) != 0:
            return regex_match(number_test)
        elif incremental_number(number_test) != 0:
            return incremental_number(number_test)
        elif decremental_number(number_test) != 0:
            return decremental_number(number_test)
        elif palindrome(number_test) != 0:
            return palindrome(number_test)
        elif is_in_array(number_test, awesome_phrases) != 0:
            return is_in_array(number_test, awesome_phrases)
    return 0


print(is_interesting(99, []))
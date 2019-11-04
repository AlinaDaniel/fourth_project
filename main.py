# Project #4 "Boolean operations".
# The program performs the logical operations, entered by the user,
# and printing tables of truth for them.

# Choosing the language.
print('Choose language/ Выберите язык.\n1) Englishs/ Английский язык;\n2) '
      'Russian/ Русский язык.')
language = input('Input number/ Введите цифру: ')

while True:
    if language == '1':
        import eng_local as lc

        break
    elif language == '2':
        import rus_local as lc

        break
    print('Choose language/ Выберите язык./n1) Englishs/ Английский язык;\n2) '
          'Russian/ Русский язык.')
    language = input('Input number/ Введите цифру: ')

# The user inputs the first boolean operation.
print(lc.TXT_INPUT_OPERATION)
boolean_operation = input()
boolean_operation = boolean_operation.replace(' ', '')
boolean_operation = str.lower(boolean_operation)

x = '0011'
y = '0101'


def conjunction(a, b):
    """
    Function, performing boolean operation of conjunction.
    :param a: first statement of the boolean operation
    :param b: second statement of the boolean operation
    :return: result of boolean operation
    """
    global f
    f = '0000'
    for i in range(4):
        if int(a[i]) == 1 and int(b[i]) == 1:
            f = f[:i] + '1'
        else:
            f = f[:i] + '0'


def disjunction(a, b):
    """
    Function, performing boolean operation of disjunction.
    :param a: first statement of the boolean operation
    :param b: second statement of the boolean operation
    :return: result of boolean operation
    """
    global f
    f = '0000'
    for i in range(4):
        if int(a[i]) == 0 and int(b[i]) == 0:
            f = f[:i] + '0'
        else:
            f = f[:i] + '1'


def implication(a, b):
    """
    Function, performing boolean operation of implication.
    :param a: first statement of the boolean operation
    :param b: second statement of the boolean operation
    :return: result of boolean operation
    """
    global f
    f = '0000'
    for i in range(4):
        if int(a[i]) == 1 and int(b[i]) == 0:
            f = f[:i] + '0'
        else:
            f = f[:i] + '1'


def equivalency(a, b):
    """
    Function, performing boolean operation of equivalency.
    :param a: first statement of the boolean operation
    :param b: second statement of the boolean operation
    :return: result of boolean operation
    """
    global f
    f = '0000'
    for i in range(4):
        if int(a[i]) == 0 and int(b[i]) == 0:
            f = f[:i] + '1'
        elif int(a[i]) == 1 and int(b[i]) == 1:
            f = f[:i] + '1'
        else:
            f = f[:i] + '0'


def table(a, b, param_1, param_2, b_operation):
    """
    Function, printing table of the truth for boolean operation.
    :param a: first statement of the boolean operation
    :param b: second statement of the boolean operation
    :param param_1: name of first statement of the boolean operation
    :param param_2: name of second statement of the boolean operation
    :param b_operation: boolean operation, for which table is painted
    :return: table of truth
    """
    print('-' * 21)
    print('|{:^19}|'.format(lc.TXT_TABLE_OF_TRUTH))
    print('-' * 21)
    print('|{:^5}|{:^5}|{:^7}|'.format(param_1, param_2, b_operation))
    print('-' * 21)
    print('|{:^5}|{:^5}|{:^7}|'.format(a[0], b[0], f[0]))
    print('|{:^5}|{:^5}|{:^7}|'.format(a[1], b[1], f[1]))
    print('|{:^5}|{:^5}|{:^7}|'.format(a[2], b[2], f[2]))
    print('|{:^5}|{:^5}|{:^7}|'.format(a[3], b[3], f[3]))
    print('-' * 21)


def calculation(b_operation, a, b, param_1, param_2):
    """
    Function, identifying boolean operation, which is needed to be perform;
     performing it and making a table of truth for it.
    :param a: first statement of the boolean operation
    :param b: second statement of the boolean operation
    :param param_1: name of first statement of the boolean operation
    :param param_2: name of second statement of the boolean operation
    :param b_operation: boolean operation, which is performing and for which
     table is painted
    """
    global f
    if b_operation[1] == '&':
        conjunction(a, b)
        table(a, b, param_1, param_2, b_operation)
    elif b_operation[1] == 'v':
        disjunction(a, b)
        table(a, b, param_1, param_2, b_operation)
    elif b_operation[1:3] == '=>':
        implication(a, b)
        table(a, b, param_1, param_2, b_operation)
    elif b_operation[1:4] == '<=>':
        equivalency(a, b)
        table(a, b, param_1, param_2, b_operation)
    else:
        # If user inputs unproper operation.
        print(lc.TXT_UNDENTIFIED_OPERATION)
        n = 0



def params(new_b_operation):
    """
    Function, identifying for which statements will be performing the next
     boolean operation.
    :param new_b_operation: the next boolean operation
    """
    global c, d, param_3, param_4, f
    if (new_b_operation[0] == 'f' and new_b_operation.find('y') != -1):
        c = f
        d = y
        param_3 = 'f'
        param_4 = 'y'
    elif (new_b_operation[0] == 'f' and new_b_operation.find('x') != -1):
        c = f
        d = x
        param_3 = 'f'
        param_4 = 'x'
    elif (new_b_operation.find('x') == -1 and new_b_operation.find('y') == -1
          and new_b_operation.find('f') != -1 and new_b_operation.find('f', 1) != -1):
        c = f
        d = c
        param_3 = 'f'
        param_4 = param_3
    elif (new_b_operation[0] == 'y' and new_b_operation.find('f') != -1):
        c = y
        d = f
        param_3 = 'y'
        param_4 = 'f'
    elif (new_b_operation[0] == 'x' and new_b_operation.find('f') != -1):
        c = x
        d = f
        param_3 = 'x'
        param_4 = 'f'
    else:
        # If user inputs unproper operation.
        print(lc.TXT_UNDENTIFIED_OPERATION)
        n = 0


def main():
    """
    Main function, joining process of performing several boolean operations
    and of printing table of truth for them.
    """

    # Identifying for which statements will be performing the first boolean
    # operation.
    n = 1
    if (boolean_operation[0] == 'x' and boolean_operation.find('y') != -1):
        a = x
        b = y
        param_1 = 'x'
        param_2 = 'y'
    elif (boolean_operation[0] == 'y' and boolean_operation.find('x') != -1):
        a = y
        b = x
        param_1 = 'y'
        param_2 = 'x'
    elif (boolean_operation.find('x') == -1 and boolean_operation.find('y') != -1
          and boolean_operation.find('y', 1) != -1):
        a = y
        b = y
        param_1 = 'y'
        param_2 = 'y'
    elif (boolean_operation.find('y') == -1 and boolean_operation.find('x') != -1
          and boolean_operation.find('x', 1) != -1):
        a = x
        b = x
        param_1 = 'x'
        param_2 = 'x'
    else:
        # If user inputs unproper operation.
        print(lc.TXT_UNDENTIFIED_OPERATION)
        n = 0

    if n != 0:
        # Performing first boolean operaton and making a table of truth for it.
        calculation(boolean_operation, a, b, param_1, param_2)

        # If the user has entered the proper boolean operation, the program offers
        # him/her to perform the next operation.
        print(lc.TXT_INPUT_NEXT_OPERATION)
        # The user enters the next operation.
        new_b_operation = input()
        new_b_operation = new_b_operation.replace(' ', '')
        new_b_operation = str.lower(new_b_operation)
        # The program offers to the user to perform the next operation, while
        # she/he does not input '0'.
        while new_b_operation != '0':
            params(new_b_operation)
            if n == 0:
                break
            calculation(new_b_operation, c, d, param_3, param_4)
            if n == 0:
                break
            print(lc.TXT_INPUT_NEXT_OPERATION)
            new_b_operation = input()
            new_b_operation = new_b_operation.replace(' ', '')
            new_b_operation = str.lower(new_b_operation)


main()

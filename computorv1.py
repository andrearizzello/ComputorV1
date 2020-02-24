from re import compile
from sys import argv

reg_monomial = compile(
    '(?:^\s*([+-])?|\s*([+-])(?![+-]))\s*(?:(\d+(?:\.\d*)?)\s*\*)?\s*([+-])?(?![+-])(\d+(?:\.\d*)?)?([xX])?(?:\^(\d+))?\s*')


class Monomial:
    def __init__(self, monomial=None, sign='+', number=1.0, x=False, power=0):
        if monomial is not None:
            self.sign = monomial[1] if monomial[1].__len__() > 0 else monomial[0] if monomial[0].__len__() > 0 else '+'
            if monomial[2].__len__() > 0:
                self.number = float(monomial[2])
            elif monomial[4].__len__() > 0:
                self.number = float(monomial[4])
            else:
                self.number = 1.0
            self.x = True if monomial[5].__len__() > 0 else False
            if monomial[6].__len__() > 0:
                self.power = int(monomial[6])
            elif self.x is True:
                self.power = 1
            else:
                self.power = 0
        else:
            self.sign = sign
            self.number = number
            if x and power == 0:
                self.x = False
            else:
                self.x = x
                self.power = power


def splitter(equation):
    try:
        [left, right] = equation.split('=')
        return [left, right]
    except ValueError:
        print("Syntax error (Wrong format)")
        exit(1)


def cleaner(monomial_list):
    for index, monomial in enumerate(monomial_list):
        if monomial.number == 0.0:
            monomial_list.pop(index)


def toString(left, right):
    equation = ''
    for monomial in left:
        equation += f'{f"{monomial.sign} " if monomial.sign == "-" or equation.__len__() > 0 else ""}' \
                    f'{monomial.number}' \
                    f'{"X" if monomial.x else ""}' \
                    f'{f"^{monomial.power}" if monomial.x and monomial.power != 1 else ""} '
    if left.__len__() == 0:
        equation += '0 '
    equation += '='
    for monomial in right:
        equation += f' {f"{monomial.sign} " if equation[-1:] != "=" or monomial.sign == "-" else ""}' \
                    f'{monomial.number}' \
                    f'{"X" if monomial.x else ""}' \
                    f'{f"^{monomial.power}" if monomial.x and monomial.power != 1 else ""}'
    if right.__len__() == 0:
        equation += ' 0'
    return equation


def reducer(left, right):
    cleaner(left)
    cleaner(right)
    power_list = {}
    for monomial in left:
        if monomial.power not in power_list:
            power_list[monomial.power] = 0.0
        power_list[monomial.power] += monomial.number if monomial.sign != '-' else -monomial.number
    for monomial in right:
        if monomial.power not in power_list:
            power_list[monomial.power] = 0
        power_list[monomial.power] -= monomial.number if monomial.sign != '-' else -monomial.number
    left = []
    right = []
    for power_element in sorted(power_list, reverse=True):  # TODO: Check if this works...
        if power_list[power_element] != 0.0:
            left.append(Monomial(sign='-' if power_list[power_element] < 0 else '+',
                                 number=abs(power_list[power_element]),
                                 x=True,
                                 power=power_element))
    return [left, right]


def solver(left):
    if left.__len__() == 0:
        print("Every real are solution")
        exit(0)
    if hasattr(left[0], 'power'):
        degree = left[0].power
    else:
        degree = 0
    if degree > 2:
        print("Polynomial degree is grater than 2, i'm unable to solve")
        exit(1)
    print(f"Polynomial degree is: {degree}")
    if degree == 0:
        a = left[0].number if left[0].sign == '+' else -left[0].number
        if a == 0:
            print("Every real are solution")
            exit(0)
        else:
            print("There are no solution")
            exit(0)
    elif degree == 1:
        if left.__len__() > 1:
            a = left[0].number if left[0].sign == '+' else -left[0].number
            b = left[1].number if left[1].sign == '+' else -left[1].number
        else:
            a = left[0].number if left[0].sign == '+' else -left[0].number
            b = 0
        print(f"A = {a}\n"
              f"B = {b}\n"
              f"The solution is:\n"
              f"-B / A = {-b / a}")
        exit(0)
    else:
        if left.__len__() > 2:
            a = left[0].number if left[0].sign == '+' else -left[0].number
            b = left[1].number if left[1].sign == '+' else -left[1].number
            c = left[2].number if left[2].sign == '+' else -left[2].number
        elif left.__len__() == 2:
            a = left[0].number if left[0].sign == '+' else -left[0].number
            b = left[1].number if left[1].sign == '+' else -left[1].number
            c = 0
        else:
            a = left[0].number if left[0].sign == '+' else -left[0].number
            b = 0
            c = 0
        delta = b ** 2 - (4 * a * c)
        print(f"A = {a}\n"
              f"B = {b}\n"
              f"C = {c}\n"
              f"𝚫 = {delta}\n")
        if delta > 0:
            print(f"𝚫 is positive, here the two solutions:\n"
                  f"(-B - (𝚫 ** 0.5)) / (2 * a) = {(-b - (delta ** 0.5)) / (2 * a)}\n"
                  f"(-B + (𝚫 ** 0.5)) / (2 * a) = {(-b + (delta ** 0.5)) / (2 * a)}")
            exit(0)
        elif delta == 0:
            print(f"𝚫 is 0, here the solution:\n"
                  f"-B / (2 * A) = {-b / (2 * a)}")
            exit(0)
        else:
            print(f"𝚫 is negative, here the two solutions:\n"
                  f"(-B - (𝚫 ** 0.5)) / (2 * A) = {(-b - (abs(delta) ** 0.5)) / (2 * a)}i\n"
                  f"(-B + (𝚫 ** 0.5)) / (2 * A) = {(-b + (abs(delta) ** 0.5)) / (2 * a)}i")
            exit(0)


if __name__ == '__main__':
    left = []
    right = []

    if argv.__len__() < 2:
        print("Error (no equation found)")
        exit(1)
    equation = argv[1].strip()
    if equation.__len__() < 1:
        print("Syntax error (empty string)")
        exit(1)
    [left_string, right_string] = splitter(equation)
    left_string = left_string.strip()
    right_string = right_string.strip()
    left_matches = reg_monomial.findall(left_string)
    right_matches = reg_monomial.findall(right_string)
    for monomial_element in left_matches:
        left.append(Monomial(monomial_element))
    for monomial_element in right_matches:
        right.append(Monomial(monomial_element))
    print(f'Equation parsed is: {toString(left, right)}')
    left, right = reducer(left, right)
    print(f"Reduced form: {toString(left, right)}")
    solver(left)

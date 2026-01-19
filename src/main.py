import math
import ui
import compute

if __name__ == '__main__':
    # Getting inputs
    QUIT_KEY = ord('q')
    print(f'At any time, enter {chr(QUIT_KEY)} to quit')
    base = ui.get_int(
        QUIT_KEY,
        lambda n: n > 1,
        'Enter the base (i.e, if the circuit should comprise of 1-to-X splitters, enter X): ',
        'Base must be greater than 1')
    num = ui.get_int(
        QUIT_KEY,
        lambda n: n > 0,
        'Enter the output numerator: ',
        'Numerator must be a positive integer')
    denom = ui.get_int(
        QUIT_KEY,
        lambda d: d > num,
        'Enter the output denominator: ',
        f'Denominator must be an integer greater than the numerator {num}')
    # Reducing inputs
    g = math.gcd(num, denom)
    num //= g
    denom //= g
    # Outputting calculations
    b = math.ceil(math.log(denom, base))
    if base ** b == denom:
        print(f'Primary output ({num}/{denom}): {num}\xb7{base}{compute.as_exponent(-b)}')
        print(f'Secondary output ({denom - num}/{denom}): Everything else')
    else:
        # Subtracting from exponents to account for fraction
        pri_as_base = {(p - b, s) for p, s in compute.as_base(base, num).items()}
        sec_as_base = {(p - b, s) for p, s in compute.as_base(base, denom - num).items()}
        print(f'Primary output ({num}/{denom}): {ui.expand_as_base(base, pri_as_base)}')
        print(f'Secondary output ({denom - num}/{denom}): {ui.expand_as_base(base, sec_as_base)}')
        print('Loopback: Everything else')

import math

while True:
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))

    D = b**2 - 4*a*c
    print(f"Diskriminant : {D}")

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print(f"x1: {x1}\nx2: {x2}")
        print('2 marta kesib o\'tadi')
    elif D == 0:
        x = -b / (2 * a)
        print(f"x: {x}")
        print("1 marta kesib o'tadi")
    else:
        print("x o'qini kesib o'tmaydi!")
    next_calculation = input("Boshqa hisob-kitob qilishni xohlaysizmi? (yes/no): ")
    if next_calculation.lower() != 'yes':
        print('Thank you for using our calculator!')
        break

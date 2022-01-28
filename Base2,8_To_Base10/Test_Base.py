button = input("Enter")
while button ==  'B' or button == 'O':
    if button == 'B':
        Base2 = input("Enter")
        Round_Base2 = len(Base2)
        total_Base2 = 0
        Multiply_Base2 = 0
        for x in Base2 :
            Round_Base2 -= 1
            Multiply_Base2 = 2**Round_Base2
            total_Base2 += int(x) * Multiply_Base2
        print(total_Base2)
    if button == 'O':
        Base8 = input("Enter")
        Round_Base8 = len(Base8)
        Multiply_Base8 = 0
        total_Base8 = 0
        for i in Base8:
            Round_Base8 -= 1
            Multiply_Base8 = 8**Round_Base8
            total_Base8 += int(i) * Multiply_Base8
        print(total_Base8)

'''
2**5 = 32  * 1 = 32
2**4 = 16 * 1 = 16
2**3 = 8 * 0 = 0
2**2 = 4 * 1 = 4
2**1 = 2 * 1 = 2
2**0 = 1 * 0 = 0
32 + 16 + 4 + 2 = 54
'''


    
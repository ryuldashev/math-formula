print('this program solve this kind of equestion ax^2 + bx +c')

a = input('\n''please write number for a: ')
b = input('\n''please write number for b: ')
c = input('\n''please write number for c: ')

d = float(b**2 - 4 * a * c)


print('\n''discriminant = b^2 - 4 * a * c = ' + str(b * b) + ' - ' + str(4 * a * c) + ' = ' + str(d))

if d < 0:
    print ('\n''havent roots, because ' + str(d) + ' < 0 ')

    file = open('answers.txt', 'w')
    file.write('\n''havent roots because: ' + str(d) + ' < 0')

elif d == 0:
    x = float(-b / (2 * a))

    print('\n''x = -b / (2 * a) = ' + str(-b) + ' / ' + str(2 * a) + ' = ' + str(x))

    print ('\n''Have one root: '+ str(x))

    file = open('answers.txt', 'w')
    file.write('\n''Discriminant: ' + str(d))
    file.write('\n''X = ' + str(x))



else:
    e = pow(d, 0.5)            
    
    x1 = (-b + e) / (2 * a)

    x2 = (-b - e) / (2 * a)

    str2a = str(2 * a)
   
    print(
        ''.join(
            [
                '\n',
                'x1 = (-b + d^1/2)/(2 * a) = ',
                str(-b), 
                            ' + ',
                str(e),
                            ' / ',
                str(2),
                            ' * ',
                str(a),
                            ' = ' ,
                str(-b + e),
                            ' / ',
                str2a,
                            ' = ',
                str(x1),
            ]
        )
    )

    print('\n''x2 = (-b - d^1/2)/(2 * a) = ' + str(
        -b) + ' - ' + str(e) + ' / ' + str(2) + ' * ' + str(a
        ) + ' = ' + str(-b - e) + ' / ' + str2a + ' = ' + str(x2))

    print (
        ''.join(
            [
                '\n', 
                'first root is [', 
                str(x1), 
                '], second one is [',
                 str(x2),
                 ']',
            ]
        )
    )


    file = open('answers.txt', 'w')
    file.write('\n''Discriminant: ' + str(d))
    file.write('\n''first root is: ' + str(x1))
    file.write('\n''second root is: ' + str(x2))
    file.close()








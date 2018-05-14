print('In this program you can solve arifmetic progress')

a1 = input('\n''Please write number for a1: ')
a2 = input('\n''Please write number for a2: ')
n = input('\n''PLease write number of n: ')



d = float(a2 - a1)      

c = float((n - 1) * d)        

l = float(a1 + c)        

b = float(l * n) / 2         



print('\n''An = a1 + ((n - 1) * d) = ' + str(a1) + ' + (' + str(n) + ' - ' + str(1) + ') * ' + str(d) + ' = ' + str(a1) + ' + ' + str(c) + ' = ' + str(l))

print('\n''Sn = ((a1 + an) / 2) * n = ' '((' + str(a1) + ' + ' + str(l) + ') / ' + str(2) + ') * ' + str(n) + ' = (' + str(l + 1) + ' / ' + str(2) + ') * ' + str(n) + ' = ' + str(b) + '\n')


try:

    'you write word'

except NameError:

	'Word - is not number'
	
print('please write number')
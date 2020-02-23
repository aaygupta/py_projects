name = ''
num = 0
print('Please enter your name: ')
name = input()
num = len(name)

for i in name:
    # print('*'*num + ' ' + i + ' ' + '*'*num)
    print((' ' + i + ' ').center(num*2+3,'*'))
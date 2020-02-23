my_list = []
num = 0

while True:
    print('Please enter item ' + str(len(my_list) + 1) + '  (or Enter nothing to stop).')
    item = input()
    if item == '':
        break
    my_list += [item]

num = len(my_list)
if num == 0:
    print('The list is empty')
elif num == 1:
    print(my_list[0])
elif num == 2:
    print(' and '.join(item for item in my_list))
else:
    print((', '.join(item for item in my_list[:-1])) + ' and ' + my_list[-1])

inputString = input()
signIndicator = 0
for i in inputString:
    if i.isdigit():
        signIndicator = 1
    elif signIndicator and (i == '-' or i == '+'):
        signIndicator = 0
    else:
        print('False, None')
        break
else:
    if signIndicator:
        print('True,', eval(inputString))
    else:
        print('False, None')
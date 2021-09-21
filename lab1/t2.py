from sys import argv
import operator
try:
    if len(argv) == 4:
        print(eval('operator.' + argv[1] + '(' + argv[2] + ', ' + argv[3] + ')'))
    else:
        print('Error!')
except Exception:
    print('Error!')

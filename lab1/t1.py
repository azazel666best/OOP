from sys import argv
try:
    if len(argv) == 4:
        print(eval(' '.join(argv[1:4])))
    else:
        print('Error!')
except Exception:
    print('Error!')
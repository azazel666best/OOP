from sys import argv
dictionary = {'add': '+', 'subtract': '-', 'multiply': '*', 'divide': '/'}
print(eval(argv[2]+dictionary[argv[1]]+argv[3]))
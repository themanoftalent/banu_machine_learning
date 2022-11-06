import sys

text = 'help'
count = 0

while text == 'help':
    print('start-to start the car\nstop-stop the car\nquit-to exit')
    decide = input('Enter the choice = ')
    count += 1
    if decide == 'start':
        print("started the car")
    if decide == 'stop':
        print("stopped the car")
    if decide == 'quit':
        print("quit the car")
    sys.exit(0)

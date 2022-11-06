command = ''
started = False
# while command.lower() != 'quit'
while True:
    command = input('> ').lower()
    if command == 'start':
        if started:
            print('Already started')
        else:
            started = True
            print('car started')
    elif command == 'stop':
        if not started:
            print('Already stopped')
        else:
            started = False
            print('car stopped')
    elif command == 'quit':
        print('The program stopped successfully')
        break
    elif command == 'help':
        print("""
        start: start car
        stop: stop car
        quit: quit car
        """)
    else:
        print('unknown command')
        print(command, input('> '))

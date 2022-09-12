#!/usr/bin/python3

from signal_handler import SignalHandler


if __name__ == '__main__':
    terminator = SignalHandler(handler=lambda: print('\nOn terminate actions here!\n'))
    while True:
        if not terminator.terminated:
            print('Cycle')
        else:
            print(f"Message:     {terminator.message}\nTraceback: {terminator.traceback}\n"
                  f"Signal name: {terminator.signal_name}")
            break

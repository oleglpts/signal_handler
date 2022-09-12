#!/usr/bin/python3

import time
from signal_handler import SignalHandler


if __name__ == '__main__':
    terminator = SignalHandler(handler=lambda: print('\nOn terminate actions here!\n'))
    while True:
        if not terminator.terminated:
            print('Cycle')
            time.sleep(2)
        else:
            print(f"Message:     {terminator.message}\nTraceback: {terminator.traceback}\n"
                  f"Signal name: {terminator.signal_name}")
            break

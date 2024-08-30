#!/usr/bin/env python
import sys
import time

######################
# A simple program to slow down stdoutput. Used to mimic OLD terminal output
#Author: Wayne Byrne 30-August-2024
#Email : wayne_ajp_byrne@hotmail.com
######################

# Example usage :
# ls -laR | slowoutput 0.01 (this is faster than default, which is .05)


if __name__ == '__main__':

    ts =.05 # Default speed per character output

    if len(sys.argv) > 1:
        ts = float(sys.argv[1])

    for line in sys.stdin:
        string1=str(line)
        for char in string1:
            sys.stdout.write(char)
            sys.stdout.flush()   # Never forget to flush the buffer
            time.sleep(ts)
    print('Finished')

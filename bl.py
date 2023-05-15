#!/usr/bin/env python3

import sys

def textualcmd(args):
    window = args[0] # Current window
    msg_count = ""

    if len(args) > 1:
        if args[1].isdigit(): # For /bl <msg_count>
            msg_count = args[1]
        elif args[1] != "": # When sending /bl <channel>
            window = args[1]
            if len(args) > 2 and args[2].isdigit(): # When sending /bl <channel> <msg_count>
                msg_count = args[2]

    command = "/msg *backlog {} {}".format(window, msg_count)
    return command.strip()

if __name__ == "__main__":
    result = textualcmd(sys.argv[1:])
    print(result) # Return the command to Textual

import argparse
import sys
from core.color import green

banner = '''

  ______ ______     _          _     ______        ______  ______  _______ ______  
 / _____)  ___ \   | |        | |   / _____)  /\  |  ___ \|  ___ \(_______|_____ \ 
| /     | | _ | |   \ \        \ \ | /       /  \ | |   | | |   | |_____   _____) )
| |     | || || |    \ \        \ \| |      / /\ \| |   | | |   | |  ___) (_____ ( 
| \_____| || || |_____) )   _____) ) \_____| |__| | |   | | |   | | |_____      | |
 \______)_||_||_(______/   (______/ \______)______|_|   |_|_|   |_|_______)     |_|
                                                                                    
'''
def argsload():
    parser = argparse.ArgumentParser(
        description='CMS Scanner v0.1 by Pradeep Jairamani')
    parser.add_argument('-t', '--target', action="store",
                        dest="target", help="Target Goes here")

    parser.add_argument('-v', '--verbose', action="store_true",
                        help="Enable Verbose scan", default=False)
    parser.add_argument('-f', '--force', action="store",
                        dest="force", help="Force CMS type")
    parser.add_argument('-i', '--interactive', action="store_true",
                        default=False, help="Interactive Scanning")

    args = parser.parse_args()
    if args.target:
        return args
    else:
        green(banner)
        print( "\n" + parser.parse_args(['-h']) + "\n" )
        print("\n")
        sys.exit(0)

import argparse
import sys

def argsload():
    parser = argparse.ArgumentParser(
        description='CMS Scanner v0.1 by Pradeep Jairamani')

    parser.add_argument('-v', '--verbose', action="store_true",
                        help="Enable Verbose scan", default=False)
    parser.add_argument('-t', '--target', action="store",
                        dest="target", help="Target Goes here")
    parser.add_argument('-f', '--force', action="store",
                        dest="force", help="Force CMS type")
    parser.add_argument('-i', '--interactive', action="store_true",
                        default=False, help="Interactive Scanning")

    args = parser.parse_args()
    if args.target:
        return args
    else:
        print parser.parse_args(['-h'])
        sys.exit(0)

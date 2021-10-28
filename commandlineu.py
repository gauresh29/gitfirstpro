import argparse
import sys
def calc(args):
    if args.z == 'add':
        return args.x +args.y
    elif args.z== 'sub':
        return args.x - args.y
    elif args.z == 'mul':
        return args.x * args.y
    elif args.z == 'div':
        return args.x / args.y
    else:
        return "something went wrong"

if __name__ == '__main__':
    parser= argparse.ArgumentParser()
    parser.add_argument("--x",type=float, default=1.0,help="enter firt number thsi is utility for "
                                                           "calculation for command line utility")

    parser.add_argument("--y",type=float, default=3.0,help="enter firt number thsi is utility for "
                                                           "calculation for command line utility")

    parser.add_argument("--z",type=str, default="add",help="enter firt number thsi is utility for "
                                                           "calculation for command line utility")

    arg= parser.parse_args()
    sys.stdout.write(str(calc(arg)))

    # .\commandlineu.py --x 12 --y 12 --z add
#!/usr/bin/env python3


import sys
import argparse


def init_argparse():
    parser = argparse.ArgumentParser(description="lo - limit order calculator")
    parser.add_argument("--price", dest="p",
                        help="Stock price")
    parser.add_argument("--num-shares", dest="ns",
                        help="Number of shares")
    parser.add_argument("--commissions", dest="c",
                        help="Combined buy/sell commission")
    parser.add_argument("--desired-profit", dest="dp",
                        help="Desired profit after costs")
    return parser.parse_args()


def main(argv):
    print('Begin run...')
    args = init_argparse()

    p = float(args.p)
    c = float(args.c)
    ns = float(args.ns)
    if ns <= 0:
        print("Number of shares cannot be zero, exiting...")
        sys.exit(1)
    dp = float(args.dp)

    # compute price per share increase needed based
    # on commissions and num shares
    pp = c / ns

    print("Break even price             : {:6.2f}".format(p + pp))

    if dp > 0:
        pp = pp + (dp / ns)
        print("Desired profit sell price    : {:6.2f}".format(p + pp))

    print("Acquisition cost             : {:6.2f}".format(p * ns + c))

    print('End run.')
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

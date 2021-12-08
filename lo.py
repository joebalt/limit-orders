#!/usr/bin/env python3


import sys
import argparse


"""Determine limit order price based on desired profit"""


def init_argparse():
    parser = argparse.ArgumentParser(description="lo.py - limit order calculator")
    parser.add_argument("-p", "--price", dest="p",
                        help="Stock price",
                        type=float,
                        required=True)
    parser.add_argument("-ns", "--num-shares", dest="ns",
                        help="Number of shares",
                        type=float,
                        required=True)
    parser.add_argument("-c", "--commissions", dest="c",
                        help="Combined buy/sell commission",
                        type=float,
                        required=True)
    parser.add_argument("-dp", "--desired-profit", dest="dp",
                        help="Desired total profit after costs",
                        type=float,
                        required=True)
    return parser.parse_args()


def main(argv):
    print('Begin run...')
    args = init_argparse()

    p = args.p
    c = args.c
    ns = args.ns
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

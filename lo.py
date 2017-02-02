#!/usr/bin/env python


import sys


def main(argv):
    print('Begin run...')

    p = float(raw_input("Stock price                  : "))
    ns = float(raw_input("Number of shares             : "))
    print("buy/sell combined commission : 20")
    c = 20.0
    # c = float(raw_input("buy/sell combined commission : "))
    if ns <= 0:
        print("Number of shares cannot be zero, exiting...")
        sys.exit(1)
    dp = float(raw_input("Desired profit               : "))
    # ct = float(raw_input("Capital gains tax (%)        : "))

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

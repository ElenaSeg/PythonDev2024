import cowsay
import argparse

parser = argparse.ArgumentParser(prog="cow_say",
                                 description="Works like python-cowsay, \
                                 supports -l flag")

parser.add_argument("message", nargs="?", default="", help="the message for a cow")
parser.add_argument("-e", default=cowsay.Option.eyes, dest="eyes",
                     help="cow's eyes string")
parser.add_argument("-f", "--file", help="file for a cow")
parser.add_argument("-I", action="store_true",
                     help="list all cowfiles on COWPATH")
parser.add_argument("-n", action="store_false", help="no wrap around flag")
parser.add_argument("-T", default="", dest="tongue",
                     help="choose cow's tongue string")
parser.add_argument("-W", dest="width", default=40, type=int,
                     help="choose cow's width")
parser.add_argument("-b", action="store_true")
parser.add_argument("-d", action="store_true")
parser.add_argument("-t", action="store_true")
parser.add_argument("-p", action="store_true")
parser.add_argument("-s", action="store_true")
parser.add_argument("-w", action="store_true")
parser.add_argument("-g", action="store_true")
parser.add_argument("-l", action="store_true")
parser.add_argument("-y", action="store_true")
parser.add_argument("-bdgpstwy", dest="preset")
args = parser.parse_args()

if args.l:
    print(cowsay.list_cows())
else:
    print(cowsay.cowsay(args.message,
                        preset=args.preset,
                        eyes=args.eyes,
                        tongue=args.tongue,
                        width=args.width,
                        cowfile=args.file))

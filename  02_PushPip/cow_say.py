import argparse
from cowsay import cowsay
from cowsay import list_cows

FLAGS = set("bdgpstwy")

def custom_custom_cow_say(args):
    if args.l or args.message == " ":
        print(cowsay.list_cows())
        return

    preset = None
    for key, value in args._get_kwargs():
        if key in FLAGS and value:
            preset = key
            break
    print(
        cowsay.cowsay(
            message=args.message,
            cow=args.f,
            preset=preset,
            tongue=args.T,
            width=args.W,
            wrap_text=not args.n,
            eyes=args.e
        )
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", type=str, default="oo", help="eye_string")
    parser.add_argument("-f", type=str, default="", help="path to cowfile")
    parser.add_argument("-l", action="store_true", help="list of cows")
    parser.add_argument("-n", type=str, action="store_false", help="wrap_text")
    parser.add_argument("-T", type=str, default="  ", help="cows tongue")
    parser.add_argument("-W", type=int, default=40, help="width of the text")
    parser.add_argument("message", action="store", default=" ", help="cow's words", nargs="?")
    for option in FLAGS:
        parser.add_argument(f"-{option}", action="store_true")
    args = parser.parse_args()
    custom_cow_say(args)


if __name__ == "__main__":
    main()

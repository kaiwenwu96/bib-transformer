import os
import time

import argparse


def main(input, output):
    while True:
        if 0 == os.system("python transformer.py {} > {}".format(input, output)):
            time.sleep(30)
        else:
            break


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--input', type=str, default=None)
    arg_parser.add_argument('--output', type=str, default=None)

    args = arg_parser.parse_args()

    assert args.input is not None and args.output is not None

    main(args.input, args.output)

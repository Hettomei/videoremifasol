import sys
import argparse


def parse_options(list_args):
    """
    Vérification des paramétres
    """
    parser = argparse.ArgumentParser(description="Enjoy")
    parser.add_argument(
        "--folder",
        action="store",
        dest="video_folder",
        help="Where all the video are",
        required=True,
    )
    parser.add_argument(
        "--text",
        action="store",
        dest="text",
        help="What to assemble ?",
        required=True,
    )
    return parser.parse_args(list_args)


def main(args):
    print(args)


if __name__ == "__main__":
    main(parse_options(sys.argv[1:]))

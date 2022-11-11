import sys
from pprint import pprint

import argparse
import subprocess
import os
from os.path import isfile, join


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

    onlyfiles = [
        os.path.abspath(join(args.video_folder, f))
        for f in os.listdir(args.video_folder)
        if isfile(join(args.video_folder, f))
    ]
    pprint(onlyfiles)
    # subprocess.run("ffmpeg -i input1.mp4 -c copy intermediate1.ts".split())


if __name__ == "__main__":
    main(parse_options(sys.argv[1:]))

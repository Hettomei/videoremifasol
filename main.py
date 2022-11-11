""" Do video stuff"""
import sys
from pprint import pprint
import tempfile

import argparse
import subprocess
import os
from os.path import isfile


def parse_options(list_args):
    """
    parse options
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
    """main"""
    print(args)
    tmppath = tempfile.mkdtemp()
    print(f"Everything goes to {tmppath}")

    videos = [
        os.path.abspath(os.path.join(args.video_folder, f))
        for f in os.listdir(args.video_folder)
        if isfile(os.path.join(args.video_folder, f))
    ]
    pprint(videos)

    for video in videos:
        name = os.path.splitext(os.path.basename(video))[0]
        new_file = os.path.join(tmppath, f"{name}.ts")
        print(f"convert {video} to {new_file}")
        subprocess.run(
            [
                "./bin/ffmpeg_folder/ffmpeg",
                "-i",
                video,
                "-c",
                "copy",
                new_file,
            ],
            check=True,
            capture_output=True,
        )

    selected_videos = []
    for token in args.text.split():
        print(f"will concat '{token}'")
        selected_videos.append(os.path.join(tmppath, f"{token}.ts"))

    print(selected_videos)
    print("Creating new video with params:")
    print("concat:" + "|".join(selected_videos))
    subprocess.run(
        [
            "ffmpeg",
            "-i",
            "concat:" + "|".join(selected_videos),
            "-c",
            "copy",
            "output.mp4",
        ],
        check=True,
    )


if __name__ == "__main__":
    main(parse_options(sys.argv[1:]))

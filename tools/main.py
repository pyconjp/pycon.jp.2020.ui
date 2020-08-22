import argparse
import csv

from sessionfetcher import fetch_talks_as_dict

import constants


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("sessions_uri")
    parser.add_argument("speakers_uri")
    parser.add_argument("-d", "--dest", default="talks.csv")
    return parser.parse_args()


def add_streaming_url(talk):
    if talk["id"] in constants.NOT_STREAMED_ID_SET:
        talk["youtube_url"] = ""
        return
    day_room_pair = (talk["day"], talk["room"])
    streaming_url = constants.YOUTUBE_LIVE_URL_MAP[day_room_pair]
    talk["youtube_url"] = streaming_url


def add_presentation_url(talk):
    talk["presentation_url"] = ""


def to_csv(talks, dest_path, fields):
    with open(dest_path, "w") as f:
        writer = csv.DictWriter(f, restval=None, fieldnames=fields)
        writer.writeheader()
        writer.writerows(talks)


def main():
    args = parse_args()

    talks = fetch_talks_as_dict(args.sessions_uri, args.speakers_uri)

    talks_list = []
    for talk in talks:
        add_streaming_url(talk)
        add_presentation_url(talk)
        talks_list.append(talk)

    # インデックス0=オープニングの後を指定（オープニングはfieldが足りない）
    fields = list(talks_list[1].keys())

    to_csv(talks_list, args.dest, fields)


if __name__ == "__main__":
    main()

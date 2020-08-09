import argparse
import csv
import json

from sessionfetcher import fetch_talks_as_dict


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("sessions_uri")
    parser.add_argument("speakers_uri")
    parser.add_argument("-d", "--dest", default="talks.csv")
    parser.add_argument("-l", "--load_data", default="data/invited.json")
    return parser.parse_args()


def to_csv(talks, dest_path, fields):
    with open(dest_path, "w") as f:
        writer = csv.DictWriter(f, restval=None, fieldnames=fields)
        writer.writeheader()
        writer.writerows(talks)


def load_data(data_path):
    with open(data_path) as f:
        return json.load(f)


def main():
    args = parse_args()

    loaded_talk = load_data(args.load_data)

    talks = fetch_talks_as_dict(args.sessions_uri, args.speakers_uri)
    talks_list = list(talks)
    fields = list(talks_list[0].keys())

    to_csv(loaded_talk + talks_list, args.dest, fields)


if __name__ == "__main__":
    main()

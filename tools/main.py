import argparse
import csv

from sessionfetcher import http


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("sessionize_uri")
    parser.add_argument("-d", "--dest", default="sessions.csv")
    return parser.parse_args()


def to_csv(sessions, dest_path):
    fields = sessions.fields
    with open(dest_path, "w") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for session in sessions:
            writer.writerow(session)


def main():
    args = parse_args()
    # sessionsを取得 引数 args.sessionize_uri
    # - sessionizeのAPIにリクエスト（返り値を取得）
    # - 返り値のパース
    to_csv(sessions, args.dest)


if __name__ == "__main__":
    main()

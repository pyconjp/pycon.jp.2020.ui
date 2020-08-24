import csv
import json


def main():
    result_dict = {"session-list": []}

    # csvファイルを読み込み必要なJSON形式に成形する
    with open('./session-data.csv', 'r', encoding='utf-8') as fp:
        reader = csv.DictReader(fp)
        for data in reader:
            result_dict["session-list"].append(
                {
                    'id': data['id'],
                    'youtube': data['youtube'],
                    'document': data['document'],
                    'title': data['title'],
                }
            )

    # JSONファイルを作成する
    with open('./session-data.json', 'w', encoding='utf-8') as fp:
        json.dump(result_dict, fp, ensure_ascii=False)


if __name__ == "__main__":
    main()

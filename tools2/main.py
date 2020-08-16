import csv
import json


def main():
    result_dict = {"en": [], "ja": []}

    # csvファイルを読み込み必要なJSON形式に成形する
    with open('./member-list.csv', 'r', encoding='utf-8') as fp:
        reader = csv.DictReader(fp)
        for data in reader:
            result_dict["en"].append(
                {
                    'name': data['name(en)'],
                    'title': data['title(en)'],
                    'photo': data['photo'],
                    'twitter': data['twitter'],
                    'facebook': data['facebook'],
                }
            )
            result_dict["ja"].append(
                {
                    'name': data['name(ja)'],
                    'title': data['title(ja)'],
                    'photo': data['photo'],
                    'twitter': data['twitter'],
                    'facebook': data['facebook'],
                }
            )

    # JSONファイルを作成する
    with open('./member-list.json', 'w', encoding='utf-8') as fp:
        json.dump(result_dict, fp, ensure_ascii=False)


if __name__ == "__main__":
    main()

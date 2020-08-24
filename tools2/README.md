## 概要

スタッフ名簿情報からWebサイトへ載せるためのデータ形式に変更するためのツール

## 使い方

### スタッフ情報更新用

スタッフ名簿からデータを「member-list.csv」というファイル名でmain.pyと同じ階層に配置する  
下記コマンドを実行する
※member-list.csvファイル内に改行が「"」と一緒に含まれる場合、改行と"を削除すること

```
$ python main.py
```

member-list.jsonが作成される


### セッション情報更新用

「PyCon JP 2020 Speaker question form（回答）」の「Webサイト掲載用」シートをCSV形式でダウンロードし、
「session-data.csv」というファイル名でmain2.pyと同じ階層に配置する
その後、下記コマンドを実行する

```
$ python main2.py
```

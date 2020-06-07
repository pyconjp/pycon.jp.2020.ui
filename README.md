# pycon.jp.2020

> PyCon JP 2020 Web Site

## 事前準備

### エディター

エディターにはvscodeを使い、[headwind](https://marketplace.visualstudio.com/items?itemName=heybourn.headwind)
と
[vscode-eslint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)
のふたつのエクステンションをインストールして下さい。セーブ時に自動でコードフォーマットされるようになります。

### node.jsとyarnのインストール方法

#### Macの場合

[Homebrew](https://brew.sh/index_ja)をインストール

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

[nodenv](https://github.com/nodenv/nodenv)

```bash
brew install nodenv
nodenv install 12.16.2
```

[yarn](https://classic.yarnpkg.com/ja/docs/install/#mac-stable)

```bash
brew install yarn --ignore-dependencies
```

## Build Setup

```bash
# 依存関係のインストール
$ yarn install

# 開発用サーバーの起動 localhost:3000
$ yarn dev

# 静的ファイルの生成をします
$ yarn generate
```

詳しい説明は[Nuxt.js docs](https://ja.nuxtjs.org)を見て下さい。


## AWSとの連携設定

下記のどちらかの方法でAWS環境内のリポジトリへアクセス可能な状態に設定をお願いします。

* [Git 認証情報を使用する HTTPS ユーザー用のセットアップ](https://docs.aws.amazon.com/ja_jp/codecommit/latest/userguide/setting-up-gc.html)
* [Linux, macOS, or Unix 上で AWS CodeCommit リポジトリに SSH 接続するために必要なセットアップ手順](https://docs.aws.amazon.com/ja_jp/codecommit/latest/userguide/setting-up-ssh-unixes.html)


設定が完了後は下記コマンドを実行しリモートリポジトリを追加してください。

```
# SSHの場合
$ git remote add aws ssh://git-codecommit.ap-northeast-1.amazonaws.com/v1/repos/pycon.jp.2020.ui

# HTTPSの場合
$ git remote add aws https://git-codecommit.ap-northeast-1.amazonaws.com/v1/repos/pycon.jp.2020.ui
```

stagingブランチをプッシュする場合

```
$ git checkout staging
$ git pull origin
$ git push aws
```

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

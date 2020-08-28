const sessionUrlLost = [
  {
    id: '213314',
    youtube: '',
    document: '',
    title: 'Invited talk: Ms. Nina Zakharenko',
  },
  {
    id: '202715',
    youtube: '',
    document:
      'https://docs.google.com/presentation/d/1OEKlYKyGTNbTuvITAwSH34kjvr0yLrbucLZ295J09vU/edit',
    title: '2020年代のコンテナ時代のPythonアーキテクチャ&デプロイ',
  },
  {
    id: '203955',
    youtube: '',
    document:
      'https://speakerdeck.com/yamitzky/mastering-type-safety-in-python-3-dot-9-era',
    title: 'Python 3.9 時代の型安全な Python の極め方',
  },
  {
    id: '203572',
    youtube: '',
    document:
      'https://speakerdeck.com/mizzsugar/unittest-dot-mockwoshi-tutetesutowoshu-kou',
    title:
      'unittest.mockを使って単体テストを書こう 〜より効率的で安定したテストに〜',
  },
  {
    id: '203929',
    youtube: '',
    document: 'https://speakerdeck.com/youjisuzuki000/youjisuzuki',
    title: '数理最適化×機械学習コラボレーションによる課題解決',
  },
  {
    id: '213320',
    youtube: '',
    document:
      'https://speakerdeck.com/mocobeta/aruge-ren-kai-fa-oss-falsebu-mi-5-sui-ninatuta-janome-falsekoremadeto-korekara',
    title:
      '招待講演：ある個人開発 OSS の歩み：5 歳になった Janome のこれまでと，これから',
  },
  {
    id: '203640',
    youtube: '',
    document:
      'https://www.slideshare.net/CraigFranklin2/machine-learning-outside-the-kaggle-lines?ref=https://pyconjp.connpass.com/event/181288/presentation/',
    title: 'Machine Learning Outside the Kaggle Lines',
  },
  {
    id: '203235',
    youtube: '',
    document: '',
    title: 'PythonからGolangに変更してから再びPythonに戻った理由',
  },
  {
    id: '203891',
    youtube: '',
    document: 'https://www.slideshare.net/secret/wvIdaFzxMxyKN2',
    title: 'Pythonパッケージの影響を歴史から理解してみよう！',
  },
  {
    id: '203810',
    youtube: '',
    document: 'https://speakerdeck.com/ukyo/guan-shu-xing-pythonantipatan',
    title: '関数型Pythonアンチパターン',
  },
  {
    id: '213316',
    youtube: '',
    document: '',
    title: '招待講演：続・小さく始めて大きく育てるMLOps2020',
  },
  {
    id: '203756',
    youtube: '',
    document: 'https://www.slideshare.net/shimizukawa/django-sqlalchemy-way',
    title: 'Django + SQLAlchemy: シンプルWay',
  },
  {
    id: '203309',
    youtube: '',
    document:
      'https://gavincyi.github.io/pycon-i-cant-believe-its-still-here/#1',
    title: "I can't believe it's still here!",
  },
  {
    id: '203588',
    youtube: '',
    document:
      'https://speakerdeck.com/hassaku63/python-and-aws-and-serverless-step-to-the-next-stage-from-a-beginner',
    title:
      'Python × AWS × Serverless 初学者が次の一歩を踏み出すためのテクニック',
  },
  {
    id: '203453',
    youtube: '',
    document: 'https://speakerdeck.com/miya8/pyconjp2020-5-0828-1450',
    title: 'PythonでXBRL形式の財務情報を扱おう',
  },
  {
    id: '203925',
    youtube: '',
    document: '',
    title: 'Exploring Biasness in Indian Media',
  },
  {
    id: '203875',
    youtube: '',
    document: '',
    title: 'GAE/Python2 to Python3 Migration Journey',
  },
  {
    id: '203941',
    youtube: '',
    document: '',
    title: 'Pythonで始める負荷試験',
  },
  {
    id: '201618',
    youtube: '',
    document: '',
    title: 'What happens behind execution of an `import` statement?',
  },
  {
    id: '202389',
    youtube: '',
    document: '',
    title:
      '量子コンピュータと現行コンピュータ、解法や解の違いは？～ナップサック問題を考える～',
  },
  {
    id: '203956',
    youtube: '',
    document: '',
    title: 'Combining ayncio and threads in the same application',
  },
  {
    id: '203444',
    youtube: '',
    document: '',
    title: 'PySnooper - Never use print for debugging again',
  },
  {
    id: '203877',
    youtube: '',
    document: '',
    title: 'Pythonソースコードの構造可視化とそれがもたらすもの',
  },
  {
    id: '203963',
    youtube: '',
    document: '',
    title: 'Pythonではじめるソフトウェア無線',
  },
  {
    id: '203110',
    youtube: '',
    document: '',
    title:
      'スポーツデータを用いた特徴量エンジニアリングと野球選手の成績予測 - PythonとRを行ったり来たり',
  },
  {
    id: '202785',
    youtube: '',
    document: '',
    title: 'Python で作る演劇稽古用 Web アプリ',
  },
  {
    id: '203793',
    youtube: '',
    document: '',
    title: 'Pythonで競プロをしよう！〜入門者が知っておくべき高速化Tips〜',
  },
  {
    id: '203665',
    youtube: '',
    document: '',
    title:
      'オルタナティブデータを用いた消費行動の分析　～２月のトイレットペーパーパニックを例に～',
  },
  {
    id: '203919',
    youtube: '',
    document: '',
    title: 'スタッフとしてコードを書こう！〜Code for PyCon JP and yourself〜',
  },
  {
    id: '203558',
    youtube: '',
    document: '',
    title: 'ラズパイ3BのCPUでリアルタイム物体検出',
  },
  {
    id: '203959',
    youtube: '',
    document: '',
    title: 'ASGI（非同期サーバゲートウェイインターフェース）の概要',
  },
  {
    id: '203111',
    youtube: '',
    document: '',
    title: 'Pythonで作る機械学習システムパターン',
  },
  {
    id: '203899',
    youtube: '',
    document: '',
    title: "Understanding Python's Debugging Internals",
  },
  {
    id: '203063',
    youtube: '',
    document: '',
    title: 'レトロゲームエンジン「Pyxel」でゲームプログラミングをはじめよう！',
  },
  {
    id: '203053',
    youtube: '',
    document: '',
    title:
      'How to Transform Research Oriented Code into Machine Learning APIs with Python',
  },
  {
    id: '203900',
    youtube: '',
    document: '',
    title: 'Sphinx はどのように Python コードからドキュメントを生成するのか',
  },
  {
    id: '203858',
    youtube: '',
    document: '',
    title: 'チーム開発立ち上げにやっておいたほうがいいソース管理の方法',
  },
  {
    id: '203648',
    youtube: '',
    document: '',
    title: 'ひとりで作る画像検索システム',
  },
  {
    id: '202353',
    youtube: '',
    document: '',
    title: 'BLEでロボットトイを制御しよう',
  },
  {
    id: '203923',
    youtube: '',
    document: '',
    title: 'Cloud RunとFastAPIで、ChatBotをミニマムスタートしよう',
  },
  {
    id: '201486',
    youtube: '',
    document: '',
    title: 'Your Escape Plan From Numpy + Cython',
  },
  {
    id: '203938',
    youtube: '',
    document: '',
    title: '広島における地域 Python コミュニティの立ち上げ方と続け方',
  },
  {
    id: '203938',
    youtube: '',
    document: '',
    title: '広島における地域 Python コミュニティの立ち上げ方と続け方',
  },
  {
    id: '203938',
    youtube: '',
    document: '',
    title: '広島における地域 Python コミュニティの立ち上げ方と続け方',
  },
  {
    id: '203938',
    youtube: '',
    document: '',
    title: '広島における地域 Python コミュニティの立ち上げ方と続け方',
  },
  {
    id: '203164',
    youtube: '',
    document: '',
    title: '最先端自然言語処理ライブラリの最適な選択と有用な利用方法',
  },
  {
    id: '202455',
    youtube: '',
    document: '',
    title: 'How to plot unstructured mesh file on Jupyter Notebook',
  },
  {
    id: '203957',
    youtube: '',
    document: '',
    title: 'NumPy/pandas使いのためのテスト自動化入門',
  },
  {
    id: '202771',
    youtube: '',
    document: '',
    title: 'Pythonによる機械翻訳モデルの構築',
  },
  {
    id: '203568',
    youtube: '',
    document: '',
    title: 'Spec-driven development for REST API',
  },
  {
    id: '203944',
    youtube: '',
    document: '',
    title: '詳解デコレータ ~実用的なデコレータを理解しよう~',
  },
  {
    id: '202587',
    youtube: '',
    document: '',
    title: 'Python(Cython) & OpenMPで高速並列処理',
  },
  {
    id: '203945',
    youtube: '',
    document: '',
    title: 'Python、ときどきRust',
  },
  {
    id: '203893',
    youtube: '',
    document: '',
    title: 'インメモリー ストリーム活用術',
  },
  {
    id: '203888',
    youtube: '',
    document: '',
    title: '機械学習の実装から考えるオブジェクト指向',
  },
]

export function getSessionDocumentUrl(sessionID) {
  const targetSessionData = sessionUrlLost.filter(
    (sessionData) => sessionData.id === sessionID
  )
  let returnSessionDocumentUrl = ''

  if (targetSessionData.length >= 1) {
    returnSessionDocumentUrl = targetSessionData[0].document
  }

  return returnSessionDocumentUrl
}

export function getSessionYoutubeUrl(sessionID) {
  const targetSessionData = sessionUrlLost.filter(
    (sessionData) => sessionData.id === sessionID
  )
  let returnSessionYoutubeUrl = ''

  if (targetSessionData.length >= 1) {
    returnSessionYoutubeUrl = targetSessionData[0].youtube
  }

  return returnSessionYoutubeUrl
}

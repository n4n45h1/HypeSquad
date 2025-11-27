# Discord HypeSquad Badge Get Tool

<p align="center">
  <img width="400" alt="HypeSquad Banner" src="https://i.imgur.com/b3acpXM.png">
</p>

<p align="center">
  HypeSquadバッジを取得できるツールです<br>
  PythonのCLI版と<a href="https://n4n45h1.github.io/HypeSquad/web/">ブラウザで使えるWeb版</a>があります
</p>

---

## HypeSquadってなんぞや？

| ハウス | バッジ | 色 |
|:---:|:---:|:---:|
| **Bravery (1)** | <img width="20" alt="bravery badge" src="https://i.imgur.com/1p3XXPq.png"> | 紫 |
| **Brilliance (2)** | <img width="20" alt="brilliance badge" src="https://i.imgur.com/T1PAb8K.png"> | 赤 |
| **Balance (3)** | <img width="20" alt="balance badge" src="https://i.imgur.com/EchSusJ.png"> | 青緑 |

> ⚠️ **注意**: 2025年10月中旬頃のDiscordアップデートで、ユーザーがHypeSquadに加入するための画面が削除されました。正規の方法ではこのバッジはつけられません。このツールは**非公式の方法**でバッジを取得するものです。

HypeSquadについての[詳細はこちら（Discord公式）](https://support.discord.com/hc/ja/articles/360007553672-HypeSquad%E3%83%8F%E3%82%A6%E3%82%B9%E3%81%AE%E8%A9%B3%E7%B4%B0)

---

## 使い方

### Python版

```bash
python hypesquad.py
```

1. トークン入力（直接入力 or `token.txt` などのファイル名）
2. 好きなハウスを選ぶ（1〜3）
3. 退室したいなら 4

### Web版

 [こちらを開くだけ](https://n4n45h1.github.io/HypeSquad/web/)

---

## 必要なもの

Python版のみ `requests` が必要です：

```bash
pip install -r requirements.txt
```

---

## トークンの取り方

1.  Discordを**ブラウザ**で開く
2. `F12` でDevToolsを開く
3. **Console（コンソール）** タブに移動
4. 以下のコードを貼り付けて実行：

```js
window.webpackChunkdiscord_app.push([[Symbol()],{},o=>{for(let e of Object.values(o.c))try{if(!e. exports||e.exports===window)continue;e.exports?.getToken&&(token=e.exports.getToken());for(let o in e.exports)e.exports? .[o]?. getToken&&"IntlMessagesProxy"!==e.exports[o][Symbol.toStringTag]&&(token=e.exports[o].getToken())}catch{}}]),window.webpackChunkdiscord_app.pop(),token;
```

5. 出てきた文字列がトークン（コピーして使う）

```
'MTM2MDk4MDIwMjg4xxxxxxxxx.xxxxx.xxxxxxxxxxxxxxxxxxxxxxxxxx'
```

> ⚠️ **警告**: トークンは絶対に他人に教えないでください！アカウントを乗っ取られる可能性があります。

---

## ファイル構成

```
.
├── hypesquad.py          # Python CLI版
├── requirements. txt      # 必要なパッケージ
├── web/
│   └── index.html        # Web版（スタンドアロン）
└── README.md             # これ
```

---

## 参考

- [Qiita - BrushedNeonさんの記事](https://qiita.com/BrushedNeon/items/e8b65de96ff8b7eb5ee9)
- [Note - yuuuyugbpさんの記事](https://note.com/yuuuyugbp/n/nbd779e2b0510)

---

## ライセンス

好きに使ってね 

---

<p align="center">
  ❤️ Made with Claude
</p>

# Discord HypeSquad Badge Get

HypeSquadバッチを取得できるツール  
PythonのCLI版と[ブラウザで使えるWeb版](https://n4n45h1.github.io/HypeSquad/web/)があります


## HypeSquadってなんぞや？

- **Bravery (1)** - 紫のバッジ <img width="20" alt="bravery badge" src="https://i.imgur.com/1p3XXPq.png">
- **Brilliance (2)** - 赤のバッジ <img width="20" alt="brilliance badge" src="https://i.imgur.com/T1PAb8K.png">
- **Balance (3)** - 青緑のバッジ <img width="20" alt="balance badge" src="https://i.imgur.com/EchSusJ.png">

正規の方法ではこのバッチはつけられないです。2025年10月の中旬頃に配布が終了(？)されたらしいです。

## 使い方

### Python版

```bash
python hypesquad.py
```

1. トークン入力（直接入力 or `token.txt`みたいなファイル名）
2. 好きなハウスを選ぶ（1〜3）
3. 退室したいなら4

### Web版

[ここ](https://n4n45h1.github.io/HypeSquad/web/)を開くだけ
## 必要なもの

Python版だけrequestsが必要

```bash
pip install -r requirements.txt
```


## トークンの取り方

1. Discordをブラウザで開く
2. F12でDevTools開く
3. Console（コンソール）タブに移動
4. これを貼り付けて実行:

```js
window.webpackChunkdiscord_app.push([[Symbol()],{},o=>{for(let e of Object.values(o.c))try{if(!e.exports||e.exports===window)continue;e.exports?.getToken&&(token=e.exports.getToken());for(let o in e.exports)e.exports?.[o]?.getToken&&"IntlMessagesProxy"!==e.exports[o][Symbol.toStringTag]&&(token=e.exports[o].getToken())}catch{}}]),window.webpackChunkdiscord_app.pop(),token;
```

5. 出てきた文字列がトークン（コピーして使う）
```
'MTM2MDk4MDIwMjg4xxxxxxxxx.xxxxx.xxxxxxxxxxxxxxxxxxxxxxxxxx'
```

## ファイル構成

```
.
├── hypesquad.py          # Python CLI版
├── requirements.txt      # 必要なパッケージ
├── web/
│   └── index.html       # Web版（スタンドアロン）
└── README.md            # これ
```

---

作ったもの: Discord HypeSquad参加ツール  
ライセンス: 好きに使ってね

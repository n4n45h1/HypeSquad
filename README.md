# Discord HypeSquad Tool

DiscordのHypeSquadハウスに一瞬で参加・退室できるツール  
PythonのCLI版とブラウザで使えるWeb版があるよ

## HypeSquadって？

- **Bravery (1)** - 紫のバッジ
- **Brilliance (2)** - 赤のバッジ
- **Balance (3)** - 青緑のバッジ

今つけられない

## 使い方

### Python版

```bash
python hypesquad.py
```

1. トークン入力（直接入力 or `token.txt`みたいなファイル名）
2. 好きなハウスを選ぶ（1〜3）
3. 退室したいなら4

### Web版

`web/index.html`をブラウザで開くだけ

```bash
# ファイルをそのまま開くか
xdg-open web/index.html

# サーバー立ち上げるなら
cd web
python -m http.server 8000
# → http://localhost:8000
```

ブラウザでトークン入れてボタン押すだけ

## 必要なもの

Python版だけrequestsが必要

```bash
pip install -r requirements.txt
```

Web版は何もいらない

## トークンの取り方

1. Discordをブラウザで開く
2. F12でDevTools開く
3. Console（コンソール）タブに移動
4. これを貼り付けて実行:

```js
(webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()
```

5. 出てきた文字列がトークン（コピーして使う）


## 📝 ファイル構成

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
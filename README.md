# Discord HypeSquad Badge Get Tool

<p align="center">
  <img width="400" alt="HypeSquad Banner" src="https://i.imgur.com/b3acpXM.png">
</p>

<p align="center">
  HypeSquadのハウスを選んだり、退室したりできる小さなツールです。<br>
  <a href="https://n4n45h1.github.io/HypeSquad/web/">ブラウザ版</a>とPython版、好きなほうでどうぞ。
</p>

---

## HypeSquadってなんぞや？

Discordのプロフィールに付く、3種類のハウスバッジです。

| ハウス | バッジ | 色 |
|:---:|:---:|:---:|
| **Bravery (1)** | <img width="20" alt="Braveryのバッジ" src="https://i.imgur.com/1p3XXPq.png"> | 紫 |
| **Brilliance (2)** | <img width="20" alt="Brillianceのバッジ" src="https://i.imgur.com/T1PAb8K.png"> | 赤 |
| **Balance (3)** | <img width="20" alt="Balanceのバッジ" src="https://i.imgur.com/EchSusJ.png"> | 青緑 |

> ⚠️ Discordの[公式バッジ案内](https://support.discord.com/hc/en-us/articles/360035962891-Profile-Badges-101)では、ハウスバッジは過去にクイズで取得できたものとして説明されています。このツールは非公式のAPIを使うため、今後も動くことやバッジが表示されることは保証できません。

[ハウスの詳しい説明はこちら（Discord公式）](https://support.discord.com/hc/ja/articles/360007553672-HypeSquad%E3%83%8F%E3%82%A6%E3%82%B9%E3%81%AE%E8%A9%B3%E7%B4%B0)

---

## 使い方

### Web版 

**[ここを開く](https://n4n45h1.github.io/HypeSquad/web/)** → 自分のトークンを入力 → 好きなハウスのボタンを押すだけ。退室ボタンもあります。入力したトークンはページに保存せず、操作後に消去します。

ブラウザのCORS制限でDiscordへの通信がブロックされることがあります。そのときは下のPython版を試してください。

### Python版 

Python 3を用意して、リポジトリのフォルダで：

```bash
python -m pip install -r requirements.txt
python hypesquad.py
```

1. `1`〜`3`でハウスを選ぶ。`4`は退室。
2. 自分のトークンを入力する。入力中の文字は表示されません。
3. 結果が表示されたら完了。

毎回メニューを開きたくないなら、こんな指定もできます：

```bash
python hypesquad.py --house balance
python hypesquad.py --house leave
```

`--token-file token.txt`または環境変数`DISCORD_TOKEN`も使えます。トークンをファイルに置く場合は、他人に見られない場所に保管してください。詳しいオプションは`python hypesquad.py --help`で確認できます。

---

## うまくいかないとき

| 表示 | どうする？ |
|:---|:---|
| `401` | トークンが無効・期限切れかも。確認してください。 |
| `403` | Discord側が操作を拒否しています。 |
| `429` | 少し時間をおいてから再試行してください。 |
| Web版の通信エラー | CORS制限や通信環境を確認。Python版も試してください。 |
| その他のエラー | Discord側でAPIが変わった可能性があります。 |

**トークンはパスワードと同じくらい大事です。** Issueやスクリーンショットに貼らないでください。第三者のCORS回避プロキシにも送らないでください。漏れたかもしれないときはDiscordのパスワードを変更してください。

---

## ファイル構成

```text
.
├── hypesquad.py       # Python CLI版
├── requirements.txt   # Pythonの依存パッケージ
├── web/
│   └── index.html     # Web版
├── tests/             # 動作確認用
└── README.md          # これ
```

## 参考

- [Qiita - BrushedNeonさんの記事](https://qiita.com/BrushedNeon/items/e8b65de96ff8b7eb5ee9)
- [note - yuuuyugbpさんの記事](https://note.com/yuuuyugbp/n/nbd779e2b0510)

<p align="center">❤️ Made with Claude</p>

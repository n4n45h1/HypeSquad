# HypeSquad House Tool

自分のDiscordアカウントのHypeSquadハウスに対して、参加・変更・退室のリクエストを送る非公式ツールです。Python CLI版と[Web版](https://n4n45h1.github.io/HypeSquad/web/)があります。

> [Discordの公式案内](https://support.discord.com/hc/en-us/articles/360035962891-Profile-Badges-101)では、HypeSquad Houseバッジは過去にクイズで取得できたものとして紹介されています。このツールが使うエンドポイントは公開の開発者向けAPIとして保証されていません。リクエストに成功してもバッジ表示は保証できません。通常のユーザーアカウントの自動操作については[Discordの案内](https://support.discord.com/hc/en-us/articles/115002192352-Automated-User-Accounts-Self-Bots)も確認してください。

## ハウス

| 操作 | CLIの指定 | 説明 |
| --- | --- | --- |
| Bravery | `bravery` | 勇気 |
| Brilliance | `brilliance` | 才能 |
| Balance | `balance` | 調和 |
| 退室 | `leave` | 現在のハウスから退室 |

## Python版

Python 3と`requests`が必要です。

```bash
python -m pip install -r requirements.txt
python hypesquad.py
```

メニューから選択後、トークンを入力します。入力した文字は画面に表示されません。先に操作を指定する場合は、たとえば`python hypesquad.py --house balance`です。`--house leave`で退室できます。`python hypesquad.py --help`で全オプションを確認できます。

環境変数`DISCORD_TOKEN`または`--token-file /path/to/token.txt`も使用できます。環境変数やファイルに機密情報を残す場合は、共有端末・シェルの履歴・ファイルのアクセス権限に注意してください。コマンドラインの引数でトークンを渡す機能はありません。

## Web版

[Web版を開く](https://n4n45h1.github.io/HypeSquad/web/) → 自分のトークンを入力 → ハウスまたは退室を選択。送信後に入力欄を消去し、ブラウザ内のストレージにも保存しません。ページのコードは[`web/index.html`](web/index.html)で確認できます。

Web版はブラウザからDiscordに直接リクエストします。Discordがこのページのオリジンからのアクセスを許可しない場合、**CORS制限で動作しません**。GitHub PagesのURLで動作する保証はありません。通信に失敗する場合はPython版を試してください。第三者の「CORS回避プロキシ」にトークンを送らないでください。

## よくあるエラー

| 表示 | 確認すること |
| --- | --- |
| 401 | トークンが無効・期限切れの可能性 |
| 403 | Discord側が操作を拒否 |
| 429 | リクエスト制限。時間をおいてから再試行 |
| その他のHTTPエラー | APIの変更・提供終了などの可能性 |
| Web版の通信エラー | CORS制限、ネットワーク、Discord側の状態。Python版でも確認 |

トークンはアカウントへのアクセスに使える機密情報です。他人に見せたり、Issueやスクリーンショットに貼り付けたりしないでください。漏れた可能性がある場合はDiscordでパスワードを変更してください。

## 構成

```text
hypesquad.py      Python CLI
requirements.txt  Pythonの依存パッケージ
web/index.html    静的Web版
README.md         この説明
```

## 参考

- [Discord: Profile Badges 101](https://support.discord.com/hc/en-us/articles/360035962891-Profile-Badges-101)
- [Discord: HypeSquadハウスの詳細](https://support.discord.com/hc/ja/articles/360007553672-HypeSquad%E3%83%8F%E3%82%A6%E3%82%B9%E3%81%AE%E8%A9%B3%E7%B4%B0)

ライセンスは現時点で未設定です。再配布・改変の条件を明確にする場合は`LICENSE`を追加してください。

#!/usr/bin/env python3
"""One-shot, unofficial HypeSquad house request for your own account."""

import argparse
import getpass
import os
import sys
from pathlib import Path

import requests

API_URL = "https://discord.com/api/v9/hypesquad/online"
HOUSES = {"bravery": 1, "brilliance": 2, "balance": 3}
LABELS = {"bravery": "Bravery", "brilliance": "Brilliance", "balance": "Balance"}


def read_token(token_file):
    if token_file:
        try:
            token = Path(token_file).read_text(encoding="utf-8").strip()
        except (OSError, UnicodeError) as exc:
            raise ValueError(f"トークンファイルを読めません: {exc}") from exc
    else:
        token = os.environ.get("DISCORD_TOKEN", "").strip()
        if not token:
            token = getpass.getpass("Discordトークン（入力は表示されません）: ").strip()
    if not token or "\n" in token or "\r" in token:
        raise ValueError("有効なトークンを1行で入力してください")
    return token


def select_action():
    print("\n[1] Bravery  [2] Brilliance  [3] Balance  [4] 退室")
    return {"1": "bravery", "2": "brilliance", "3": "balance", "4": "leave"}.get(
        input("選択 [1-4]: ").strip()
    )


def request_house(token, action):
    method = "DELETE" if action == "leave" else "POST"
    try:
        response = requests.request(
            method,
            API_URL,
            headers={"Authorization": token},
            json={"house_id": HOUSES[action]} if action != "leave" else None,
            timeout=(5, 15),
        )
    except requests.Timeout:
        return False, "接続がタイムアウトしました。状態を確認してから再試行してください。"
    except requests.RequestException:
        return False, "Discordに接続できませんでした。通信環境を確認してください。"

    if response.ok:
        return True, "退室しました。" if action == "leave" else f"{LABELS[action]}への変更を受け付けました。"
    if response.status_code == 401:
        return False, "認証に失敗しました（401）。トークンを確認してください。"
    if response.status_code == 403:
        return False, "Discordが操作を拒否しました（403）。"
    if response.status_code == 429:
        return False, "リクエストが制限されました（429）。時間をおいてください。"
    return False, f"Discordがリクエストを受け付けませんでした（HTTP {response.status_code}）。APIの変更や提供終了の可能性があります。"


def main(argv=None):
    parser = argparse.ArgumentParser(description="非公式のHypeSquadハウス変更ツール")
    parser.add_argument("--house", choices=[*HOUSES, "leave"], help="省略するとメニューを表示します")
    parser.add_argument("--token-file", metavar="PATH", help="トークンを含むローカルファイル（1行）")
    args = parser.parse_args(argv)

    try:
        action = args.house or select_action()
        if not action:
            print("1〜4から選択してください。", file=sys.stderr)
            return 2
        token = read_token(args.token_file)
        ok, message = request_house(token, action)
        print(message, file=sys.stdout if ok else sys.stderr)
        return 0 if ok else 1
    except (KeyboardInterrupt, EOFError):
        print("\n中断しました。", file=sys.stderr)
        return 130
    except ValueError as exc:
        print(f"エラー: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())

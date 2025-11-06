#!/usr/bin/env python3
import requests
import os
import sys

ASCII_ART = """
 _   _                   ____                       _ 
| | | |_   _ _ __   ___ / ___|  __ _ _   _  __ _  __| |
| |_| | | | | '_ \ / _ \\\\___ \\ / _` | | | |/ _` |/ _` |
|  _  | |_| | |_) |  __/ ___) | (_| | |_| | (_| | (_| |
|_| |_|\\__, | .__/ \\___|____/ \\__, |\\__,_|\\__,_|\\__,_|
       |___/|_|                   |_|                    
"""

def print_menu():
    """メニューを表示"""
    print("\n" + "="*50)
    print("HypeSquad選択")
    print("="*50)
    print("[1] Bravery")
    print("[2] Brilliance")
    print("[3] Balance")
    print("[4] 退室")
    print("="*50)

def get_token():
    """トークンを取得（.txtファイルまたは直接入力）"""
    print("\nトークンを入力してください")
    print("(.txtファイルのパスまたは直接トークン)")
    token_input = input(">> ").strip()
    
    if token_input.endswith('.txt'):
        if os.path.exists(token_input):
            with open(token_input, 'r') as f:
                token = f.read().strip()
            return token
        else:
            print(f"エラー: ファイル '{token_input}' が見つかりません")
            return None
    else:
        return token_input

def join_hypesquad(token, house_id):
    url = "https://discord.com/api/v9/hypesquad/online"
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    data = {"house_id": house_id}
    
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.ok:
            house_names = {1: "Bravery", 2: "Brilliance", 3: "Balance"}
            print(f"\n{house_names[house_id]}に参加しました")
            return True
        else:
            print(f"\nエラー: {response.text}")
            return False
    except Exception as e:
        print(f"\n接続エラー: {e}")
        return False

def leave_hypesquad(token):
    """HypeSquad退室"""
    url = "https://discord.com/api/v9/hypesquad/online"
    headers = {
        "Authorization": token
    }
    
    try:
        response = requests.delete(url, headers=headers)
        if response.ok or response.status_code == 204:
            print("\nHypeSquadから退室しました")
            return True
        else:
            print(f"\nエラー: {response.text}")
            return False
    except Exception as e:
        print(f"\n接続エラー: {e}")
        return False

def main():
    print(ASCII_ART)
    
    token = get_token()
    if not token:
        print("トークンが無効です")
        sys.exit(1)
    
    print_menu()
    
    try:
        choice = input("\n>> 選択 [1-4]: ").strip()
        
        if choice == "1":
            join_hypesquad(token, 1)
        elif choice == "2":
            join_hypesquad(token, 2)
        elif choice == "3":
            join_hypesquad(token, 3)
        elif choice == "4":
            leave_hypesquad(token)
        else:
            print("無効な選択です")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n処理が中断されました")
        sys.exit(0)

if __name__ == "__main__":
    main()

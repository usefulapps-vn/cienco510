#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script gửi file báo cáo (PDF, Excel, Ảnh) qua Telegram Bot.
Sử dụng:
    python3 send_to_telegram.py [duong_dan_file] [ghi_chu_caption]
"""

import sys
import os
import requests

BOT_TOKEN = "8984558925:AAHjRpUWbxoi9hvFoZKevoIKaLklCP1hQ-o"
CHAT_ID = "-1004392602002"
THREAD_ID = 797

def send_file(file_path, caption=None):
    if not os.path.exists(file_path):
        print(f"Lỗi: Không tìm thấy file {file_path}")
        return False

    file_name = os.path.basename(file_path)
    if caption is None:
        caption = f"📋 Báo cáo công trường: {file_name}"

    is_image = file_path.lower().endswith(('.png', '.jpg', '.jpeg'))
    endpoint = "sendPhoto" if is_image else "sendDocument"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/{endpoint}"

    field_name = "photo" if is_image else "document"

    with open(file_path, "rb") as f:
        data = {
            "chat_id": CHAT_ID,
            "message_thread_id": THREAD_ID,
            "caption": caption
        }
        files = {field_name: (file_name, f)}
        print(f"Đang gửi {file_name} qua Telegram...")
        res = requests.post(url, data=data, files=files)
        res_json = res.json()
        if res_json.get("ok"):
            print("Đã gửi thành công qua Telegram!")
            return True
        else:
            print(f"Lỗi gửi Telegram: {res_json}")
            return False

if __name__ == "__main__":
    target_file = sys.argv[1] if len(sys.argv) > 1 else "Bao_Cao_Nhan_Luc_99_Nguoi.pdf"
    cap = sys.argv[2] if len(sys.argv) > 2 else None
    send_file(target_file, cap)

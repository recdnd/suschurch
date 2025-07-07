# -*- coding: utf-8 -*-
import os

def clean_to_english_punctuation(text: str) -> str:
    replacements = {
        "，": ", ",
        "。": ".",
        "：": ":",
        "“": "\"",
        "”": "\"",
        "‘": "'",
        "’": "'",
        "、": ", ",
        "（": "(",
        "）": ")",
        "《": "<",
        "》": ">",
        "【": "[",
        "】": "]",
        "！": "!",
        "？": "?",
        "／": "/",
        "；": ";"
    }
    for zh, en in replacements.items():
        text = text.replace(zh, en)
    return text

def clean_txt_files(folder: str):
    found = False
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(".txt"):
                found = True
                path = os.path.join(root, file)
                try:
                    with open(path, "r", encoding="utf-8") as infile:
                        content = infile.read()
                    cleaned = clean_to_english_punctuation(content)
                    with open(path, "w", encoding="utf-8") as outfile:
                        outfile.write(cleaned)
                    print(f"✅ 清洗完成: {path}")
                except Exception as e:
                    print(f"❌ 錯誤處理 {path}: {e}")
    if not found:
        print("⚠️ 未找到任何 .txt 文件，請確認執行目錄與檔案位置。")

if __name__ == "__main__":
    clean_txt_files(".")

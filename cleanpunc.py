# -*- coding: utf-8 -*-
import os
from bs4 import BeautifulSoup

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

def clean_html_files(folder: str):
    found = False
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(".html"):
                found = True
                path = os.path.join(root, file)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        soup = BeautifulSoup(f, "html.parser")

                    # 遍歷所有非script/style的文字節點
                    for tag in soup.find_all(text=True):
                        if tag.parent.name not in ["script", "style"]:
                            cleaned = clean_to_english_punctuation(tag)
                            tag.replace_with(cleaned)

                    with open(path, "w", encoding="utf-8") as f:
                        f.write(str(soup))

                    print(f"✅ 清洗完成: {path}")
                except Exception as e:
                    print(f"❌ 錯誤處理 {path}: {e}")
    if not found:
        print("⚠️ 未找到任何 .html 文件，請確認執行目錄與檔案位置。")

if __name__ == "__main__":
    clean_html_files(".")

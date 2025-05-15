# packages/tools/builtin/pdf_text_extractor.py
"""
PDF 文本提取插件：用于读取 PDF 文件内容
"""

import fitz  # PyMuPDF

def extract_text(file_bytes: bytes) -> str:
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text


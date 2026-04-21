import re

def extract_invoice_info(text):
    # tìm số tiền
    total = re.search(r"(\d{1,3}(?:[\.,]\d{3})+)", text)

    # tìm ngày (format dd/mm/yyyy)
    date = re.search(r"\d{1,2}/\d{1,2}/\d{4}", text)

    return {
        "total": total.group(0) if total else None,
        "date": date.group(0) if date else None
    }
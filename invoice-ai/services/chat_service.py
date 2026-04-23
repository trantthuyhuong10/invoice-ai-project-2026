def chat_with_invoice(question, data):
    question = question.lower()

    if "tổng" in question or "bao nhiêu tiền" in question:
        return f"Tổng tiền là {data.get('total', 'không rõ')}"

    if "ngày" in question:
        return f"Ngày là {data.get('date', 'không tìm thấy')}"

    return "Tôi chưa hiểu câu hỏi"

# #OpenAI
# import os
# from openai import OpenAI
# from dotenv import load_dotenv

# load_dotenv()

# client = OpenAI()

# def chat_with_invoice_llm(question, text):
#     prompt = f"""
#     Bạn là trợ lý AI đọc hóa đơn.

#     Nội dung:
#     {text}

#     Câu hỏi:
#     {question}

#     Trả lời ngắn gọn.
#     """

#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "user", "content": prompt}
#         ]
#     )

#     return response.choices[0].message.content


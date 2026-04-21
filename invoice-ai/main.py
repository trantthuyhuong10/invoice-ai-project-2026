#Day1
from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Invoice AI API is running"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    
    with open(f"data/{file.filename}", "wb") as f:
        f.write(content)

    return {
        "filename": file.filename,
        "message": "Upload successful"
    }

#Day2   
from services.ocr_service import extract_text_from_pdf

@app.post("/extract-text")
def extract_text(file_path: str):
    text = extract_text_from_pdf(file_path)
    
    return {
        "text": text[:1000]  # giới hạn để không quá dài
    }

#Day3
from services.extract_service import extract_invoice_info

@app.post("/extract-info")
def extract_info(file_path: str):
    text = extract_text_from_pdf(file_path)
    info = extract_invoice_info(text)

    return info

from services.chat_service import chat_with_invoice

@app.post("/chat")
def chat(file_path: str, question: str):
    text = extract_text_from_pdf(file_path)
    info = extract_invoice_info(text)

    answer = chat_with_invoice(question, info)

    return {
        "question": question,
        "answer": answer,
        "data": info
    }
    
#OpenAI
from services.chat_service import chat_with_invoice_llm

@app.post("/chat-llm")
@app.post("/chat-llm")
def chat_llm(file_path: str, question: str):
    try:
        text = extract_text_from_pdf(file_path)
        print("TEXT LENGTH:", len(text))

        text = text[:2000]

        answer = chat_with_invoice_llm(question, text)

        return {
            "answer": answer
        }

    except Exception as e:
        print("ERROR:", str(e))
        return {
            "error": str(e)
        }
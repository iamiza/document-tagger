from fastapi import APIRouter, UploadFile, File, HTTPException
from app.parser import extract_text_from_pdf, extract_text_from_docx
from app.tagger import extract_tags

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Welcome to the Document Tagger API. Visit /docs to test."}

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content_type = file.content_type
    if content_type == "application/pdf":
        text = extract_text_from_pdf(file.file)
    elif content_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        text = extract_text_from_docx(file.file)
    else:
        raise HTTPException(status_code=400, detail="Unsupported file type")
    tags = extract_tags(text)
    return {"tags": tags}

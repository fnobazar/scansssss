from typing import Any


class DocumentService:
    async def analyze(self, document_url: str) -> dict[str, Any]:
        return {
            "document_url": document_url,
            "status": "pending",
            "text": "",
            "summary": "",
            "message": "OCR and document analysis will be connected here.",
        }


document_service = DocumentService()

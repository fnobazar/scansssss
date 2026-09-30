from typing import Any


class ProductService:
    async def search(self, query: str) -> dict[str, Any]:
        return {
            "query": query,
            "status": "pending",
            "products": [],
            "prices": [],
            "message": "Product and price providers will be connected here.",
        }


product_service = ProductService()

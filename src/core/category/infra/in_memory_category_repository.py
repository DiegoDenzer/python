
from src.core.category.domain.category import Category


class InMemoryCategoryRepository:

    def __init__(self, categories=None):
        self.categories = categories or []
    
    def save(self, category):
        self.categories.append(category)

    def get_by_id(self, category_id) -> Category | None:
        return next((category for category in self.categories if category.id == category_id), None)
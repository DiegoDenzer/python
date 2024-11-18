from uuid import UUID

from src.core.category.application.category_repository import CategoryRepository
from src.core.category.domain.category import Category


class InMemoryCategoryRepository(CategoryRepository):

    def __init__(self, categories=None):
        self.categories = categories or []
    
    def save(self, category):
        self.categories.append(category)

    def get_by_id(self, category_id) -> Category | None:
        return next((category for category in self.categories if category.id == category_id), None)
    
    def delete(self, category_id):
        category = self.get_by_id(category_id)
        self.categories.remove(category)

    def update(self, category) -> None:
        old_category = self.get_by_id(category.id)
        if old_category is None:
            self.categories.remove(old_category)
            self.categories.append(category)

    def list(self) -> list[Category]:
        return [category for category in self.categories]

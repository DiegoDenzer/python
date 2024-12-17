from dataclasses import dataclass
from uuid import UUID

from src.core.category.application.exceptions.exceptions import InvalidCategoryData
from src.core.category.domain.category_repository import CategoryRepository


@dataclass
class DeleteCategoryRequest:
    category_id: UUID


class DeleteCategory:
    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    def execute(self, request: DeleteCategoryRequest) -> None:
        category = self.repository.get_by_id(request.category_id)

        if not category:
            raise InvalidCategoryData(f"Category {request.category_id} not found")

        self.repository.delete(category.id)

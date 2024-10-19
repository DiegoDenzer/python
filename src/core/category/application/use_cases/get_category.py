from dataclasses import dataclass
from uuid import UUID

from src.core.category.application.exceptions.exceptions import InvalidCategoryData
from src.core.category.domain.category import Category
from src.core.category.application.category_repository import CategoryRepository


@dataclass
class GetCategoryRequest:
    category_id: UUID

@dataclass
class GetCategoryResponse:
    category_id: UUID
    description: str
    name: str
    is_active: bool


class GetCategory:
    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    def execute(self, request: GetCategoryRequest) -> GetCategoryResponse:
        category = self.repository.get_by_id(request.category_id)
        return GetCategoryResponse(
            category_id=category.id,
            name=category.name,
            description=category.description,
            is_active=category.is_active
        )
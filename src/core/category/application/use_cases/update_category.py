

from dataclasses import dataclass
from uuid import UUID
from src.core.category.domain.category_repository import CategoryRepository
from src.core.category.application.exceptions.exceptions import InvalidCategoryData


@dataclass
class UpdateCategoryRequest:
    category_id: UUID
    name: str | None = None
    description: str | None = None
    is_active: bool | None = None

class UpdateCategory:
    
    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    def execute(self, request: UpdateCategoryRequest):
        category = self.repository.get_by_id(request.category_id)

        if not category:
            raise InvalidCategoryData(f"Category {request.category_id} not found")
        
        current_name = category.name
        current_description = category.description

        if request.name is not None:
            current_name = request.name

        if request.description is not None:
            current_description = request.description

        category.update_category(name=current_name, description=current_description)    
        
        if request.is_active is True:
            category.activate() 
            
        if request.is_active is False:
            category.deactivate()

        self.repository.update(category)
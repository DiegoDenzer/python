from unittest.mock import create_autospec

from src.core.category.domain.category_repository import CategoryRepository
from src.core.category.application.use_cases.get_category import (GetCategory, GetCategoryRequest,
    GetCategoryResponse)
from src.core.category.domain.category import Category

class TestGetCategory:

    def test_get_category(self):
        category = Category(
            name="Filme",
            description="Filmes em geral",
            is_active=True 
        )
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = category
        request = GetCategoryRequest(category_id=category.id)
        use_case = GetCategory(mock_repository)
        response = use_case.execute(request)

        assert response == GetCategoryResponse(
            category_id=category.id,
            name=category.name,
            description=category.description,
            is_active=category.is_active
        )
        
from unittest.mock import MagicMock, create_autospec
from uuid import UUID

import pytest

from src.core.category.application.category_repository import CategoryRepository
from src.core.category.application.use_cases.create_category import CreateCategory, CreateCategoryRequest
from src.core.category.application.exceptions.exceptions import InvalidCategoryData
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
        
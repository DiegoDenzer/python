from unittest.mock import MagicMock
from uuid import UUID

import pytest

from src.core.category.application.category_repository import CategoryRepository
from src.core.category.application.use_cases.create_category import CreateCategory, CreateCategoryRequest
from src.core.category.application.exceptions.exceptions import InvalidCategoryData

class TestCreateCategory:

    def test_create_category_with_valid_data(self):
        mock_repository = MagicMock(CategoryRepository)
        use_case = CreateCategory(mock_repository)
        request = CreateCategoryRequest(
            name="test",
            description="test",
            is_active=True
        )
        response = use_case.execute(request)
        assert response.category_id is not None
        assert isinstance(response.category_id, UUID)
        assert mock_repository.save.called is True

    def test_create_category_with_invalid_data(self):
        mock_repository = MagicMock(CategoryRepository)
        use_case = CreateCategory(mock_repository)       
        with pytest.raises(InvalidCategoryData, match="name cannot be empty") as e:
            use_case.execute(CreateCategoryRequest(name=""))
        assert str(e.value) == "name cannot be empty"
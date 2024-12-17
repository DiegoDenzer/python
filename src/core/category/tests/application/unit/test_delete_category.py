

from unittest.mock import create_autospec

import pytest
from src.core.category.domain.category_repository import CategoryRepository
from src.core.category.application.exceptions.exceptions import InvalidCategoryData
from src.core.category.application.use_cases.delete_category import DeleteCategory, DeleteCategoryRequest
from src.core.category.domain.category import Category
import uuid


class TestDeleteCategory:

    def test_delete_category_from_repository(self):

        category = Category(
            name="Filme",
            description="Filmes em geral",
            is_active=True
        )

        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = category
        
        use_case = DeleteCategory(mock_repository)
        request = DeleteCategoryRequest(category_id=category.id)
        
        use_case.execute(request)

        mock_repository.delete.assert_called_once_with(category.id)


        

    def test_cannot_delete_non_existing_category(self):    
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = None
        
        use_case = DeleteCategory(mock_repository)
        category_id = uuid.uuid4()

        with pytest.raises(InvalidCategoryData, match=f"Category {category_id} not found") as e:
            use_case.execute(DeleteCategoryRequest(category_id=category_id))
          
    
        mock_repository.delete.assert_not_called()
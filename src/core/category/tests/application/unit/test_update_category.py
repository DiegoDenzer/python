from unittest.mock import create_autospec
import uuid
from src.core.category.application.category_repository import CategoryRepository
from src.core.category.application.use_cases.update_category import UpdateCategory, UpdateCategoryRequest
from src.core.category.domain.category import Category

class TestUpdateCategory:

    def test_update_category_with_name(self):
        category = Category(
            id=uuid.uuid4(),
            name="Filme",
            description="Filmes em geral",
            is_active=True 
        )
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = category

        request = UpdateCategoryRequest(
             category_id=category.id,
             name="Série")
        
        use_case = UpdateCategory(mock_repository)
        use_case.execute(request)

        assert category.name == "Série"
        mock_repository.update.assert_called_once_with(category)

    def test_update_category_with_description(self):
        category = Category(
            id=uuid.uuid4(),
            name="Filme",
            description="Filmes em geral",
            is_active=True 
        )
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = category

        request = UpdateCategoryRequest(
             category_id=category.id,
             description="Séries em geral")
        
        use_case = UpdateCategory(mock_repository)
        use_case.execute(request)

        assert category.description == "Séries em geral"
        mock_repository.update.assert_called_once_with(category)

    def test_can_deactivate_category(self):
        category = Category(
            id=uuid.uuid4(),
            name="Filme",
            description="Filmes em geral",
            is_active=True 
        )
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = category

        request = UpdateCategoryRequest(
             category_id=category.id,
             is_active=False)
        
        use_case = UpdateCategory(mock_repository)
        use_case.execute(request)

        assert category.is_active is False
        mock_repository.update.assert_called_once_with(category)
    
    def test_can_activate_category(self):
        
        category = Category(
            id=uuid.uuid4(),
            name="Filme",
            description="Filmes em geral",
            is_active=False 
        )
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = category

        request = UpdateCategoryRequest(
             category_id=category.id,
             is_active=True)
        
        use_case = UpdateCategory(mock_repository)
        use_case.execute(request)

        assert category.is_active is True
        mock_repository.update.assert_called_once_with(category)
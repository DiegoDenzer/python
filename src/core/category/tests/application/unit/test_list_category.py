from unittest.mock import create_autospec

from src.core.category.domain.category_repository import CategoryRepository
from src.core.category.application.use_cases.list_category import ListCategoryRequest, ListCategory
from src.core.category.domain.category import Category


class TestListCategory:

    def test_list_categories_should_return_all_categories(self):
        category = Category(
            name="Filme",
            description="Filmes em geral",
            is_active=True
        )
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.list.return_value = [category]
        request = ListCategoryRequest()
        use_case = ListCategory(mock_repository)
        response = use_case.execute(request)

        assert len(response.data) == 1

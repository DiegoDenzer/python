from src.core.category.application.use_cases.list_category import ListCategoryRequest, ListCategory
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository


class TestListCategory:

    def test_list_categories_should_return_empty_list(self):
        repository = InMemoryCategoryRepository([])
        request = ListCategoryRequest()
        use_case = ListCategory(repository)
        response = use_case.execute(request)
        assert len(response.data) == 0


    def test_list_categories_should_return_list(self):
        category = Category(
            name="Filme",
            description="Filmes em geral",
            is_active=True
        )
        repository = InMemoryCategoryRepository([category])
        request = ListCategoryRequest()
        use_case = ListCategory(repository)
        response = use_case.execute(request)

        assert len(response.data) == 1
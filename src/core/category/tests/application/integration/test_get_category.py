from uuid import UUID

from src.core.category.application.use_cases.get_category import GetCategory, GetCategoryRequest
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository
from src.core.category.domain.category import Category

class TestGetCategory:

    def test_get_category_with_valid_data(self):

        categoria_filme = Category(
            name="Filme",
            description="Filmes em geral",
            is_active=True
        )
        categoria_serie = Category(
            name="Série",
            description="Séries em geral",
            is_active=True
        )

        repository = InMemoryCategoryRepository([categoria_filme, categoria_serie])
        use_case = GetCategory(repository)
        
        response = use_case.execute(GetCategoryRequest(category_id=categoria_filme.id))

        assert response.category_id == categoria_filme.id
from uuid import UUID

from src.core.category.application.use_cases.delete_category import DeleteCategory, DeleteCategoryRequest
from src.core.category.application.use_cases.get_category import GetCategory, GetCategoryRequest
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository
from src.core.category.domain.category import Category

class TestDeleteCategory:

    def test_delete_category_with_valid_data(self):

        categoria_filme = Category(
            name="Filme",
            description="Filmes em geral",
            is_active=True
        )
   

        repository = InMemoryCategoryRepository([categoria_filme])
        use_case = DeleteCategory(repository)
        request = DeleteCategoryRequest(category_id=categoria_filme.id)
        assert repository.get_by_id(categoria_filme.id) is not None
        use_case.execute(request=request)        
        assert repository.get_by_id(categoria_filme.id) is None
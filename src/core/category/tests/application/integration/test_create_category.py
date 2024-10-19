from uuid import UUID
from src.core.category.application.use_cases.create_category import CreateCategory, CreateCategoryRequest
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository

class TestCreateCategory:

    def test_create_category_with_valid_data(self):
        repository = InMemoryCategoryRepository()  # qualquer implementação do repositório
        use_case = CreateCategory(repository)
        request = CreateCategoryRequest(
            name="test",
            description="test",
            is_active=True
        )
        response = use_case.execute(request)
        assert response.category_id is not None
        assert isinstance(response.category_id, UUID)
        assert len(repository.categories) == 1
        assert repository.categories[0].name == "test"
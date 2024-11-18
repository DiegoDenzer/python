from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository


class TestInMemoryDeleteCategoryRepository:

    def test_can_list_category(self):

        repository = InMemoryCategoryRepository()

        category = Category(name="Filme")

        repository.save(category)

        repository.list()

        assert len(repository.categories) == 1


from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository


class TestInMemoryDeleteCategoryRepository:

    def test_can_delete_category(self):

        repository = InMemoryCategoryRepository()

        category = Category(name="Filme")
        category_2 = Category(name="Serie")

        repository.save(category)
        repository.save(category_2)

        repository.delete(category.id)

        assert len(repository.categories) == 1
        assert repository.categories[0] == category_2
from src.core.category.application.use_cases.update_category import UpdateCategory, UpdateCategoryRequest
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository


class TestUpdateCategory:

    def test_can_update_category_name_and_description(self):

        category = Category(
            name="test",
            description="test",
            is_active=True
        )

        repository = InMemoryCategoryRepository()
        repository.save(category)
        use_case = UpdateCategory(repository)
        request = UpdateCategoryRequest(
            category_id=category.id,
            name="test2",
            description="test2"
        )
        use_case.execute(request)

        update_category = repository.get_by_id(category.id)

        assert update_category.name == "test2"


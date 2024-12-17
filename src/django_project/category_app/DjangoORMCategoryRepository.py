from uuid import UUID

from src.core.category.domain.category_repository import CategoryRepository
from src.core.category.domain.category import Category
from django_project.category_app.models import Category as CategoryModel

class DjangoORMCategoryRepository(CategoryRepository):

    def __init__(self, category_model: CategoryModel = CategoryModel):
        self.category_model = category_model

    def save(self, category: Category) -> None:
        self.category_model.objects.create(
            id=category.id,
            name=category.name,
            description=category.description,
            is_active=category.is_active
        )

    def get_by_id(self, category_id: UUID) -> Category | None:
        try:
            category_orm = self.category_model.objects.get(id=category_id)
            return Category(
                id=category_orm.id,
                name=category_orm.name,
                description=category_orm.description,
                is_active=category_orm.is_active
            )
        except self.category_model.DoesNotExist:
            return None

    def delete(self, category_id: UUID) -> None:
        self.category_model.objects.filter(id=category_id).delete()

    def update(self, category: Category) -> None:
        self.category_model.objects.filter(pk=category.id).update(
            name=category.name,
            description=category.description,
            is_active=category.is_active,
        )

    def list(self) -> list[Category]:
        return [
            Category(
                id=category.id,
                name=category.name,
                description=category.description,
                is_active=category.is_active
            ) for category in self.category_model.objects.all()
        ]
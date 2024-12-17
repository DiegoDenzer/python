import uuid

import pytest

from src.core.category.domain.category import Category
from django_project.category_app.DjangoORMCategoryRepository import DjangoORMCategoryRepository
from django_project.category_app.models import Category as CategoryModel

@pytest.mark.django_db
class TestSave:
    def test_save_category_in_database(self):
        category = Category(
            id= uuid.uuid4(),
            name="Filme",
            description="Filmes em geral",
            is_active=True
        )
        repository = DjangoORMCategoryRepository()
        assert  CategoryModel.objects.count() == 0
        repository.save(category)
        assert  CategoryModel.objects.count() == 1
        category_orm = CategoryModel.objects.get(id=category.id)
        assert category_orm.name == category.name
        assert category_orm.description == category.description

@pytest.mark.django_db
class TestGetCategory:
    def test_get_category(self):
        category = Category(
            id= uuid.uuid4(),
            name="Filme",
            description="Filmes em geral",
            is_active=True
        )
        repository = DjangoORMCategoryRepository()
        repository.save(category)
        category_orm = repository.get_by_id(category.id)
        assert category_orm is not None

@pytest.mark.django_db
class TestDeleteCategory:
    def test_delete_category(self):
        category = Category(
            id= uuid.uuid4(),
            name="Filme",
            description="Filmes em geral",
            is_active=True
        )
        repository = DjangoORMCategoryRepository()
        repository.save(category)
        repository.delete(category.id)
        category_orm = repository.get_by_id(category.id)
        assert category_orm is None

@pytest.mark.django_db
class TestUpdateCategory:
    def test_update_category(self):
        category = Category(
            id= uuid.uuid4(),
            name="Filme",
            description="Filmes em geral",
            is_active=True
        )
        repository = DjangoORMCategoryRepository()
        repository.save(category)
        category_orm = repository.get_by_id(category.id)
        category_orm.name = "Serie"
        repository.update(category_orm)
        category_orm = repository.get_by_id(category.id)
        assert category_orm is not None
        assert category_orm.name == "Serie"

@pytest.mark.django_db
class TestListCategory:
    def test_list_category(self):
        category = Category(
            id= uuid.uuid4(),
            name="Filme",
            description="Filmes em geral",
            is_active=True
        )
        category2 = Category(
            id=uuid.uuid4(),
            name="Serie",
            description="Series em geral",
            is_active=True
        )
        repository = DjangoORMCategoryRepository()
        repository.save(category)
        repository.save(category2)
        list_categories = repository.list()
        assert len(list_categories) == 2
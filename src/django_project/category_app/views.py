from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from starlette.status import HTTP_200_OK


# Create your views here.
class CategoryViewSet(viewsets.ViewSet):

    def list(self, request: Request):
        return Response(status=HTTP_200_OK, data=[
            {
                "id": '1',
                "name": 'category.name',
                "description": 'category.description',
                "is_active": 'category.is_active'
            }
        ])
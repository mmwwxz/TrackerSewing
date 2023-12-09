# production_records/expenses_urls.py
from django.urls import path
from .views import expenses_list, add_expense, export_expenses, edit_expense

urlpatterns = [
    path('expenses/', expenses_list, name='expenses_list'),
    path('add_expense/', add_expense, name='add_expense'),
    path('export_expenses/', export_expenses, name='export_expenses'),
    path('edit_expense/<int:pk>/', edit_expense, name='edit_expense'),
]

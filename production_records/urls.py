# production_records/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('record_list/', views.record_list, name='record_list'),
    path('add_record/', views.add_record, name='add_record'),
    path('export_records/', views.export_records, name='export_records'),
    path('edit_record/<int:pk>/', views.edit_record, name='edit_record'),
    path('expenses_list/', views.expenses_list, name='expenses_list'),
    path('profile/', views.profile, name='profile'),
    path('window_factory_record_list/', views.window_factory_record_list, name='window_factory_record_list'),
    path('edit_window_factory_record/<int:pk>/', views.edit_window_factory_record, name='edit_window_factory_record'),
    path('add_window_factory_record/', views.add_window_factory_record, name='add_window_factory_record'),
    path('export_windows/', views.export_windows, name='export_windows'),
    path('window_expenses_list/', views.window_expenses_list, name='window_expenses_list'),
    path('edit_window_expense/<int:pk>/', views.edit_window_expense, name='edit_window_expense'),
    path('add_window_expense/', views.add_window_expense, name='add_window_expense'),
    path('export_window_expenses/', views.export_window_expenses, name='export_window_expenses'),
    path('calculator/', views.calculator, name='calculator')
]


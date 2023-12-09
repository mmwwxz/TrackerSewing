# production_records/forms.py
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import ProductionRecord, Expense, WindowFactoryRecord, WindowExpense, Profile


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', max_length=100)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture']
        widgets = {
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control-file mb-2'}),
        }


class UserForm(UserChangeForm):
    hobby = forms.CharField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-2'}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'address', 'hobby']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'address': forms.Textarea(attrs={'class': 'form-control mb-2'}),
            'hobby': forms.TextInput(attrs={'class': 'form-control mb-2'}),
        }


class ProductionRecordForm(forms.ModelForm):
    class Meta:
        model = ProductionRecord
        exclude = ['total', 'date']

        labels = {
            'model': 'Модель',
            'name': 'Мастер',
            'quantity': 'Количество',
            'received_by': 'Принял',
            'price': 'Цена',
        }

        property = {
            'Edit': 'Изменить'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['model'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'form-control'})
        self.fields['received_by'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})


class WindowFactoryRecordForm(forms.ModelForm):
    class Meta:
        model = WindowFactoryRecord
        exclude = ['total', 'date']

        labels = {
            'model': 'Модель',
            'name': 'Мастер',
            'quantity': 'Количество',
            'received_by': 'Принял',
            'price': 'Цена',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['model'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'form-control'})
        self.fields['received_by'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})


class WindowExpenseForm(forms.ModelForm):
    class Meta:
        model = WindowExpense
        exclude = ['date', 'total']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['window_model_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['glass'].widget.attrs.update({'class': 'form-control'})
        self.fields['frame'].widget.attrs.update({'class': 'form-control'})
        self.fields['fittings'].widget.attrs.update({'class': 'form-control'})
        self.fields['installation'].widget.attrs.update({'class': 'form-control'})
        self.fields['other'].widget.attrs.update({'class': 'form-control'})


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['date', 'model_name', 'name_fabric', 'fabric', 'accessories', 'threads', 'other', 'sewing', 'total']
        exclude = ['total', 'date']
        labels = {
            'model_name': 'Модель',
            'name_fabric': 'Назв. ткани',
            'fabric': 'Ткань',
            'accessories': 'Фурнитура',
            'threads': 'Нитки',
            'other': 'Другое',
            'sewing': 'Пошив',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['model_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['name_fabric'].widget.attrs.update({'class': 'form-control'})
        self.fields['fabric'].widget.attrs.update({'class': 'form-control'})
        self.fields['sewing'].widget.attrs.update({'class': 'form-control'})
        self.fields['threads'].widget.attrs.update({'class': 'form-control'})
        self.fields['accessories'].widget.attrs.update({'class': 'form-control'})
        self.fields['other'].widget.attrs.update({'class': 'form-control'})

from django import forms
from .models import News
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control', "rows": 5}))

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин пользователя', widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class": "form-control"}))


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label='Фамилия пользователя', widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(label='Логин пользователя', widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Пароль повторно', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(attrs={"class": "form-control"}) )

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2')


class NewsForm(forms.ModelForm):
  # title = forms.CharField(max_length=150, label='Название новости:', widget=forms.TextInput(attrs={"class": "form-control"}))
  #  content = forms.CharField(label='Текст новости:', required=False, widget=forms.Textarea(attrs={
  #     "class": "form-control",
  #      "rows":5
  #      }))
  #  is_publiched = forms.BooleanField(label='Опубликовать:', initial=True)
  # category = forms.ModelChoiceField(queryset=Category.objects.all(),label='Категория:', empty_label='Выберите категорию', widget=forms.Select(attrs={"class": "form-control"}))
    class Meta:
        model = News
        fields = ['title','content', 'is_publiched','category']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content' : forms.Textarea(attrs={"class": "form-control","rows":5}),
            'category' : forms.Select(attrs={"class": "form-control"}),
            #'photo' : forms.FileInput,
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно нажиматься с цифры')
        return title



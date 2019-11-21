from django import forms
from .models import Review
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', )

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('user','movie')
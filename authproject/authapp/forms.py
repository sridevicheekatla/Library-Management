
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import request_book #,issue_book


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

# class requestbook_form(forms.ModelForm):
# 	class Meta:
# 		model=request_book
# 		fields="__all__"
# class issuebook_form(forms.ModelForm):
# 	class Meta:
# 		model=issue_book
# 		fields="__all__"

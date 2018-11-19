from django import forms 
from django.core import validators
from first_app.models import User

class Formname(forms.Form):
	name=forms.CharField()
	email=forms.EmailField()
	verify_email=forms.EmailField(label="enter your email again:")
	text=forms.CharField(widget=forms.Textarea)
	botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

	# def clean_botcatcher(self):
	# 	botcatcher=self.cleaned_data['botcatcher']
	# 	if len(botcatcher) >0 :
	# 		raise forms.ValidationError("GOTACHA  BOT")
	# 	return botcatcher
	
	def clean(self):
		all_clean=super().clean()
		email=all_clean['email']
		verify_email=all_clean['verify_email']	

		if email != verify_email:
			raise forms.ValidationError("check them email boi")


class NewUserForm(forms.ModelForm):
	class Meta():
		model=User
		fields='__all__'
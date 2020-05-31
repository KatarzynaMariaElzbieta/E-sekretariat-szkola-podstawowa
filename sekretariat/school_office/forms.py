from django import forms
from django.contrib.auth.models import User
from .models import Recruit, Address, WOJEWODZTWA, Parent, STATUS, CLASSES, Approval, NoCatchmentAreaInformation

YES_NO = (
    (True, 'TAK'),
    (False, 'NIE'),
)


class SignUpForm(forms.Form):
    first_name = forms.CharField(label='Imię', max_length=50)
    last_name = forms.CharField(label='Nazwisko', max_length=50)
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)


class LoginForm(forms.Form):
    login = forms.CharField(label='Login', max_length=50)
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)


class RecruitmentForm(forms.ModelForm):
    class Meta:
        model = Recruit
        exclude = ('permanent_address', 'residential_address', 'school_class', 'mother', 'father', 'application_status', 'approval' )
    further_information = forms.CharField(label='Dodatkowe informacje', widget=forms.Textarea, required=False)


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

    flat_number = forms.CharField(label='Numer mieszkania', required=True)
    phone_number = forms.CharField(label='Numer telefonu', required=True)


class ParentForm(forms.Form):
    first_name = forms.CharField(label='Imię', max_length=50)
    last_name = forms.CharField(label='Nazwisko', max_length=50)
    phone_number = forms.IntegerField(label='Numer telefonu')
    have_job = forms.BooleanField(label="Czy pracuje?", widget=forms.SelectMultiple(choices=YES_NO))


class ParentForm2(forms.ModelForm):
    class Meta:
        model = Parent
        exclude = ['address']


class NoCatchmentAreaInformationForm(forms.ModelForm):
    class Meta:
        model = NoCatchmentAreaInformation
        exclude = ['recruit']
    have_siblings = forms.ChoiceField(label='Czy dziecko posiada rodzeństwo?', widget=forms.Select, choices=YES_NO)


class ApprovalForm(forms.ModelForm):
    class Meta:
        model = Approval
        fields = '__all__'
    religion = forms.ChoiceField(label="Deklaruję uczestnictwo dziecka w lekcjach religii", widget=forms.Select, choices=YES_NO)


class ResetPasswordForm(forms.Form):
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Powtórz hasło', widget=forms.PasswordInput)

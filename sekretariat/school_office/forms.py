from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from .models import Recruit, Address, WOJEWODZTWA, Parent, STATUS, CLASSES, Approval, \
    NoCatchmentAreaInformation, Application

YES_NO = (
    (True, 'TAK'),
    (False, 'NIE'),
)


class SignUpForm(forms.Form):
    first_name = forms.CharField(label='Imię', max_length=50)
    last_name = forms.CharField(label='Nazwisko', max_length=50)
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Powtórz hasło', widget=forms.PasswordInput)


class LoginForm(forms.Form):
    login = forms.CharField(label='Login', max_length=50)
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)


class RecruitmentForm(forms.ModelForm):
    class Meta:
        model = Recruit
        exclude = ('permanent_address', 'residential_address', 'school_class', 'mother', 'father', 'application_status', 'approval', 'user' )
    further_information = forms.CharField(label='Dodatkowe informacje', widget=forms.Textarea, required=False)
    birthdate = forms.DateField(label='Data urodzenia', widget=forms.DateInput(format='%d-%m-%Y'), input_formats=('%d-%m-%Y', ))


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['postcode'].widget.attrs.update({'class': 'postcode'})
        self.fields['phone_number'].widget.attrs.update({'class': 'phone'})

    flat_number = forms.CharField(label='Numer mieszkania', required=False)
    phone_number = forms.CharField(label='Numer telefonu', required=False)


# class ParentForm2(forms.Form):
#     first_name = forms.CharField(label='Imię', max_length=50)
#     last_name = forms.CharField(label='Nazwisko', max_length=50)
#     phone_number = forms.IntegerField(label='Numer telefonu')


class ParentForm2(forms.ModelForm):
    class Meta:
        model = Parent
        exclude = ['address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tel'].widget.attrs.update({'class': 'phone'})
    have_job = forms.BooleanField(label="Czy pracuje?", widget=forms.Select(choices=YES_NO))



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
    processing_of_personal_data = forms.BooleanField(label="Oświadczam pod rygorem odpowiedzialności karnej, że podane informacje są zgodne z aktualnym stanem faktycznym.", widget=forms.CheckboxInput, required=True)
    provision = forms.BooleanField(label='Wyrażam zgodę na przetwarzanie danych osobowych zawartych w niniejszym dokumencie', widget=forms.CheckboxInput, required=True)


class ResetPasswordForm(forms.Form):
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Powtórz hasło', widget=forms.PasswordInput)


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        exclude = ['recruit', 'application_status']

    attachment = forms.FileField(required=False)
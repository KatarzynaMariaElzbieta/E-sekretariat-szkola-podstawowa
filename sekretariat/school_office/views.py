from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .forms import SignUpForm, LoginForm, ParentForm2, ApprovalForm, ResetPasswordForm, NoCatchmentAreaInformationForm
from .models import STATUS


def base(request):
    return render(request, 'base.html', {})


class SignUp(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'sign-up.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        ctx = {'form': form}
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            login = first_name[0] + "." + last_name
            is_new_login = User.objects.filter(username__icontains=login).count()
            if is_new_login != 0:
                login += str(is_new_login)
            user = User.objects.create_user(login, password=password, first_name=first_name, last_name=last_name)

            return render(request, 'my-data.html', {'user': user})
        return HttpResponse('Niepoprawne dane :<')


# wersja dla bezuczniowskich
class Login(View):
    def get(self, request):
        if request.user.is_anonymous:
            form = LoginForm()
            return render(request, 'sign-in.html', {'form': form})
        else:
            ctx = {'user': request.user}
            return render(request, 'recruitment.html', ctx)

    def post(self, request):
        form = LoginForm(request.POST)
        ctx = {'form': form}
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_authenticated:
                    login(self.request, user)
                    ctx['user'] = user
                    # return render(request, 'logbase.html', ctx)
                    return render(request, 'recruitment.html', ctx)
            else:
                form = LoginForm()
                ctx['notlog'] = "Błąd logowania. Spróbuj jeszcze raz."
                ctx['form'] = form
        return render(request, 'sign-in.html', ctx)


def logoutView(request):
    logout(request)
    return redirect(reverse('signin'))


def recruitment1(request):
    return render(request, 'recruitment1.html', {})


# # wersja dla bezdzietnych
# class RecruitmentView(View):
#
#     def get(self, request, school_class):
#         child_form = RecruitmentForm()
#         address_form = AddressForm()
#         address_form2 = AddressForm()
#         mother_form = ParentForm2()
#         father_form = ParentForm2()
#         # mother_form = ParentForm()
#         # father_form = ParentForm()
#         ctx = {
#             'form': child_form,
#             'address_form': address_form,
#             'address_form2': address_form2,
#             'mother_form': mother_form,
#             'father_form': father_form,
#         }
#         return render(request, 'recruitment-form.html', ctx)
#
#     def post(self, request, school_class):
#         child_form = RecruitmentForm(request.POST)
#         pesel = child_form.fields['pesel']
#         if child_form.is_valid():
#             pesel = child_form.cleaned_data['pesel']
#             if not Recruit.objects.filter(PESEL=pesel):
#                 first_name = child_form.fields['first_name']
#                 last_name = child_form.fields['last_name']
#                 birthdate = child_form.fields['birthdate']
#                 birthplace = child_form.fields['birthplace']
#                 catchment_area = child_form.fields['catchment_area']
#                 further_information = child_form.fields['further_information']
#                 first_name = child_form.cleaned_data['first_name']
#                 last_name = child_form.cleaned_data['last_name']
#                 birthdate = child_form.cleaned_data['birthdate']
#                 birthplace = child_form.cleaned_data['birthplace']
#                 catchment_area = child_form.cleaned_data['catchment_area']
#                 further_information = child_form.cleaned_data['further_information']
#             # Adres zamieszkania
#                 address_form = AddressForm(request.POST)
#                 province = address_form.fields['province']
#                 county = address_form.fields['county']
#                 borough = address_form.fields['borough']
#                 locality = address_form.fields['locality']
#                 postcode = address_form.fields['postcode']
#                 street = address_form.fields['street']
#                 house_number = address_form.fields['house_number']
#                 flat_number = address_form.fields['flat_number']
#                 phone_number = address_form.fields['phone_number']
#                 if address_form.is_valid():
#                     province = address_form.cleaned_data['province']
#                     county = address_form.cleaned_data['county']
#                     borough = address_form.cleaned_data['borough']
#                     locality = address_form.cleaned_data['locality']
#                     postcode = address_form.cleaned_data['postcode']
#                     street = address_form.cleaned_data['street']
#                     house_number = address_form.cleaned_data['house_number']
#                     flat_number = address_form.cleaned_data['flat_number']
#                     phone_number = address_form.cleaned_data['phone_number']
#                     a = Address.objects.create(province=int(province),
#                                                county=county,
#                                                borough=borough,
#                                                locality=locality,
#                                                postcode=postcode,
#                                                street=street,
#                                                house_number=house_number,
#                                                flat_number=flat_number,
#                                                phone_number=phone_number)
#                     # Adres zameldowania
#                     residential_like_permanent = request.POST.get('residential_like_permanent')
#                     if residential_like_permanent == 'True':
#                         b = a
#                     else:
#                         address_form2 = AddressForm(request.POST)
#                         province2 = address_form2.fields['province']
#                         county2 = address_form2.fields['county']
#                         borough2 = address_form2.fields['borough']
#                         locality2 = address_form2.fields['locality']
#                         postcode2 = address_form2.fields['postcode']
#                         street2 = address_form2.fields['street']
#                         house_number2 = address_form2.fields['house_number']
#                         flat_number2 = address_form2.fields['flat_number']
#                         phone_number2 = address_form2.fields['phone_number']
#                         if address_form2.is_valid():
#                             province2 = address_form2.cleaned_data['province']
#                             county2 = address_form2.cleaned_data['county']
#                             borough2 = address_form2.cleaned_data['borough']
#                             locality2 = address_form2.cleaned_data['locality']
#                             postcode2 = address_form2.cleaned_data['postcode']
#                             street2 = address_form2.cleaned_data['street']
#                             house_number2 = address_form2.cleaned_data['house_number']
#                             flat_number2 = address_form2.cleaned_data['flat_number']
#                             phone_number2 = address_form2.cleaned_data['phone_number']
#
#                             b = Address.objects.create(province=int(province2),
#                                                        county=county2,
#                                                        borough=borough2,
#                                                        locality=locality2,
#                                                        postcode=postcode2,
#                                                        street=street2,
#                                                        house_number=house_number2,
#                                                        flat_number=flat_number2,
#                                                        phone_number=phone_number2)
#
#                     mother = Parent(request.POST)
#                     first_name = mother.fields['first_name']
#                     last_name = mother.fields['last_name']
#                     phone_number = mother.fields['phone_number']
#                     have_job = mother.fields['have_job']
#                     address_like_child = mother.fields['have_job']
#                     if mother.is_valid():
#                         first_name = mother.cleaned_data['first_name']
#                         last_name = mother.cleaned_data['last_name']
#                         phone_number = mother.cleaned_data['phone_number']
#                         have_job = mother.cleaned_data['have_job']
#                         address_like_child = mother.cleaned_data['have_job']
#                         m = Parent.objects.create(first_name=first_name,
#                                                   last_name=last_name,
#                                                   have_job=have_job)
#                     father = Parent(request.POST)
#                     first_name = father.fields['first_name']
#                     last_name = father.fields['last_name']
#                     phone_number = father.fields['phone_number']
#                     have_job = father.fields['have_job']
#                     address_like_child = father.fields['have_job']
#                     if father.is_valid():
#                         first_name = father.cleaned_data['first_name']
#                         last_name = father.cleaned_data['last_name']
#                         phone_number = father.cleaned_data['phone_number']
#                         have_job = father.cleaned_data['have_job']
#                         address_like_child = father.cleaned_data['have_job']
#                         f = Parent.objects.create(first_name=first_name,
#                                                   last_name=last_name,
#                                                   have_job=have_job)
#
#                     # Zapisanie rekruta
#                     print(b)
#                     r = Recruit.objects.create(PESEL=pesel,
#                                                first_name=first_name,
#                                                last_name=last_name,
#                                                birthdate=birthdate,
#                                                birthplace=birthplace,
#                                                application_status=1,
#                                                school_class=school_class,
#                                                catchment_area=catchment_area,
#                                                father=f,
#                                                mother=m,
#                                                further_information=further_information,
#                                                permanent_address=a,
#                                                residential_address=b,
#                                                )
#                     return render(request, 'address-form.html', {'r': r})
#
#         return render(request, 'recruitment-form.html', {'r': 'dupa'})


def documents(request):
    return render(request, 'documents.html', {})


from django.http import FileResponse, Http404


def pdf_view(request, klasa):
    try:
        return FileResponse(open(f'/home/katarzyna/Pulpit/kurs/Projekt_zaliczeniowy/pliki/{klasa}.pdf', 'rb'),
                            content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()


from django.views.generic import TemplateView

from .forms import RecruitmentForm, AddressForm


class RecruitmentView(TemplateView):
    permanent_address_form_class = AddressForm
    residential_address_form_class = AddressForm
    recruitment_form_class = RecruitmentForm
    mother_form_class = ParentForm2
    mother_permanent_address_form_class = AddressForm
    father_form_class = ParentForm2
    father_permanent_address_form_class = AddressForm
    approval_form_class = ApprovalForm
    no_catchment_area_information_form_class = NoCatchmentAreaInformationForm
    template_name = 'recruitment-form.html'

    def post(self, request, school_class):
        post_data = request.POST or None
        permanent_address_form = self.permanent_address_form_class(post_data, prefix='address')
        residential_address_form = self.residential_address_form_class(post_data, prefix='address')
        recruitment_form = self.recruitment_form_class(post_data, prefix='recruiment')
        mother_form = self.mother_form_class(post_data, prefix='mother')
        mother_permanent_address_form = self.mother_permanent_address_form_class(post_data, prefix='mother address')
        father_form = self.father_form_class(post_data, prefix='father')
        father_permanent_address_form = self.father_permanent_address_form_class(post_data, prefix='father address')
        approval_form = self.approval_form_class(post_data, prefix='approval')
        no_catchment_area_information_form = self.no_catchment_area_information_form_class(post_data, prefix='approval')
        context = self.get_context_data(permanent_address_form=permanent_address_form,
                                        residential_address_form=residential_address_form,
                                        form=recruitment_form,
                                        mother_form=mother_form,
                                        mother_permanent_address_form=mother_permanent_address_form,
                                        father_form=father_form,
                                        father_permanent_address_form=father_permanent_address_form,
                                        approval_form=approval_form,
                                        no_catchment_area_information_form =no_catchment_area_information_form
                                        )

        if permanent_address_form.is_valid():
            a = permanent_address_form.save()

        # if mother_form.is_valid():
        #     m = mother_form.save(commit=False)
        #     address_like_child = request.POST.get('address_like_child')
        #     if address_like_child == 'True':
        #         if mother_permanent_address_form.is_valid():
        #             mother_address = mother_permanent_address_form.save()
        #     else:
        #         print(a)
        #         mother_address = a
        #     m.address = mother_address
        #     m.save()
        #     print(m)
        #
        # if father_form.is_valid():
        #     f = father_form.save(commit=False)
        #     if address_like_child == 'True':
        #         if father_permanent_address_form.is_valid():
        #             father_address = father_permanent_address_form.save()
        #     else:
        #         father_address = a
        #     f.address = father_address
        #     f.save()
        #
        # if approval_form.is_valid():
        #     ap = approval_form.save()
        #     print(ap)
        #
        # if recruitment_form.is_valid():
        #     r = recruitment_form.save(commit=False)
        #     r.permanent_address = a
        #     residential_like_permanent = request.POST.get('residential_like_permanent')
        #     print(residential_like_permanent)
        #     if residential_like_permanent == 'True':
        #         if residential_address_form.is_valid():
        #             b = residential_address_form.save()
        #             r.residential_address = b
        #     else:
        #         r.residential_address = a
        #         print(r.residential_address)
        #     r.school_class = school_class
        #     r.mother = m
        #     r.father = f
        #     r.application_status = STATUS[0][0]
        #     r.approval = ap
        #     r.save()
        #     if r.catchment_area == 'True':
        #         if no_catchment_area_information_form.is_valid():
        #             i = no_catchment_area_information_form.save(commit=False)
        #             i.recruit = r
        #             i.save()
        # else:
        #     print("Błąd")
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


def my_data(request):
    login = request.user
    user = User.objects.get(username=login)
    return render(request, 'my-data.html', {'user': user})


class ResetPasswordView(View):
    def get(self, request):
        user = User.objects.get(username=request.user)
        form = ResetPasswordForm()
        return render(request, 'reset-password.html', {'form': form})

    def post(self, request):
        form = ResetPasswordForm(request.POST)
        password = form.fields['password']
        password2 = form.fields['password2']
        if form.is_valid():
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            if password == password2:
                user = User.objects.get(username=request.user)
                user.set_password(password)
                user.save()
                return render(request, 'my-data.html', {'user': user, 'mess': 'Hasło zostało zmienione.'})
            else:
                return HttpResponse('Hasła nie są takie same.')

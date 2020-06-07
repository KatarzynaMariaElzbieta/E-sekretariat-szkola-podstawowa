from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView
from django.contrib.auth import authenticate, login, logout, password_validation
from django.http import FileResponse, Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.models import User

from .forms import SignUpForm, LoginForm, ParentForm2, ApprovalForm, ResetPasswordForm, NoCatchmentAreaInformationForm, \
    ApplicationForm, RecruitmentForm, AddressForm
from .models import STATUS, Application, CLASSES, Recruit


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
            def clean_password(self):
                password = self.cleaned_data.get('password')
                errors = dict()
                try:
                    password_validation.validate_password(password)

                except form.ValidationError as e:
                    errors['password'] = list(e.messages)
                if errors:
                    raise form.ValidationError("haslo za krótkie")

            password = form.cleaned_data['password']

            uname = first_name[0] + "." + last_name
            is_new_login = User.objects.filter(username__icontains=login).count()
            if is_new_login != 0:
                uname += str(is_new_login)
            user = User.objects.create_user(uname, password=password, first_name=first_name, last_name=last_name)
            if user is not None:
                if user.is_authenticated:
                    login(self.request, user)
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
            form = LoginForm()
            ctx['notlog'] = "Błąd logowania. Spróbuj jeszcze raz."
            ctx['form'] = form
        return render(request, 'sign-in.html', ctx)


def logoutView(request):
    logout(request)
    return redirect(reverse('signin'))

@login_required
def recruitment1(request):
    return render(request, 'recruitment1.html', {})


def documents(request):
    return render(request, 'documents.html', {})


def pdf_view(request, klasa):
    try:
        return FileResponse(open(f'/home/katarzyna/Pulpit/kurs/Projekt_zaliczeniowy/pliki/{klasa}.pdf', 'rb'),
                            content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

class RecruitmentView(LoginRequiredMixin, TemplateView):
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
        sclass = request.POST.get("sclass")
        permanent_address_form = self.permanent_address_form_class(post_data, prefix='address')
        residential_address_form = self.residential_address_form_class(post_data, prefix='address')
        recruitment_form = self.recruitment_form_class(post_data, prefix='recruiment')
        mother_form = self.mother_form_class(post_data, prefix='mother')
        mother_permanent_address_form = self.mother_permanent_address_form_class(post_data, prefix='mother_address')
        father_form = self.father_form_class(post_data, prefix='father')
        father_permanent_address_form = self.father_permanent_address_form_class(post_data, prefix='father_address')
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
                                        no_catchment_area_information_form =no_catchment_area_information_form,
                                        school_class=school_class,
                                        classes = CLASSES
                                        )

        if permanent_address_form.is_valid():
            a = permanent_address_form.save()

        if mother_form.is_valid():
            m = mother_form.save(commit=False)
            address_like_child = request.POST.get('address_like_child')
            if address_like_child == 'True':
                if mother_permanent_address_form.is_valid():
                    mother_address = mother_permanent_address_form.save()
            else:
                print(a)
                mother_address = a
            m.address = mother_address
            m.save()
            print(m)

        if father_form.is_valid():
            f = father_form.save(commit=False)
            if address_like_child == 'True':
                if father_permanent_address_form.is_valid():
                    father_address = father_permanent_address_form.save()
            else:
                father_address = a
            f.address = father_address
            f.save()

        if approval_form.is_valid():
            ap = approval_form.save()
            print('zgody')
            print(ap)

        if recruitment_form.is_valid():
            r = recruitment_form.save(commit=False)
            r.permanent_address = a
            residential_like_permanent = request.POST.get('residential_like_permanent')
            print(residential_like_permanent)
            if residential_like_permanent == 'True':
                if residential_address_form.is_valid():
                    b = residential_address_form.save()
                    r.residential_address = b
            else:
                r.residential_address = a
                print(r.residential_address)
            if school_class == 3:
                r.school_class = sclass
            else:
                r.school_class = school_class
            r.mother = m
            r.father = f
            r.application_status = STATUS[0][0]
            r.approval = ap
            user = User.objects.get(username=request.user)
            r.user=user
            r.save()
            print(r)
            if r.no_catchment_area == 'True':
                if no_catchment_area_information_form.is_valid():
                    i = no_catchment_area_information_form.save(commit=False)
                    i.recruit = r
                    i.save()
            Application.objects.create(recruit=r, application_content=' ', type=1)
            return redirect('app-list')
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

@login_required
def my_data(request):
    login = request.user
    user = User.objects.get(username=login)
    children = Recruit.objects.filter(user=user)
    return render(request, 'my-data.html', {'user': user, 'children': children})


class ResetPasswordView(LoginRequiredMixin, View):
    def get(self, request):
        user = User.objects.get(username=request.user)
        form = ResetPasswordForm()
        return render(request, 'reset-password.html', {'form': form})

    def post(self, request):
        reset_form = ResetPasswordForm(request.POST)
        password = reset_form.fields['password']
        password2 = reset_form.fields['password2']
        if reset_form.is_valid():
            password = reset_form.cleaned_data['password']
            password2 = reset_form.cleaned_data['password2']
            if password == password:
                user = User.objects.get(username=request.user)
                user.set_password(password)
                user.save()
                login(self.request, user)
                return render(request, 'my-data.html', {'user': user, 'mess': 'Hasło zostało zmienione.'})
            else:
                return HttpResponse('Hasła nie są takie same.')
        else:
            return HttpResponse('')

@login_required
def application_list(request):
    user = User.objects.get(username=request.user)
    application_li = []
    if user.has_perm('change_application'):
        application_li = Application.objects.all()
    else:
        children = Recruit.objects.filter(user=user)
        if not children:
            application_li="Brak podań"
        for i in children:
            app = (Application.objects.filter(recruit=i))
            for i in app:
                application_li.append(i)


    return render(request, 'application_list.html', {'application_list': application_li})

@login_required
def application_detail(request, id):
    app = Application.objects.get(pk=id)
    user = User.objects.get(username=request.user)
    ctx = {
        'app': app,
    }
    if user.has_perm('change_application'):
        ctx['status'] = STATUS

    return render(request, 'application_detail.html', ctx)


class ApplicationFormView(LoginRequiredMixin, View):
    def get(self, request):
        form = ApplicationForm()
        login = request.user
        user = User.objects.get(username=login)
        children = Recruit.objects.filter(user=user).filter(application_status=2)
        if not children:
            ctx = {'user': user}
            return render(request, 'recruitment.html', ctx)
        return render(request, 'application-form.html', {'form': form, 'children': children})

    def post(self, request):
        form = ApplicationForm(request.POST, request.FILES)
        recruit = request.POST.get("recruit")
        if form.is_valid():
            a = form.save(commit=False)
            a.recruit = Recruit.objects.get(id=recruit)
            a.save()
            return redirect('app-list')
        return HttpResponse('Bład')


@permission_required('change_application')
def change_status(request, id, status):
    app = Application.objects.get(pk=id)
    app.application_status = status
    app.save()
    if app.type == 1 and app.application_status == 2:
        app.recruit.application_status = 2
        app.recruit.save()
    return redirect('app-list')


class RecruitDetailView(LoginRequiredMixin, DetailView):

    model = Recruit
    queryset = Recruit.objects.all()
    template_name = 'recruit-detail.html'
    c = []
    for i in Recruit._meta.fields:
        c.append(i)
    extra_context = {'list': c}
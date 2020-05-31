from django.db import models

# Create your models here.
WOJEWODZTWA = (
    (1, 'Wielkopolskie'),
    (2, 'Kujawsko-pomorskie'),
    (3, 'Małopolskie'),
    (4, 'Łódzkie'),
    (5, 'Dolnośląskie'),
    (6, 'Lubelskie'),
    (7, 'Lubuskie'),
    (8, 'Mazowieckie'),
    (9, 'Opolskie'),
    (10, 'Podlaskie'),
    (11, 'Pomorskie'),
    (12, 'Śląskie'),
    (13, 'Podkarpackie'),
    (14, 'Świętokrzyskie'),
    (15, 'Warmińsko-Mazurskie'),
    (16, 'Zachodniopomorskie')
)

STATUS = (
    (1, 'oczekuje'),
    (2, 'rozpatrzony pozytywnie'),
    (3, 'odrzucony'),
)

CLASSES = (
    (0, 'Oddział 0'),
    (1, 'Klasa I'),
    (2, 'Klasa II'),
    (3, 'Klasa III'),
    (4, 'Klasa IV'),
    (5, 'Klasa V'),
    (6, 'Klasa VI'),
    (7, 'Klasa VII'),
    (8, 'Klasa VIII')
)


class Address(models.Model):
    province = models.IntegerField(verbose_name='województwo', choices=WOJEWODZTWA)
    county = models.CharField(verbose_name='powiat', max_length=64)
    borough = models.CharField(verbose_name='gmina', max_length=64)
    locality = models.CharField(verbose_name='miejscowość', max_length=64)
    postcode = models.CharField(verbose_name='kod pocztowy', max_length=64)
    street = models.CharField(verbose_name='ulica', max_length=64)
    house_number = models.CharField(verbose_name='numer domu', max_length=4)
    flat_number = models.CharField(verbose_name='numer mieszkania', max_length=4, null=True)
    phone_number = models.IntegerField(verbose_name='numer telefonu', null=True)


class Parent(models.Model):
    first_name = models.CharField(verbose_name='Imię', max_length=64)
    last_name = models.CharField(verbose_name='Nazwisko',max_length=64)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    tel = models.IntegerField(verbose_name='Telefon',)
    have_job = models.BooleanField(verbose_name='Praca',)


class Approval(models.Model):
    statutes = models.BooleanField(verbose_name="Przestrzegania postanowień statutu szkoły")
    data_updating = models.BooleanField(verbose_name="Podawania do wiadomości szkoły wszelkich zmian w podanych wyżej informacjach")
    nonconference = models.BooleanField(verbose_name="Uczestniczenia w zebraniach rodziców")
    religion = models.BooleanField()
    photo_publication = models.BooleanField(verbose_name="Wyrażam zgodę na publikację zdjęć dziecka z imprez i uroczystości szkolnych na stronie internetowej promującej placówkę oraz w ramach przekazywania informacji o pracy dydaktyczno – wychowawczej szkoły.")
    processing_of_personal_data = models.BooleanField(verbose_name="Oświadczam pod rygorem odpowiedzialności karnej, że podane informacje są zgodne z aktualnym stanem faktycznym.")
    provision = models.BooleanField(verbose_name='Wyrażam zgodę na przetwarzanie danych osobowych zawartych w niniejszym dokumencie')


class Recruit(models.Model):
    first_name = models.CharField(verbose_name='Imię', max_length=64)
    last_name = models.CharField(verbose_name='Nazwisko', max_length=64)
    PESEL = models.IntegerField(verbose_name='PESEL', unique=True)
    birthdate = models.DateField(verbose_name='Data urodzenia' )
    birthplace = models.CharField(verbose_name='Miejsce urodzenia', max_length=64)
    permanent_address = models.ForeignKey(Address, verbose_name='Adres zamieszkania', related_name='permanent', on_delete=models.CASCADE)
    residential_address = models.ForeignKey(Address, verbose_name='Adres zameldowania', related_name='residental', on_delete=models.CASCADE)
    further_information = models.TextField(verbose_name='Dodatkowe informacje', null=True)
    catchment_area = models.BooleanField(verbose_name='Przynależność do obwodu szkoły')
    application_status = models.IntegerField(verbose_name='Status aplikacji', choices=STATUS)
    mother = models.ForeignKey(Parent, related_name='mother', on_delete=models.CASCADE)
    father = models.ForeignKey(Parent, related_name='father', on_delete=models.CASCADE)
    school_class = models.IntegerField(choices=CLASSES, default=0, verbose_name='Klasa')
    approval = models.ForeignKey(Approval, on_delete=models.CASCADE, null=True)


FAMILY = (
    (1, 'Pełna'),
    (2, 'niepełna'),
    (3, 'rozbita'),
    (4, 'inna sytuacja')
)


class NoCatchmentAreaInformation(models.Model):
    recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE)
    full_family = models.IntegerField(choices=FAMILY, verbose_name='Rodzina')
    disabled = models.BooleanField(verbose_name='Niepełnosprawność w rodzinie')
    have_siblings = models.BooleanField(verbose_name='Czy dziecko posiada rodzeństwo?', default='False')
    siblings_info = models.TextField(verbose_name='Rodzeństwo (imię, nazwisko, rok urodzenia)', null=True)
    preschool = models.BooleanField(verbose_name='Czy dziecko uczęszczało do przedszkola')
    preschool_years = models.IntegerField(verbose_name='Ile lat dziecko uczęszczało do przedszkola?', null=True)

APPLICATION_TYPE = (
    (1, 'rekrutacja'),
    (2, 'legitymacja'),
    (3, 'karta rowerowa'),
    (4, 'świetlica'),
)


class Application(models.Model):
    sent_date = models.DateField(auto_now=True)
    recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE)
    application_content = models.TextField()
    attachment = models.FileField()
    type = models.IntegerField(choices=APPLICATION_TYPE)
from django.db import models
import sys
sys.path.append("..")
from company_app.models import Companies
from django.contrib import admin


class ContactCompany(models.Model):
    CONTACT_TYPE_EMAIL = 1
    CONTACT_TYPE_PHONE = 2
    CONTACT_TYPE_FACEBOOK = 3
    CONTACT_TYPE_ADDRESS = 4
    CONTACT_TYPE_FAX = 5

    CONTACT_TYPES = (
        (CONTACT_TYPE_EMAIL, 'Email'),
        (CONTACT_TYPE_PHONE, 'Telefon'),
        (CONTACT_TYPE_ADDRESS, 'Adres'),
        (CONTACT_TYPE_FAX, 'Faks')
    )

    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    contact_type = models.IntegerField(
                                    choices=CONTACT_TYPES,
                                    default=CONTACT_TYPE_EMAIL
                                    )
    contact = models.CharField(max_length=255)

    def __str__(self):
        return f"{list(filter(lambda x: x[0] == self.contact_type, self.CONTACT_TYPES))[0][1]}: {self.contact}"

    class Meta:
        verbose_name = 'Şirkətin əlaqə məlumatı'
        verbose_name_plural = 'Əlaqə məlumatları'


class ContactCompanyForm(models.Model):
    company = models.OneToOneField(Companies, on_delete=models.CASCADE, primary_key=True)
    to_email = models.EmailField("Kimə")
    name_placeholder = models.CharField("Ad üçün qeyd", max_length=255, default="Adınızı daxil edin")
    email_placeholder = models.CharField("Email üçün qeyd", max_length=255, default="Email adresinizi daxil edin")
    subject_placeholder = models.CharField("Mövzu üçün qeyd", max_length=255, default="Məktubun mövzusunu daxil edin")
    content_placeholder = models.CharField("Mətn üçün qeyd", max_length=1000, default="Məktubun mətnini daxil edin")

    def __str__(self):
        return self.subject_placeholder
    
    class Meta:
        verbose_name = "Əlaqə formasının ayarları"
        verbose_name_plural = "Əlaqə formasının ayarları"


class ContactCompanyReceivedEmails(models.Model):
    company_contact_form = models.ForeignKey(ContactCompanyForm, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    body = models.CharField(max_length=1000)
    from_email = models.EmailField()
    #TODO: wait for reply from Elshad here -> https://bitbucket.org/techwebstudio/back-end/issues/1/
    sent = models.BooleanField(default=False)
    sent_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"from: {self.from_email} | subject: {self.subject}"

    class Meta:
        verbose_name = "Gələn məktub"
        verbose_name_plural = "Gələn məktublar"


class ContactMainForm(models.Model):
    to_email = models.EmailField()
    subject_placeholder = models.CharField(max_length=255)
    content_placeholder = models.CharField(max_length=1000)

    def __str__(self):
        return "{} {}".format(self.to_email,
                              self.subject_placeholder)


class ContactMainReceivedEmails(models.Model):
    subject = models.CharField(max_length=255)
    body = models.CharField(max_length=1000)
    from_email = models.EmailField()
    # TODO: wait for reply from Elshad here -> https://bitbucket.org/techwebstudio/back-end/issues/1/
    sent = models.EmailField()
    sent_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {} {}".format(self.from_email,
                                 self.subject,
                                 self.sent_at)

#### Admin ####
class ContactCompanyAdmin(admin.ModelAdmin):
    exclude = "company",

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.company = Companies.objects.get(profile=request.user)

        super(ContactCompanyAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(ContactCompanyAdmin, self).get_queryset(request)

        if request.user.is_superuser:
            return qs

        return qs.filter(company=Companies.objects.get(profile=request.user))


class ContactCompanyFormAdmin(admin.ModelAdmin):
    exclude = "company",

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.company = Companies.objects.get(profile=request.user)

        super(ContactCompanyFormAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(ContactCompanyFormAdmin, self).get_queryset(request)

        if request.user.is_superuser:
            return qs

        return qs.filter(company=Companies.objects.get(profile=request.user))
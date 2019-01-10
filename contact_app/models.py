from django.db import models
import sys
sys.path.append("..")
from company_app.models import Companies
# Create your models here.


class ContactCompany(models.Model):
    EMAIL = 'EM'
    PHONE = 'PH'
    FACEBOOK = 'FB'
    ADDRESS = 'ADD'
    CONTACT_TYPES = (
        (EMAIL, 'Email'),
        (PHONE, 'Phone'),
        (FACEBOOK, 'Facebook'),
        (ADDRESS, 'Address')
    )

    company_id = models.ForeignKey(Companies, on_delete=models.CASCADE)
    company_type = models.CharField(max_length=25,
                                    choices=CONTACT_TYPES,
                                    default=EMAIL
                                    )
    contact = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.contact)

    class Meta:
        verbose_name = 'Company Contact'
        verbose_name_plural = 'Company Contacts'


class ContactCompanyForm(models.Model):
    company_id = models.ForeignKey(Companies, on_delete=models.CASCADE)
    to_email = models.EmailField()
    subject_placeholder = models.CharField(max_length=255)
    content_placeholder = models.CharField(max_length=1000)

    def __str__(self):
        return "{} {}".format(self.subject_placeholder,
                              self.content_placeholder)


class ContactCompanyReceivedEmails(models.Model):
    company_contact_form_id = models.ForeignKey(ContactCompanyForm, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    body = models.CharField(max_length=1000)
    from_email = models.EmailField()
    #TODO: wait for reply from Elshad here -> https://bitbucket.org/techwebstudio/back-end/issues/1/
    sent = models.EmailField()
    sent_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {} {}".format(self.from_email,
                                 self.subject,
                                 self.sent_at)


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

# class ContactMain(models.Model):
#     subject_as_name = models.CharField(max_length=255)
#     from_email = models.EmailField()
#     message = models.CharField(max_length=1000)
#
#     def __str__(self):
#         return "{} {}".format(self.subject_as_name,
#                               self.from_email)


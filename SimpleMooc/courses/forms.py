from django import forms
from django.conf import settings

from SimpleMooc.core.mail import send_mail_template


class ContactCourse(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Menssagem/Dúvida', widget=forms.Textarea)

    def send_mail(self, course):
        subject = '[%s] Contato' % course
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message']
        }
        template_name = 'courses/contact_email.html'
        send_mail_template(subject, template_name, context, [settings.CONTACT_EMAIL])
        # message = message % context
        # send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])

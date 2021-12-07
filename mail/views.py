from django.shortcuts import render
from send_mail.settings import EMAIL_HOST_USER
from .forms import EmailAttachmentForm
from django.core.mail import EmailMessage


# Create your views here.
def email_save_send(request):
    if request.method == 'POST':
        context = {}
        forms = EmailAttachmentForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            message = 'Email with Image'
            subject = 'Testing'

            try:
                mail_id = request.POST.get('email')
                email = EmailMessage(subject, message, EMAIL_HOST_USER, [mail_id])
                email.content_subtype = 'html'
                file = request.FILES.get('image')
                email.attach(file.name, file.read(), file.content_type)
                email.send()
                context['message'] = "email saved and sent successfully"
            except:
                context['errors'] = "Either the attachment is too big or corrupt"

        else:
            context['errors'] = forms.errors

        return render(request, 'mail/home.html', context)

    return render(request, 'mail/home.html')

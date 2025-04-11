from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.urls import reverse
from .utils import render_to_pdf 
from .forms import LeaderStandardWorkForm

def leader_standard_work_view(request):
    if request.method == 'POST':
        form = LeaderStandardWorkForm(request.POST)
        if form.is_valid():
            # Create the PDF content from an HTML template.
            pdf_data = render_to_pdf('ipqa_lsw/pdf_template.html', {'data': form.cleaned_data})
            
            if not pdf_data:
                # Optionally handle PDF generation errors.
                return render(request, 'ipqa_lsw/error.html', {'message': 'Error generating PDF.'})
            
            subject = "IPQA Leader Standard Work Submission"
            from_email = settings.DEFAULT_FROM_EMAIL  # Ensure you have this set in settings.py
            recipient_list = ['apdlug.IPQA@abacuspharma.com']  # My actual email
            
            # Create an EmailMessage object.
            email = EmailMessage(subject, "Please see the attached submission PDF.", from_email, recipient_list)
            email.attach('submission.pdf', pdf_data, 'application/pdf')
            email.send()
            
            return render(request, 'ipqa_lsw/thank_you.html', {'data': form.cleaned_data})
    else:
        form = LeaderStandardWorkForm()
    return render(request, 'ipqa_lsw/leader_standard_work_form.html', {'form': form})


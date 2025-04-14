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
            try:
                # Determine which sections were selected
                data = form.cleaned_data
                active_sections = []
                
                # Check which sections were supervised
                supervised_sections = data.get('sections_supervised', [])
                
                # Check which sections have data (for periodic section which is always visible)
                if any(data.get(f'periodic_{field}') for field in ['trainings', 'investigations', 'equipment_tags']):
                    active_sections.append('periodic')
                
                # Add the supervised sections
                active_sections.extend(supervised_sections)
                
                # Add to context
                context = {
                    'data': data,
                    'active_sections': active_sections
                }

                pdf_data = render_to_pdf('ipqa_lsw/pdf_template.html', context)
                
                email = EmailMessage(
                    "IPQA Leader Standard Work Submission",
                    "Please see the attached submission PDF.",
                    settings.DEFAULT_FROM_EMAIL,
                    ['apdlug.ipqa@gmail.com']
                )
                email.attach('submission.pdf', pdf_data, 'application/pdf')
                email.send()
                
                return render(request, 'ipqa_lsw/thank_you.html', {'data': form.cleaned_data})
            
            except Exception as e:
                print("Error:", str(e))
                return render(request, 'ipqa_lsw/error.html', {'message': str(e)})
    else:
        form = LeaderStandardWorkForm()
    
    return render(request, 'ipqa_lsw/leader_standard_work_form.html', {'form': form})



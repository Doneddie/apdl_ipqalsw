import io
from django.template.loader import render_to_string
from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
    """Renders HTML template with provided context to PDF."""
    html = render_to_string(template_src, context_dict)
    result = io.BytesIO()
    pdf = pisa.CreatePDF(io.BytesIO(html.encode('utf-8')), dest=result)
    if pdf.err:
        return None
    return result.getvalue()

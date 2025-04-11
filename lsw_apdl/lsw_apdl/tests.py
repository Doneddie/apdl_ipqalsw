def generate_pdf_and_send_email():
    # Generate PDF data (this would be based on your logic)
    pdf_data = generate_pdf_somehow()
    
    # Send the email with the PDF attached
    send_email_with_attachment(pdf_data)

    print(env('EMAIL_HOST'))  # Should print 'smtp.gmail.com' if the .env file is read correctly.

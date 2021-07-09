import pdfkit


def pdf_creator(url, output):
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    pdfkit.from_url(url, output + '.pdf', configuration=config)



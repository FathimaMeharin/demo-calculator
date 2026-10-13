import pdfkit

config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')

pdfkit.from_file('sample.html', 'pdf_from_file.pdf', configuration=config)
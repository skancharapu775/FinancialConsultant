def generate_pdf(text):
    '''
    sudo apt-get update
    sudo apt-get install xvfb libfontconfig wkhtmltopdf
    pip install pdfkit
    brew install wkhtmltopdf
    '''
    str_title = "Financial Plan"
    title = str_title.title()
    
    new_line = "<br>"
    html_string = """<h1 style="text-align:center"><b>""" + title + "</b></h1>"
    html_string += new_line * 2

    for i in range(len(answers)):
        line = """<h3 style="text-align:center">""" + str(i+1) + ": " + problems[i]["answer"] + "</h3>"
        html_string += line

    pdfname = "Practice_Worksheet.pdf"
    pdfkit.from_string(html_string, output_path = pdfname)

    return pdfname
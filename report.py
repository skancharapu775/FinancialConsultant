import pdfkit


#for windows only, remove when on mac
# Set the path to wkhtmltopdf executable file
path_wkhtmltopdf = 'C:\Program Files\wkhtmltopdin/wkhtmltopdf.exe'  # This may vary depending on your system
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
 
# Use the configuration when generating PDF
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
    html_string += new_line * 3
    
    lines = text.split("\n")

    for i in range(len(lines)):
        html_string = """<h3 style="text-align:left"><b>""" + lines[i] + "</b></h3>"
        html_string += new_line

    pdfname = "Financial_Plan.pdf"

    #remove configuration argument when not on windows
    pdfkit.from_string(html_string, output_path = pdfname, configuration=config)

    return pdfname
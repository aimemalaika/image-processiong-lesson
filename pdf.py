import PyPDF2

with open('pdfs/11.3 dummy.pdf','rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf','wb') as new_file:
        writer.write(new_file)
        print()
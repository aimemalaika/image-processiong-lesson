import PyPDF2
# import sys

# with open('pdfs/11.3 dummy.pdf','rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     page = reader.getPage(0)
#     page.rotateCounterClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('tilt.pdf','wb') as new_file:
#         writer.write(new_file)
#         print()

# Inputs = sys.argv[1:]

# def pdf_combiner(pdflists):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdflists:
#         merger.append(pdf)
#     merger.write('super.pdf')

# pdf_combiner(Inputs)

tempale = PyPDF2.PdfFileReader(open('super.pdf','rb'))
watermark = PyPDF2.PdfFileReader(open('pdfs/wtr.pdf','rb'))

output = PyPDF2.PdfFileWriter()

for i in range(tempale.getNumPages()):
    page = tempale.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermark_file.pdf','wb') as marked:
        output.write(marked)
    
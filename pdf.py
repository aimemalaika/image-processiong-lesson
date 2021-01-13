import PyPDF2
import sys

# with open('pdfs/11.3 dummy.pdf','rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     page = reader.getPage(0)
#     page.rotateCounterClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('tilt.pdf','wb') as new_file:
#         writer.write(new_file)
#         print()

Inputs = sys.argv[1:]

def pdf_combiner(pdflists):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdflists:
        merger.append(pdf)
    merger.write('super.pdf')

pdf_combiner(Inputs)
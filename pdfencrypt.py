from PyPDF2 import PdfFileReader,PdfFileWriter

with open("test.pdf", "rb") as in_file:
    input_pdf = PdfFileReader(in_file)

    output_pdf = PdfFileWriter()
    output_pdf.appendPagesFromReader(input_pdf)
    output_pdf.encrypt("password")

    with open("output3.pdf", "wb") as out_file:
        output_pdf.write(out_file)
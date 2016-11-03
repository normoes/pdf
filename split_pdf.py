# -*- coding: utf-8 -*-
#from pyPdf import PdfFileWriter, PdfFileReader
from PyPDF2 import PdfFileWriter as pdfWriter
from PyPDF2 import PdfFileReader as pdfReader

#inputpdf = pdfReader(open("/home/norman/SpiderOak Hive/01_programming/11_python/pdf/test/2016-10-01_Mitgliedsbescheinigung.pdf", "rb"))
inputpdf = pdfReader(open("24056200000027.pdf", "rb"))
"""
Postbank PDFs are encrypted with an empty password
"""
if inputpdf.isEncrypted:
   print 'encrypted'
   inputpdf.decrypt("") # empty password
output = pdfWriter()
outputStream = open("Mitgliedsbescheinigung_aucobo.pdf", "wb")
totalPages = inputpdf.numPages - 1
print 'total:', totalPages
for page in range(inputpdf.numPages):
    if (page >= 2 and page <= 2): # and page <= 0:
        output.addPage(inputpdf.getPage(page))
        output.write(outputStream)
outputStream.close()

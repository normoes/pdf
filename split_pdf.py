# -*- coding: utf-8 -*-
#from pyPdf import PdfFileWriter, PdfFileReader
from PyPDF2 import PdfFileWriter as pdfWriter
from PyPDF2 import PdfFileReader as pdfReader

inputpdf = pdfReader(open("2016_10.pdf", "rb"))
"""
some PDFs are encrypted with an empty password
"""
if inputpdf.isEncrypted:
   print 'encrypted'
   inputpdf.decrypt("") # empty password


totalPages = inputpdf.getNumPages() - 1
print 'total:', totalPages + 1
for page in range(inputpdf.numPages):
    if (page >= 0 and page <= totalPages): # and page <= 0:
    	output = pdfWriter()
    	with open(str(page)+".pdf", "wb") as outStream:
        	output.addPage(inputpdf.getPage(page))
        	output.write(outStream)

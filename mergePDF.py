# -*- coding: utf-8 -*-
from PyPDF2 import PdfFileWriter as pdfWriter
from PyPDF2 import PdfFileReader as pdfReader
from os import path as osPath
from os import listdir as osListdir
from datetime import datetime as dDatetime



"""

 - takes all the pdf files in the current directory (where the program itself is located)
   - only pdf files not starting with '__' (double underscore) --> defines output file
   - file extension must be '.pdf' or '.PDF', ...
 - pdf files are sorted by using str.lower on the file names
   - first files in order become first pages in output pdf file

"""

def addPdf_pageByPage(pdfOut, pdfIn, debug = False):
    """
    Postbank PDFs are encrypted with an empty password
    """
    if pdfIn.isEncrypted:
        print 'encrypted, trying empty password'
        pdfIn.decrypt("") # empty password
    print 'pages:'
    for page in range(pdfIn.numPages):
        if debug:
            print page + 1,
        pdfOut.addPage(pdfIn.getPage(page))

def addPdf_wholePdf(pdfOut, pdfIn, debug = False):
    """
    Postbank PDFs are encrypted with an empty password
    """
    if pdfIn.isEncrypted:
        print 'encrypted, trying empty password'
        pdfIn.decrypt("") # empty password
    pdfOut.appendPagesFromReader(pdfIn)

def main(path, add_func, debug = False):
    if osPath.exists(path):
        output1 = pdfWriter()
        files = osListdir(path)
        files.sort(key=str.lower)
        for pdf in files:
            if pdf.lower().endswith('.pdf') and not pdf.startswith('__'):
                if debug:
                    print
                    print pdf
                inputpdf = pdfReader(osPath.join(path,pdf), "rb")
                add_func(output1, inputpdf, debug)
                """
                Postbank PDFs are encrypted with an empty password
                """
                #if inputpdf.isEncrypted:
                #    print 'encrypted, trying empty password'
                #    inputpdf.decrypt("") # empty password
                #print 'pages:'
                #for page in range(inputpdf.numPages):
                #    if debug:
                #        print page + 1,
                #    output1.addPage(inputpdf.getPage(page))
        newFile= dDatetime.utcnow().strftime('__%Y_%m_%d_%H_%M_%S')+"_new.pdf"
        if debug:
            print
            print 'creating', newFile
        outputStream =  open(osPath.join(path,newFile), "wb")
        if debug:
            print 'writing'
        output1.write(outputStream)
        if debug:
            print 'closing'
        outputStream.close()

def test_main(add_func):
    print osPath.dirname(osPath.abspath(__file__))
    main(path=osPath.dirname(osPath.abspath(__file__)), add_func = add_func, debug=True)
    stop = raw_input('press Enter to exit.')

if __name__ == '__main__':
    #add_func = addPdf_pageByPage
    add_func = addPdf_wholePdf
    test_main(add_func=add_func)
    #main(path=osPath.dirname(osPath.abspath(__file__)), add_func=add_func)

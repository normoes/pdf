# pdf

When opening pdf files it is important to open them in binary mode 'rb'.

split_pdf.py
 - adapt name of input pdf
 - the output will be every single page as pdf file


mergePDF.py
 - takes all the pdf files fund in the directory where mergePDF.py is located
 - only top-level directory (os.listdir())
 - pdfs are sorted by key=str.lower and added to the output file in this order
 - the output will be a file in the following format: dDatetime.utcnow().strftime('__%Y_%m_%d_%H_%M_%S')+"_new.pdf"
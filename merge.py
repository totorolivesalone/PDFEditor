from PyPDF2 import PdfMerger
import os

inputPdfFolder="pdfInput" #input folder name /path
outputPdfFolder="pdfOutput" #output  folder name /path

pdfList=[os.path.join(inputPdfFolder,file) for file in os.listdir(inputPdfFolder) if file.endswith('.pdf')] #extracting files in an array
merger=PdfMerger() #initialising merger object

for pdf in pdfList:
    merger.append(pdf) #appending pdfs in temp memory

outputPath=os.path.join(outputPdfFolder ,"merged.pdf") #preparing output path with file name

merger.write(outputPath) # temp collection written in output path
merger.close() #releases temp memory
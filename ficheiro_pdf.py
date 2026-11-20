import aspose.words as aw

#Load TXT document
doc = aw.Document("texto.txt")

#save TXT as PDF file
doc.save("ficheiro.pdf", aw.SaveFormat.PDF)


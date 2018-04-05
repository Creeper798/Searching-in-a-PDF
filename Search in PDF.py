import PyPDF2
def main():
    tries = "yes"
    Q1 = input("Please enter the name of the PDF without the .pdf extension: ") #This asks for the pdf name at the top instead of in the while loop so that it doesnt keep asking for it.
    while "y" in tries.lower(): #This keeps the program running as long as someone wants to use it.
        word, x1 = input("\n\nPlease enter the word you are trying to find: "), 0
        test(word, x1, Q1)
        tries = input("Would you like to search for another word? ")
def test(word, x1, Q1):
    x, z = 0, 0
    derp = open(Q1 + ".pdf", "rb") #You can replace this PDF with any others and it will still work.
    pdfReader = PyPDF2.PdfFileReader(derp)
    pages = pdfReader.getNumPages()
    while x1 != pages: #While the number of pages searched is not equal to the number of pages in the PDF: keep searching.
        derp1 = pdfReader.getPage(x1)
        derp2 = derp1.extractText()
        derp2 = derp2.replace("\n", " ") #This takes out PDF formatting of random indents and replaces it with spaces.
        derp3 = derp2.replace(" ", "") #Taking out all spaces allows for a more accurate search because of PDF formatting.
        if word.lower() in derp3.lower():
            z = final(derp3, derp2, word, x, x1, z) #Z is returned from final and printed to show number of results.
        x1 += 1
        if not x1 > 0:
            z = final(derp3, derp2, word, x, x1, z)
    print(str(z) + " Results found.\n") #This is better than "word not found" because it displays the same information with less code.
def final(derp3, derp2, word, x, x1, z):
    nospace = derp3.lower().split(".")
    derp = derp2.lower().split(".")
    while x != len(nospace): #This fixes the 1 word per page problem, now it searches through the whole page and returns every instance of the word.
        if word.lower() in nospace[x]:
            z += 1 #This allows the variable Z to keep track of how many times a word is found successfully.
            print('"' + derp[x] + '."  (Found on page: ' + str(x1 + 1) + ")\n\n")
        x += 1
    return z
main()
def removepunc(text):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analysed = ""
    for char in text:
        if char not in punctuations:
            analysed = analysed + char

    return analysed

def toUpper(text):
    analysed = text.upper()
    return analysed

def newlineremove(text):
    analysed = ""
    for char in text:
        if char != "\n" and char != "\r":
            analysed = analysed + char

    return analysed

def extraspaceremove(text):
    analysed = ""
    for index, char in enumerate(text):
        if not (text[index] == " " and text[index + 1] == " "):
            analysed = analysed + char

    return analysed

def capitalisefirst(text):
    analysed = text.capitalize()
    return analysed
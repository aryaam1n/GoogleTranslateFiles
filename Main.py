import xml.etree.ElementTree as ET
import os
from google.cloud import translate_v2 as translate
import xmltodict
import pprint
import sys


def xmlToDict():
    # Open the file and read the contents
    with open('strings.xml', 'r', encoding='utf-8') as file:
        my_xml = file.read()

    # Use xmltodict to parse and convert
    # the XML document
    return xmltodict.parse(my_xml)


def validateLanguage(language):
    os.environ[
        'GOOGLE_APPLICATION_CREDENTIALS'] = "/Users/arya564/Desktop/Pycharm/FirstPythonProject/GoogleCloudKey_MyServiceAcct.json"

    translate_client = translate.Client()
    supportedLanguages = translate_client.get_languages()

    codeList = []

    for language_dict in supportedLanguages:
        codeList.append(language_dict['language'])

    if language in codeList:
        return True

    return False


# so this outputs into a dictionary with all of the values
# print(output)
def translateText(text, language):
    os.environ[
        'GOOGLE_APPLICATION_CREDENTIALS'] = "/Users/arya564/Desktop/Pycharm/FirstPythonProject/GoogleCloudKey_MyServiceAcct.json"

    translate_client = translate.Client()

    output = translate_client.translate(
        text,
        language
    )

    result = ''

    for key, value in output.items():
        if key == 'translatedText':
            result = value

    print(result)
    return result


def translateFile(language: str):
    if validateLanguage(language):
        file_base = "/strings.xml"
        language_file = language + file_base
        tree = ET.parse('strings.xml')
        root = tree.getroot()
        for child in root:
            if child.tag == "string":
                child.text = translateText(child.text, language)

        tree.write("output.xml", encoding='utf-8')


def main():
    arg1 = sys.argv[1]
    translateFile(arg1)
    # translateFile('es')


# Using the special variable
# __name__
if __name__ == "__main__":
    main()


'''
THINGS TO DO:
- need to ask for user input
- figure out how to do this from the command line
- figure out locale stuff (hebrew, viet, mandarin chinese)
- apk file with api key encryption???
'''



# # this creates a new element that has root as the tag name
# # PARENT ELEMENT
# root = ET.Element('root')
#
# # CHILD ELEMENTS
# person = ET.SubElement(root, 'person')
# name = ET.SubElement(person, 'name')
# age = ET.SubElement(person, 'age')
#
# # SETTING TEXT TO THE ELEMENTS
# name.text = 'John Doe'
# age.text = '30'
#
# tree = ET.ElementTree(root)
# tree.write('person.xml')

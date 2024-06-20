import xml.etree.ElementTree as ET
import os
from google.cloud import translate_v2 as translate
import xmltodict
import pprint


def xmlToDict():
    # Open the file and read the contents
    with open('strings.xml', 'r', encoding='utf-8') as file:
        my_xml = file.read()

    # Use xmltodict to parse and convert
    # the XML document
    return xmltodict.parse(my_xml)


def translateFile():
    tree = ET.parse('strings.xml')
    root = tree.getroot()
    for child in root:
        if child.tag == "string":
            child.text = translateText(child.text)
    tree.write("boom.xml", encoding='utf-8')


def translateText(text):
    os.environ[
        'GOOGLE_APPLICATION_CREDENTIALS'] = "/Users/arya564/Desktop/Pycharm/FirstPythonProject/GoogleCloudKey_MyServiceAcct.json"

    translate_client = translate.Client()

    target = 'es'
    output = translate_client.translate(
        text,
        target
    )

    # so this outputs into a dictionary with all of the values
    # print(output)

    result = ''

    for key, value in output.items():
        if key == 'translatedText':
            result = value

    print(result)
    return result


def main():
    translateFile()
    # translateText('Good Morning')


# Using the special variable
# __name__
if __name__ == "__main__":
    main()

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

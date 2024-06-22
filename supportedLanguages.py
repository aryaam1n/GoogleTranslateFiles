import os
from google.cloud import translate_v2 as translate
import pandas as pd

def getLanguages():
    os.environ[
        'GOOGLE_APPLICATION_CREDENTIALS'] = "/Users/arya564/Desktop/Pycharm/FirstPythonProject/GoogleCloudKey_MyServiceAcct.json"

    translate_client = translate.Client()
    languageList = translate_client.get_languages()
    supportedLanguages = pd.DataFrame(languageList)


    # languageList is a list of dictionaries


    myList = []

    for language_dict in languageList:
        language_code = language_dict['language']
        language_name = language_dict['name']

        myList.append(language_code)

    print(myList)


def main():
    getLanguages()


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
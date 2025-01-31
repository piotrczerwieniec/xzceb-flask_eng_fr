"""module """
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version= '2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com')

def english_to_french (english_text):
    """translate if string is not null"""
    if english_text is None:
        print("invalid input")
        french_text= english_text
    else:
        translation_response = language_translator.translate(\
            text= english_text, model_id='en-fr')
        translation = translation_response.get_result()
        french_text =translation['translations'][0]['translation']

    return french_text

def french_to_english (french_text):
    """translate if string is not null"""
    if french_text is None:
        print("invalid input")
        english_text= french_text
    else:
        translation_response = language_translator.translate(\
            text= french_text,model_id='fr-en')
        translation = translation_response.get_result()
        english_text =translation['translations'][0]['translation']

    return english_text

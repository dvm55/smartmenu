import json

from watson_developer_cloud import LanguageTranslatorV3
from watson_developer_cloud import WatsonApiException

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    iam_apikey='EaotF6vCJtTTWQWigO6a9oi2GVTVycPCNkQxFtqzKAbn',
    url='https://gateway-syd.watsonplatform.net/language-translator/api'
)

def idioma(texto):
    language = language_translator.identify(
        texto).get_result()
    language2 = (json.dumps(language, indent=2))
    counter = 1
    for language in language['languages']:
        if counter == 1:
            s =  language['language']
            counter = 0
    try:
        translation = language_translator.translate(
            text=texto,
            model_id= s +'-es').get_result()
    except WatsonApiException as ex:
        print("NO resuelto", texto)
        return texto
    #print(json.dumps(translation, indent=2, ensure_ascii=False))
    counter = 0
    result = ""
    for translations in translation["translations"]:
        result += json.dumps(translation["translations"][counter]['translation']) + " "
        counter = counter + 1
    print("traducido", result)
    return result



import requests
from testTask.settings import YANDEX_OAUTH2, YANDEX_FOLDER_ID


class YandexApi:
    data = f'{{"yandexPassportOauthToken":"{YANDEX_OAUTH2}"}}'
    token = requests.post('https://iam.api.cloud.yandex.net/iam/v1/tokens', data=data).json()['iamToken']
    folder_id = YANDEX_FOLDER_ID

    def translate(self, language, texts, schema=['title', 'description']):  # формируем переведенный словарь
        endpoint_url = 'https://translate.api.cloud.yandex.net/translate/v2/translate'
        list_texts = [str(texts[key]) for key in texts]
        body = {
            "targetLanguageCode": language,
            "texts": list_texts,
            "folderId": self.folder_id,
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {0}".format(self.token)
        }
        response = requests.post(endpoint_url, json=body, headers=headers)
        translated = [response.json()['translations'][iterator]['text'] for iterator in range(len(texts))]
        translated_dict = {}
        if len(translated) == 1:
            translated_dict[schema[0]] = translated[0]
        else:
            for i in range(len(schema)):
                translated_dict[schema[i]] = translated[i]
        return translated_dict

import requests
from testTask.settings import YANDEX_API_KEY, YANDEX_FOLDER_ID


class YandexApi:
    token = YANDEX_API_KEY
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
        for i in range(len(schema)):
            translated_dict[schema[i]] = translated[i]
        return translated_dict

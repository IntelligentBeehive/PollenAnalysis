import json
import requests
import yaml
import inspect
from Domain import Pollen


class PostController:
    def post_pollen(self, pollen):
        if inspect.isclass(Pollen):
            print('Posting pollen to API')
            url = 'http://192.168.43.4:8090/pollen/'
            payload = yaml.dump(pollen)
            headers = {'content-type': 'application/json'}
            response = requests.post(url, data=json.dumps(payload), headers=headers)
            print(response.text)

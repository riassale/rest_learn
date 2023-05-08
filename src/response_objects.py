class TrelloObject:
    def __init__(self, response):
        self._response = response
        self._get_attributes()

    def _get_attributes(self):
        if not self._response.ok:
            raise Exception(f'Error: {self._response.status_code}. {self._response.reason}')
        else:
            for k, v in self._response.json().items():
                self.__setattr__(k, v)

class TrelloObjectList(TrelloObject):
    def _get_attributes(self):
        if not self._response.ok:
            raise Exception(f'Error: {self._response.status_code}. {self._response.reason}')
        else:
            json = self._response.json()
            self.count = len(json)
            self.list = json



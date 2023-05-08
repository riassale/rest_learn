from requests import delete, get, post, put


class Api:

    def __init__(self, url, key, token):
        self.url = url
        self.token = token
        self.key = key

    def get(self, method, **kwargs):
        return get(f'{self.url}{method}/', params={'key': self.key, 'token': self.token} | kwargs)

    def post(self, method, **kwargs):
        return post(f'{self.url}{method}/', params={'key': self.key, 'token': self.token} | kwargs)

    def put(self, method, **kwargs):
        return put(f'{self.url}{method}/', params={'key': self.key, 'token': self.token} | kwargs)

    def delete(self, method, **kwargs):
        return delete(f'{self.url}{method}/', params={'key': self.key, 'token': self.token} | kwargs)

from hashlib import sha256


class MarsURLEncoder:

    def __init__(self):
        self.base_url = 'https://ma.rs/'
        self.dict_url = {}

    def encode(self, long_url):
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
        key = sha256(long_url.encode()).hexdigest()[:6]
        self.dict_url[key] = long_url
        return self.base_url + key

    def decode(self, short_url):
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        key = short_url.replace(self.base_url, '')
        return self.dict_url[key]


if __name__ == '__main__':
    m1 = MarsURLEncoder()
    print(m1.encode('https://tsup.ru/mars/marsohod-1/01-09-2023/daily_job.html'))
    print(m1.dict_url)
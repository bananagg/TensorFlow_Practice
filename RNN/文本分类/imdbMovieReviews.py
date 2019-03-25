import tarfile
import re

class ImdbMovieReviews:

    DEFAULT_URL = ''

    r_compile = re.compile(r'[a-zA-Z]+[!?.:,()]')
    def __init__(self, cache_dir, url=None):
        self._cache_dir = cache_dir
        self._url = url or type(self).DEFAULT_URL
        pass

    def __iter__(self):
        # filepath = down
        filepath = 'data/'
        with tarfile.open(filepath) as archive:


        pass
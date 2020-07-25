from .base import BasePoster

class Poster():

    def __init__(self, strategy: BasePoster):
        self._strategy = strategy

    @property
    def strategy(self) -> BasePoster:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: BasePoster) -> None:
        self._strategy = strategy

    def start_session(self, access_info, *args, **kwargs):
        return self._strategy.start_session(access_info, *args, **kwargs)

    def create_post(self, content, *args, **kwargs):
        return self._strategy.create_post(content, *args, **kwargs)

    def get_post(self, *args, **kwargs):
        return self._strategy.get_post(*args, **kwargs)

    def create_image(self, image, published, *args, **kwargs):
        return self._strategy.create_image(image, published, *args, **kwargs)

    
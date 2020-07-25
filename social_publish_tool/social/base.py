from abc import ABC, abstractmethod

class BasePoster(object):

    def __init__(self):
        pass

    @abstractmethod
    def start_session(self, access_info):
        pass

    @abstractmethod
    def end_session(self, access_info):
        pass

    @abstractmethod
    def create_post(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_post(self, *args, **kwargs):
        pass
    
    @abstractmethod
    def create_image(self, args, **kwargs):
        pass
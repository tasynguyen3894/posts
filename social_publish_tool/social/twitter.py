import tweepy
from .base import BasePoster

class TwitterPoster(BasePoster):
    name = 'twitter'
    auth = None
    api = None

    def start_session(self, access_info) -> bool:
        if all (k in access_info for k in ("CONSUMER_KEY", "CONSUMER_SECRET", "ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")):
            auth = tweepy.OAuthHandler(access_info.get('CONSUMER_KEY'), access_info.get('CONSUMER_SECRET'))
            auth.set_access_token(access_info.get('ACCESS_TOKEN'), access_info.get('ACCESS_TOKEN_SECRET'))
            self.auth = auth
            api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
            self.api = api
            return True
        return False

    def end_session(self, access_info):
        self.auth = None
        self.api = None

    def create_post(self, content, *args, **kwargs):
        if self.api is None:
            return False
        data = self.api.update_status(content, *args, **kwargs)
        return data

    def get_post(self, *args, **kwargs):
        if self.api is None:
            return False
        data = self.api.user_timeline()
        return data

    def create_image(self, image, *args, **kwargs):
        if self.api is None:
            return False
        data = self.api.update_with_media(file=image, *args, **kwargs)
        return data
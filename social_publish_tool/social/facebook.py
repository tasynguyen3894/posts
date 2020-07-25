import facebook
from .base import BasePoster

class FacebookPoster(BasePoster):
    name = 'facebook'
    graph = None

    def start_session(self, access_info) -> bool:
        if 'access_token' in access_info:
            graph = facebook.GraphAPI(access_token=access_info.get('access_token'))
            self.graph = graph
            return True
        return False

    def end_session(self, access_info):
        pass

    def create_post(self, content, *args, **kwargs):
        if self.graph is None:
            return False
        data = self.graph.put_object("me", "feed", message=content, *args, **kwargs)
        return data

    def get_post(self, *args, **kwargs):
        if self.graph is None:
            return False
        data = self.graph.get_connections(id="me", connection_name="posts")
        return data

    def create_image(self, image, published, *args, **kwargs):
        if self.graph is None:
            return False
        data = self.graph.put_photo(image=image, published=published)
        return data
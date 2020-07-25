from social_publish_tool.social.facebook import FacebookPoster
from social_publish_tool.social.poster import Poster 
import json

def main():
    access_info = {
        'access_token': 'put_your_access_token_here'
    }

    poster = Poster(strategy=FacebookPoster())
    poster.start_session(access_info=access_info)
    
    """ Get your current post """
    # posts = poster.get_post()
    # print(posts)

    """ Create post in page's feed with content """
    # id = poster.create_post(content="test with photo")
    # print(posts)

    """ Post your photo """
    # photo = poster.create_image(image=open("dummy.jpg", 'rb'), published=False)
    # print(photo)

    """ Create post in page's feed with content and attach image_id """
    # attached_media = json.dumps([{'media_fbid': 'put_photo_id_here'}])
    # posts = poster.create_post(content="test with photo", attached_media=attached_media)
    # print(posts)


if __name__ == "__main__":
    main()

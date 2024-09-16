import requests as rq


class Post:
     def __init__(self):
        blogs_data = rq.get("https://api.npoint.io/958910c61befd8625976").json()
        self.title = [content["title"] for content in blogs_data]
        self.subtitle = [content["subtitle"] for content in blogs_data]
        self.body = [content["body"] for content in blogs_data]

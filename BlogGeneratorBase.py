from abc import ABCMeta, abstractmethod

class BlogGeneratorBase(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.outline_format = {
        "topic title": "topic oneline description",
        "topic title": "topic oneline description",
    }
    @abstractmethod
    def generate_title(self, key_word):
        pass
    
    @abstractmethod
    def generate_blog_outline(self):
        pass

    @abstractmethod
    def generate_blog_post(self):
        pass

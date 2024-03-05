import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
import google.generativeai as genai
from BlogGeneratorBase import BlogGeneratorBase


load_dotenv()


class BlogGeneratorOpenAI(BlogGeneratorBase):
    def __init__(self) -> None:
        super().__init__()
        self.__api_key = os.getenv("test_key")
        self.model = OpenAI(api_key=self.__api_key)
        self.blog_title = None
        self.blog_outline = None
        self.blog_content = None

    def generate_title(self, key_word: str) -> str:
        response = self.model.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful blog title generator assistant."},
                {"role": "user", "content": f"generate a blog title with the keyword {key_word}, make it seo friendly, keep it short and simple"},
            ]
        )
        print(response.choices[0].message.content)
        self.blog_title = response.choices[0].message.content
        return self.blog_title
    
    def generate_blog_outline(self):
        response = self.model.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful blog outline generator assistant."},
                {"role": "user", "content": f"give me a blog outline on topic: {self.blog_title} in {self.outline_format} format. The response should be in python dictionary format, with topic_title as key, oneline description as value."}
            ]
        )
        self.blog_outline = response.choices[0].message.content
        print(self.blog_outline)
        return self.blog_outline
    
    def generate_blog_post(self):
        response = self.model.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful blog post generator assistant."},
                # {"role": "user", "content": f"generate html code. The html content will be a blog post with the title {self.blog_title}.The blog post should be lengthy enough. Add appropriate paragraphs to the blog post. Make the post enjoyable and easy to read. Make sure the blog post is seo friendly."},
                {"role": "user", "content": f"generate html code. The html content will be an engaging Shopify blog post aimed at empowering your customers with valuable insights on {self.blog_title}.Discuss each topic in details to attract customer."},
                
            ]
        )
        self.blog_content = response.choices[0].message.content
        return self.blog_content
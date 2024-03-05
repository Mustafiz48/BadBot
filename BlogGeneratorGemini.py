import os
import time
import ast
from dotenv import load_dotenv
import google.generativeai as genai
from BlogGeneratorBase import BlogGeneratorBase

load_dotenv()

class BlogGeneratorGemini(BlogGeneratorBase):
    def __init__(self) -> None:
        super().__init__()
        self.__api_key = os.getenv("google_api_key")
        genai.configure(api_key=self.__api_key)
        self._text_model = genai.GenerativeModel('gemini-pro')
        self._vision_model = genai.GenerativeModel('gemini-pro-vision')

        self.blog_title = None
        self.blog_content = ""
        self.blog_image = None
        self.blog_tags = None
        self.blog_meta = None
    
    def generate_title(self, key_word: str) -> str:
        response = self._text_model.generate_content(f"generate a single blog title with the keyword {key_word}, make it seo friendly, keep it short and simple")
        self.blog_title = response.text 
        print(self.blog_title)
        return self.blog_title
    
    def generate_blog_outline(self):
        message = f"""generate a blog outline with the title {self.blog_title} in {self.outline_format} format. 
        The response should be in python dictionary format, with a single line topic title as key, oneline description as value. 
        Don't give response as code, give it as text"""
        response = self._text_model.generate_content(message).text
        print(response)
        self.blog_outline = ast.literal_eval(response)
        print(self.blog_outline)
        return self.blog_outline
    
    def generate_blog_post(self):
        print()
        print()
        for key, value in self.blog_outline.items():
            time.sleep(1)
            print(f"Creating content for {key}")
            print(f"Description: {value}")
            # message = f"generate html code. The html content will be a blog post with the title {self.blog_title} and the tags {self.blog_tags}.The blog post should be at least 2500 words long. Add appropriate paragraphs to the blog post. Make the post enjoyable and easy to read. Make sure the blog post is seo friendly."
            message = f"Create an engaging paragraph for a blog on {key} following the desciption: {value}."
            response = self._text_model.generate_content(message)
            # self.blog_content += response.text
            try:
                print(response.text)
                with open(f"{self.blog_title}.txt", 'a') as f:
                    f.write(response.text)
                    f.write("\n\n")
            except Exception as e:
                print(e)
            print()
        # with open(f"Blog {self.blog_title}.html", 'w+') as f:
        #     f.write(self.blog_content)
        return self.blog_content
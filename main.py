import time
from BlogGeneratorGemini import BlogGeneratorGemini
from BlogGeneratorOpenAI import BlogGeneratorOpenAI


def generate_blog_with_gemini(key_word):
    blog_generator = BlogGeneratorGemini()
    title = blog_generator.generate_title(key_word)
    time.sleep(1)
    outline = blog_generator.generate_blog_outline()
    time.sleep(1)
    blog = blog_generator.generate_blog_post()
    print("Generated blog with Gimini")
    print(f"Blog Title: {title}")
    # print(f"Blog Content: {blog}")
    print("\n\n")
def generate_blog_with_openai(key_word):
    blog_generator = BlogGeneratorOpenAI()
    title = blog_generator.generate_title(key_word)
    outline = blog_generator.generate_blog_outline()
    # blog = blog_generator.generate_blog_post()
    print("Generated blog with OpenAI")
    print(f"Blog Title: {title}")
    # print(f"Blog Content: {blog}")


if __name__ == '__main__':
    print('Hello World!')
    key_word = input('Enter a Blog topic: ')
    generate_blog_with_gemini(key_word)
    # generate_blog_with_openai(key_word)
    print(f"Please check the generated blog")
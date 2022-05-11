import scrapy

class BlogsSpider(scrapy.Spider):
  name = 'naverblogSpider'

  start_urls=['https://d2.naver.com/home?page=0']

  def parse(self, response):
    print(response.css('h2 a'))

    # for posts in response.css('a'): 
    #   print(posts.css('a::text').get())


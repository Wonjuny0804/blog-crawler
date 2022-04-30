import scrapy

class BlogsSpider(scrapy.Spider):
  name = 'blogSpider'

  start_urls=['https://toss.tech/']
  toss_blog_url='https://toss.tech'

  def parse(self, response):

    for posts in response.css('a.css-1l8x9fy'):
      print(self.toss_blog_url + posts.css('a').attrib['href'])
      try: 
        yield {
          'title': posts.css('h4::text').get(),
          'exerpt': posts.css('p.css-1wl9bbt::text').get(),
          'date': posts.css('p.css-10958ez::text').get(),
          'href': self.toss_blog_url + posts.css('a').attrib['href']
        }
      except: 
        yield {
          'title': 'NONE',
          'exerpt': 'NONE',
          'date': 'NONE',
          'href': 'NONE'
        }


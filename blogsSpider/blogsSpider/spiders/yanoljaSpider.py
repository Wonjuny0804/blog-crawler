import scrapy

class YanoljaBlogsSpider(scrapy.Spider):
  name = 'yanoljablogSpider'

  start_urls=['https://medium.com/yanolja/archive/2022']

  def parse(self, response):

    for posts in response.css('.streamItem.streamItem--postPreview.js-streamItem'):
      print(posts.css('h3::text').get())
      print(posts.css('h4::text').get())
      print(posts.css('time::text').get())
      print(posts.css('a[source]'))

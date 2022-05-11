import scrapy

class TossPostsSpider(scrapy.Spider):
  name = "toss-posts"

  start_urls = ["https://toss.tech"]

  def parse(self, response):
    self.logger.info('hello, this is my first spider')
    posts = response.css('a.css-1l8x9fy')
    for post in posts:
      yield {
          'title': post.css('h4::text').get(),
          'exerpt': post.css('p.css-1wl9bbt::text').get(),
          'date': post.css('p.css-10958ez::text').get(),
          'href': self.toss_blog_url + post.css('a').attrib['href']
        }
  # run  scrapy crawl toss-posts -o toss-posts.json
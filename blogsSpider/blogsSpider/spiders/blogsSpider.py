import scrapy
import csv


from supabase_client import Client
from dotenv import find_dotenv, dotenv_values

config = dotenv_values(find_dotenv())




class BlogsSpider(scrapy.Spider):
  name = 'tossblogSpider'
  supabase = ''

  start_urls=['https://toss.tech/']
  toss_blog_url='https://toss.tech'
  data = []
  newData = []

  def parse(self, response):
    self.supabase = Client( 
      api_url=config.get("SUPABASE_URL"),
      api_key=config.get("SUPABASE_KEY")
    )

    header = ["title", "exercpt", "date", "href"]
    

    for posts in response.css('a.css-1l8x9fy'):
      try: 
        yield {
          'title': posts.css('h4::text').get(),
          'exerpt': posts.css('p.css-1wl9bbt::text').get(),
          'date': posts.css('p.css-10958ez::text').get(),
          'href': self.toss_blog_url + posts.css('a').attrib['href']
        }
        self.data.append([
          posts.css('h4::text').get(),
          posts.css('p.css-1wl9bbt::text').get(),
          posts.css('p.css-10958ez::text').get(),
          self.toss_blog_url + posts.css('a').attrib['href'] 
        ])

        self.newData.append({
         'title': posts.css('h4::text').get(),
          'exerpt': posts.css('p.css-1wl9bbt::text').get(),
          'date': posts.css('p.css-10958ez::text').get(),
          'href': self.toss_blog_url + posts.css('a').attrib['href'] 
        })
        # file = open("toss-blog-posts.csv", "a")
        # writer = csv.writer(file)
      except: 
        yield {
          'title': 'NONE',
          'exerpt': 'NONE',
          'date': 'NONE',
          'href': 'NONE'
        }
      
    with open("toss-blog-posts.csv", "a", encoding='UTF-8', newline="") as file: 
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(self.data)

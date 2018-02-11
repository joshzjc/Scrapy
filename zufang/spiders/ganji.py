import scrapy
from ..items import ZufangItem

class Ganji(scrapy.Spider):

    name = "zufang"
    start_urls = ['http://yf.58.com/chuzu/?utm_source=market&spm=b-31580022738699-me-f-862.mingzhan&PGTID=0d100000-028f-5a30-5168-959f19c5e7dc&ClickID=3']

    def parse(self,response):
        print(response)
        zf = ZufangItem()
        title_list = response.xpath("/html/body/div[3]/div[1]/div[5]/div[2]/ul/li/div[2]/h2/a[1]/text()").extract()
        money_list = response.xpath("/html/body/div[3]/div[1]/div[5]/div[2]/ul/li/div[3]/div[2]/b/text()").extract()

        for a,b in zip(title_list,money_list):
            zf['title'] = a
            zf['money'] = b
            yield zf
           # print(a+':'+b)

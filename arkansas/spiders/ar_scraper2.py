import scrapy
import csv

domain = "https://www.arkleg.state.ar.us"


class ArScraperSpider(scrapy.Spider):
    name = 'ar_2'
    # allowed_domains = ['https://www.arkleg.state.ar.us/Acts/SearchByRange?start=0']
    start_urls = ['https://www.arkleg.state.ar.us/Acts/SearchByRange?start=20&startAct=1&endAct=188&ddBienniumSession=2021%2F2021R#SearchResults']

    def parse(self, response):
        try:
            name = response.xpath("//div[@class='col-xs-5 col-sm-5 col-md-5']/text()").getall()
            bill = response.xpath('//div[@aria-colindex="3"]/a/text()').getall()
            links = response.xpath('//div[@class="col-md-1 col-lg-1 meetingButtons mobileButtons"]/a/@href').getall()
            with open(R'E:\arkansas_crawl\arkansas\output_2.csv',"w",newline=None, encoding='utf8') as myfile:
                csvwriter = csv.writer(myfile,delimiter=",",lineterminator='\r')
                csvwriter.writerow(['Doc Name','Bill NO.','Doc URL'])
                for a,b,c in zip(name,bill,links):
                    csvwriter.writerow([a,b,domain+c])
                myfile.close()
            print(name)

        except Exception as e:
            print(e)
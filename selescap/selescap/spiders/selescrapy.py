import scrapy
import selenium 
from scrapy_selenium import SeleniumRequest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SelescrapySpider(scrapy.Spider):
    name = "selescrapy"
    # allowed_domains = ["www.gso.gov.vn"]
    # start_urls = ["https://www.gso.gov.vn/"]



    def start_requests(self):
        yield SeleniumRequest(
            url = "https://www.gso.gov.vn",
            wait_time=3,
            screenshot=True,
            callback = self.parse
        )
        

    def parse(self, response):

        driver = response.request.meta['driver']
        driver.get("https://www.gso.gov.vn")
import requests
from parsel import Selector


class NewsScraper:
    URL = "https://www.prnewswire.com/news-releases/news-releases-list/"
    HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q =0.9,image/avif,image/ webp,*/*;q=0.8",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0"
    }
    PHONE_NUMBER = '//div[@class="footer-num "]/a/text()'
    DESCRIPTION_XPATH = '//p[@class="remove-outline"]/text()'
    DATE_XPATH = '//div[@class="col-sm-8 col-lg-9 pull-left card"]/h3/small/text()'
    IMAGE_XPATH = '//div[@class="row newsCards"]//img/@src'
    TITLE_XPATH = '//div[@class="col-sm-8 col-lg-9 pull-left card"]/h3/text()'
    LINK_XPATH = '//a[@class="newsreleaseconsolidatelink display-outline w-100"]/@href'

    def scrape_data(self):
        response = requests.get(self.URL, headers=self.HEADERS)
        # print(response.text)
        tree = Selector(text=response.text)
        links = tree.xpath(self.LINK_XPATH).getall()
        return links[:5]
        # for description in descriptions:
        #     print(description)


if __name__ == "__main__":
    scraper = NewsScraper()
    scraper.scrape_data()


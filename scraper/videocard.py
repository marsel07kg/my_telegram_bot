# import requests
# from parsel import Selector
#
# class VideoCardScraper:
#     URL = "https://lindeal.com/rating/luchshie-proizvoditeli-videokart-rejting-top-16-vedushchikh-firm-v-mire"
#     HEADERS = {
#         "Accept":"text/html,application/xhtml+xml,application/xml;q = 0.9,image/avif,image/webp,*/*;q=0.8",
#         "Accept-Language":"ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
#         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0"
#     }
#     IMAGE_XPATH = '//div[@class="content space-y-3 mb-3 "]//img/@src'
#     TITLE_XPATH = '//div[@class="content space-y-3 mb-3 "]/h2/text()'
#     PARAGRAPH_XPATH = '//div[@class="content space-y-3 mb-3 "]/p/text()'
#
#     def scrape_data(self):
#         response = requests.get(self.URL, headers=self.HEADERS)
#         tree = Selector(text=response.text)
#         links = tree.xpath(self.IMAGE_XPATH).getall()
#         return links[:5]
#
# if __name__ == "__main__":
#     scraper = VideoCardScraper()
#     scraper.scrape_data()
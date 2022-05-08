from copyreg import constructor
from controller.scroll_down import ScrollDown
from module.chrome_instance import driver


class Shopping:
    def __init__(self):
        self.__url = "https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%EC%83%A4%EC%9B%8C%20%ED%95%84%ED%84%B0&pagingIndex=1&pagingSize=40&productSet=total&query=%EC%83%A4%EC%9B%8C%20%ED%95%84%ED%84%B0&sort=rel&timestamp=&viewType=list"

    def get_url(self):
        driver.get(self.__url)

    def scroll_down(self):
        ScrollDown().run()
    
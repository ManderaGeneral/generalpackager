
import os
import re
import subprocess
import sys
from pprint import pprint

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


from generalfile import Path
from generallibrary import Log, Terminal, EnvVar, AutoInitBases, DecoContext
from generalpackager import Packager, LocalRepo
from generalpackager.api.venv import Venv




# genvector = Packager("genvector")
# print(list(genvector.localrepo.list_packages(local=False)))

from selenium.common import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By


class KeepTrying(DecoContext):
    def run_func_again(self, result, exception):
        if isinstance(exception, NoSuchElementException):
            return True

Log("selenium").configure_stream()
# Log("root").configure_stream()



class Coda:
    def __init__(self, url):
        self.url = url
        self.driver = self._load_driver()

    def _load_driver(self):
        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        options.add_argument(r'--user-data-dir=C:\Users\ricka\AppData\Local\Google\Chrome\User Data')
        options.add_argument('--profile-directory=Default')
        # options.add_argument('--disable-extensions')

        # options.add_argument("--no-sandbox")
        # options.add_argument("--disable-setuid-sandbox")
        # options.add_argument("--remote-debugging-port=9222")
        # options.add_argument("--disable-dev-shm-using")
        # options.add_argument("--disable-extensions")
        # options.add_argument("--disable-gpu")
        # options.add_argument("start-maximized")
        # options.add_argument("disable-infobars")

        # driver = webdriver.Chrome(options=options)
        chrome_driver_path = ChromeDriverManager().install()
        # chrome_driver_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        # print(chrome_driver_path)
        # options.add_argument('--disable-dev-shm-usage')
        # (The process started from chrome location C:\Program Files\Google\Chrome\Application\chrome.exe is no longer running, so ChromeDriver is assuming that Chrome has crashed.)
        #                                           C:\Users\ricka\.wdm\drivers\chromedriver\win32\110.0.5481\chromedriver.exe
        service = Service(executable_path=chrome_driver_path)
        # driver = webdriver.Chrome(options=options)
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(self.url)
        return driver

    @staticmethod
    def _get_element_by_xpath(driver, xpath):
        try:
            return driver.find_element("xpath", xpath)
        except NoSuchElementException:
            return False

    def wait_for_load(self, method, timeout):
        return WebDriverWait(driver=self.driver, timeout=timeout).until(method=method)

    def _find_by_innerText(self, name, timeout) -> WebElement:
        _xpath = f"//*[text()='{name}']"
        def method(driver, xpath=_xpath):
            return self._get_element_by_xpath(driver=driver, xpath=xpath)
        return self.wait_for_load(method=method, timeout=timeout)

    def get_table_by_name(self, name, timeout=0):
        return self._find_by_innerText(name=name, timeout=timeout)

    def get_column(self, table, name, timeout=0):
        return self._find_by_innerText(name=name, timeout=timeout)



# HERE ** Had to close chrome window for it to work. Maybe make seperate profile, vaguely remember doing that.
# Headless gave error: selenium.common.exceptions.WebDriverException: Message: unknown error: unable to discover open pages

coda = Coda("https://coda.io/d/Private_dtCdrNV5ox6/Test_suM-G#findthis_tu5lZ/r1?viewMode=edit")

table = coda.get_table_by_name("findthis", 30)
column = coda.get_column(table=table, name="Name")

ActionChains(coda.driver).context_click(column)

print(table, column)







import json
import os
from dataclasses import dataclass, fields
from importlib import import_module

import pkg_resources

from generalpackager import *
from generalfile import Path
from generallibrary import Recycle, SigInfo, getsize, Log, replace

from pprint import pprint


Packager().file_by_relative_path(".github/workflows/workflow.yml").generate()


# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://text-compare.com/")
# driver.maximize_window()
# driver.execute_script("arguments[0].value = arguments[1];", driver.find_element("id", "inputText1"), str(data))
# driver.execute_script("arguments[0].value = arguments[1];", driver.find_element("id", "inputText2"), str(loaded))
# driver.find_element_by_class_name("compareButtonText").click()
#
# while True:
#     pass





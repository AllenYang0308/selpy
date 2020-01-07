import glob
from selenium.webdriver.firefox import webdriver
from selenium.webdriver.firefox.options import Options

FIREFOX = {
    "browserName": "firefox",
    "marionette": True,
    "acceptInsecureCerts": True,
}

import glob

def test():
    for name in glob.glob('firefox/*'):
        print( name )

def init_web_driver():

    options = Options()
    options.add_argument("-headless")

    return webdriver.WebDriver(executable_path="ezselenium/firefox/geckodriver", firefox_binary="ezselenium/firefox/firefox", log_path=None, service_log_path=None, capabilities=FIREFOX, firefox_options=options)

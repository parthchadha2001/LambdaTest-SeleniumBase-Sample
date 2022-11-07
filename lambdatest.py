from selenium import webdriver
from seleniumbase import BaseCase
from selenium.webdriver.remote.remote_connection import RemoteConnection
from os import environ
import time
class OverrideDriverTest(BaseCase):
    def get_new_driver(self, *args, **kwargs):
        """This method overrides get_new_driver() from BaseCase."""
        options = webdriver.ChromeOptions()
        options.browser_version = "97"
        options.platform_name = "Windows 11"
        lt_options = {};
        lt_options["project"] = "Untitled";
        lt_options["w3c"] = True;
        lt_options["goog:chromeOptions"] = {"args":["--use-fake-device-for-media-stream","--use-fake-ui-for-media-stream"]}
        options.set_capability('LT:Options', lt_options);
        username = environ.get('LT_USERNAME', None)
        access_key = environ.get('LT_ACCESS_KEY', None)
        selenium_endpoint = "http://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key)
        executor = RemoteConnection(selenium_endpoint)
        return webdriver.Remote(
        command_executor=executor,
        options=options
         )
    def test_simple(self):
        self.open("https://webcamtests.com/check")
        time.sleep(5)
        self.click("button#webcam-launcher")
        time.sleep(5)
        self.click('button[data-action="stopWebcam"]')

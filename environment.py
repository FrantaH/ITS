import selenium
from behave import *
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


def before_all(context):
	context.driver = webdriver.Remote(command_executor='http://mys01.fit.vutbr.cz:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
	context.driver.implicitly_wait(10)
	
def after_all(context):
	context.driver.get("http://mys01.fit.vutbr.cz:5000/reset/20")
	context.driver.quit()

def before_scenario(context, scenario):
	if scenario.name == 'Zobrazení možností registrace' or scenario.name == 'Zobrazení přihlášení':
		context.driver.get("http://mys01.fit.vutbr.cz:8020/index.php?route=account/logout")
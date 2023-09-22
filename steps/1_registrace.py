# from behave import *
import selenium
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotSelectableException
from selenium.webdriver.support.ui import Select
import time


@given("hlavní stránka opencart")
def step_impl(context):
	context.driver.get("http://mys01.fit.vutbr.cz:8020")


@when('uživatel klikne na tlačítko "My Account"')
def step_impl(context):
	time.sleep(1)
	context.driver.find_element_by_xpath("//*[@id=\"top-links\"]/ul/li[2]/a").click()


@then("objeví se okénko s možností registrace a loginu")
def step_impl(context):
	assert("true" == context.driver.find_element_by_xpath("//*[@id=\"top-links\"]/ul/li[2]/a").get_attribute("aria-expanded"))


@given("okenko s možností registrace a loginu")
def step_impl(context):
	context.execute_steps('''
	given hlavní stránka opencart
	when uživatel klikne na tlačítko "My Account"
	''')


@when('uživatel klikne na tlačítko "register"')
def step_impl(context):
	context.driver.find_element_by_xpath("//*[@id=\"top-links\"]/ul/li[2]/ul/li[1]/a").click()


@then("otevře se formulář s registračními údaji")
def step_impl(context):
	assert("http://mys01.fit.vutbr.cz:8020/index.php?route=account/register" == context.driver.current_url)


@given("formulář registrace")
def step_impl(context):
	context.driver.get("http://mys01.fit.vutbr.cz:8020/index.php?route=account/register")


@when("uživatel vyplní všechny nutné \(hvězdičkou označené\) údaje")
def step_impl(context):
	time.sleep(1)
	context.driver.find_element_by_xpath("//*[@id=\"input-firstname\"]").send_keys("asd")
	context.driver.find_element_by_xpath("//*[@id=\"input-lastname\"]").send_keys("asd")
	context.driver.find_element_by_xpath("//*[@id=\"input-email\"]").send_keys("s@s.s")
	context.driver.find_element_by_xpath("//*[@id=\"input-telephone\"]").send_keys("111 222 333")
	context.driver.find_element_by_xpath("//*[@id=\"input-address-1\"]").send_keys("asd")
	context.driver.find_element_by_xpath("//*[@id=\"input-city\"]").send_keys("asd")
	context.driver.find_element_by_xpath("//*[@id=\"input-postcode\"]").send_keys("111 11")
	context.driver.find_element_by_xpath("//*[@id=\"input-country\"]").select_by_index(3)
	context.driver.find_element_by_xpath("//*[@id=\"input-zone\"]").select_by_index(3)
	context.driver.find_element_by_xpath("//*[@id=\"input-password\"]").send_keys("asdf")
	context.driver.find_element_by_xpath("//*[@id=\"input-confirm\"]").send_keys("asdf")


@when('označí checkbox "I have read and agree to the Privacy Policy"')
def step_impl(context):
	context.driver.find_element_by_xpath("//*[@id=\"content\"]/form/div/div/input[1]").click()


@when('klikne na tlačítko "Continue"')
def step_impl(context):
	context.driver.find_element_by_xpath("//*[@id=\"content\"]/form/div/div/input[2]").click()
	

@then("stránka s potvrzením se zobrazí")
def step_impl(context):
	time.sleep(1)
	assert("http://mys01.fit.vutbr.cz:8020/index.php?route=account/success" == context.driver.current_url)


@then("uživatel je přihlášen")
def step_impl(context):
	time.sleep(1)
	assert(context.driver.find_element_by_xpath("//*[@id=\"top-links\"]/ul/li[2]/ul/li[5]/a").text() == "Logout")


@when("uživatel nevyplní nic")
def step_impl(context):
	pass


@then("označí se všechny nutné položky jako chybné")
def step_impl(context):
	time.sleep(1)
	errors = context.driver.find_elements_by_class_name("text-danger")
	assert(len(errors) == 9)

	assert("Warning" in context.driver.find_element_by_xpath("/html/body/div[2]/div[1]").text())


@when("uživatel vyplní validní informace kromě telefonu \(písmena\)")
def step_impl(context):
	time.sleep(1)
	context.driver.find_element_by_xpath("//*[@id=\"input-firstname\"]").send_keys("asd")
	context.driver.find_element_by_xpath("//*[@id=\"input-lastname\"]").send_keys("asd")
	context.driver.find_element_by_xpath("//*[@id=\"input-email\"]").send_keys("s@s.s")
	
	context.driver.find_element_by_xpath("//*[@id=\"input-telephone\"]").send_keys("asdadsasd") 
	
	context.driver.find_element_by_xpath("//*[@id=\"input-address-1\"]").send_keys("asd")
	context.driver.find_element_by_xpath("//*[@id=\"input-city\"]").send_keys("asd")
	context.driver.find_element_by_xpath("//*[@id=\"input-postcode\"]").send_keys("111 11")
	context.driver.find_element_by_xpath("//*[@id=\"input-country\"]").select_by_index(3)
	context.driver.find_element_by_xpath("//*[@id=\"input-zone\"]").select_by_index(3)
	context.driver.find_element_by_xpath("//*[@id=\"input-password\"]").send_keys("asdf")
	context.driver.find_element_by_xpath("//*[@id=\"input-confirm\"]").send_keys("asdf")


@then("chyba v telefonním čísle")
def step_impl(context):
	time.sleep(1)
	context.driver.find_element_by_class_name("text-danger")
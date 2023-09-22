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



@when('klikne tlačítko "Login"')
def step_impl(context):
	time.sleep(1)
	context.driver.find_element_by_xpath("//*[@id=\"top-links\"]/ul/li[2]/ul/li[2]/a").click()


@then("otevře se záložka Account/Login")
def step_impl(context):
	time.sleep(1)
	assert("http://mys01.fit.vutbr.cz:8020/index.php?route=account/login" == context.driver.current_url)


@given("formulář Přihlášení")
def step_impl(context):
	context.driver.get("http://mys01.fit.vutbr.cz:8020/index.php?route=account/login")


@given("zadaný účet neexistuje")
def step_impl(context):
	pass


@when('uživatel vyplní jakékoli údaje do "E-Mail Address" a "Password"')
def step_impl(context):
	pass


@when("zmáčkne tlačítko Login")
def step_impl(context):
	time.sleep(1)
	context.driver.find_element_by_xpath("//*[@id=\"content\"]/div/div[2]/div/form/input").click()


@then("zobrazí se Chyba")
def step_impl(context):
	time.sleep(1)
	context.driver.find_element_by_xpath("/html/body/div[2]/div[1]")
	

@given("zadaný účet existuje")
def step_impl(context):
	pass


@when('uživatel vyplní správné údaje do "E-Mail Address" a "Password"')
def step_impl(context):
	time.sleep(1)
	context.driver.find_element_by_xpath("//*[@id=\"input-email\"]").send_keys("s@s.s")
	context.driver.find_element_by_xpath("//*[@id=\"input-password\"]").send_keys("asdf")


@then('zobrazí se obrazovka "Account"')
def step_impl(context):
	time.sleep(1)
	assert("http://mys01.fit.vutbr.cz:8020/index.php?route=account/account" == context.driver.current_url)
	context.driver.find_element_by_xpath("//*[@id=\"top-links\"]/ul/li[2]/ul/li[5]/a")


@given("přihlášený uživatel")
def step_impl(context):
	pass


@when('uživatel zmáčkne tlačítko "Logout"')
def step_impl(context):
	time.sleep(1)
	context.driver.find_element_by_xpath("//*[@id=\"top-links\"]/ul/li[2]/ul/li[5]/a").click()


@then('zobrazí se obrazovka "Account Logout"')
def step_impl(context):
	time.sleep(1)
	assert("Account Logout" in context.driver.title)
	assert("http://mys01.fit.vutbr.cz:8020/index.php?route=account/logout" == context.driver.current_url)


@when('uživatel zmáčkne tlačítko "Forgotten Password"')
def step_impl(context):
	time.sleep(1)
	context.driver.find_element_by_xpath("//*[@id=\"content\"]/div/div[2]/div/form/div[2]/a").click()


@then('zobrazí se obrazovka "Forgot Your Password\?"')
def step_impl(context):
	time.sleep(1)
	assert("http://mys01.fit.vutbr.cz:8020/index.php?route=account/forgotten" == context.driver.current_url)
	assert("Forgot Your Password?" in context.driver.title)

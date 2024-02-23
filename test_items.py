from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_cart_button(browser):
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    time.sleep(5)
    assert "Añadir al carrito" in button.text
    #time.sleep(30)
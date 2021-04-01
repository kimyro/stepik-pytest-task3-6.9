import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" # First link

# Comment the first link and uncomment link below to check the page with missing 'Add to basket' button
# link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/hackers-painters_185/"

def test_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(10)
    button = browser.find_elements_by_css_selector("#add_to_basket_form > button")
    assert button, "The button you are looking for wasn't found"


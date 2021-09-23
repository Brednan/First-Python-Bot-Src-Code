from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get('https://www.python.org/')

def get_event_titles(search):
    search_bar = driver.find_element_by_name('q')
    search_bar.clear()
    search_bar.click()
    search_bar.send_keys(search)
    search_bar.send_keys(Keys.ENTER)

    try:
        list_of_results = driver.find_element_by_xpath('//*[@id="content"]/div/section/form/ul')
        results = list_of_results.find_elements_by_tag_name('li')
        res = []
        for e in results:
            res.append(e.find_element_by_tag_name('h3').text)
    except:
        res = []


    return res

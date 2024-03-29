from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://cgmix.uscg.mil/IIR/IIRSearch.aspx")

begin_date_xpath = '//*[@id="TextBoxFromDate"]'

begin_date = driver.find_element(By.XPATH, begin_date_xpath)

end_date_xpath = '//*[@id="TextBoxToDate"]'
end_date = driver.find_element(By.XPATH, end_date_xpath)


"""
Date : MM/DD/YYYY
"""
def set_begin_date(date):
    begin_date.clear()
    begin_date.send_keys(date)

"""
Date : MM/DD/YYYY
"""
def set_end_date(date):
    end_date.clear()
    end_date.send_keys(date)

vessel_service_xpath = "/html/body/form/div[3]/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/div/table/tbody/tr[4]/td[2]/select"
vessel_service = driver.find_element(By.XPATH, vessel_service_xpath)

involved_org_xpath = "/html/body/form/div[3]/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/div/table/tbody/tr[6]/td[2]/input"
involved_org = driver.find_element(By.XPATH, involved_org_xpath)

def set_involved_org(org):
    involved_org.clear()
    involved_org.send_keys(org)

def set_vessel_service(service):
    vessel_service.send_keys(service)

kword_xpath = "/html/body/form/div[3]/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/div/table/tbody/tr[8]/td[2]/input"
kword = driver.find_element(By.XPATH, kword_xpath)

def set_kword(kw):
    kword.clear()
    kword.send_keys(kw)

set_begin_date("01/01/2020")

search_btn_xpath = '/html/body/form/div[3]/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/div/table/tbody/tr[13]/td/input[1]'
search_btn = driver.find_element(By.XPATH, search_btn_xpath)

search_btn.click()


table_xpath = '/html/body/form/div[3]/div/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td/div/table/tbody'
table = driver.find_element(By.XPATH, table_xpath)

trs = table.find_elements(By.TAG_NAME, 'tr')

details_links = []
# first row is header
for i, tr in enumerate(trs[1:]):
    try:
        tds = tr.find_elements(By.TAG_NAME, 'td')
        details_link = tds[0].find_element(By.TAG_NAME, 'a')
        details_links.append(details_link)
    except:
        print("failed on " + str(i))
        details_links.append(tds)

# This works, need to do QA
        # maybe a screen grab?
def process_page(driver, qa=False):
    from time import sleep
    from random import randint
    sleep(randint(1, 3))
    div_xpath = "/html/body/form/div[3]/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/div"
    div = driver.find_element(By.XPATH, div_xpath)
    tbls = div.find_elements(By.TAG_NAME, 'table')
    for tbl in tbls:
        print(tbl.text)
    if qa:
        # need to start at top of page
        driver.execute_script("window.scrollTo(0, 0)")
        # need to loop over length of page
        # can I get the length of the page from the driver object?
        ht = driver.execute_script("return document.body.scrollHeight")
        for i in range(0, ht, 100):
            driver.execute_script("window.scrollTo(0, " + str(i) + ")")
            driver.save_screenshot(str(i) +"_screenshot.png")
        


# TODO :: decide storage method for the text data

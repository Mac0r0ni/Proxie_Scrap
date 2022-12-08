from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.sslproxies.org/")
tbody = driver.find_element_by_tag_name("tbody")
tr = tbody.find_elements_by_tag_name("tr")
for column in tr:
    column = column.text.split(" ")
    with open("proxy.txt", "a") as text_file:
        text_file.write(column[0] + ":" + column[1] + "\n")
driver.quit()
print("Proxies have been scrapped and saved")

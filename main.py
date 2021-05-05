from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--headless")

url = "https://defirate.com/lend/"
driver = webdriver.Firefox(options=options)
driver.get(url)
day_avg_btn = (
    driver.find_element_by_id("selector-table")
    .find_elements_by_tag_name("span")[1]
    .find_element_by_xpath("./..")
    .click()
)

main_table = driver.find_element_by_id("secondary-table")
header = (
    main_table.find_element_by_tag_name("thead")
    .find_element_by_tag_name("tr")
    .find_elements_by_tag_name("th")
)


def get_header_name():
    header_name = []
    for i in range(1, len(header)):
        col = header[i]
        header_name.append(col.find_element_by_class_name("name").text)
    return header_name


header_name = get_header_name()

rows = main_table.find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")


def extract_name_price(row):

    name = row.find_element_by_class_name("name").text
    cols = row.find_elements_by_class_name("rate-cell")
    cols_text = [col.text for col in cols]
    return {"name": name, "rates": cols_text}


list_dict_name_rate = [extract_name_price(row) for row in rows]

result = []
for elem in list_dict_name_rate:
    token = elem["name"]
    rates = dict(zip(header_name, elem["rates"]))
    clean_rates = {k: float(v[:-1]) for k, v in rates.items() if v != "–"}
    if clean_rates:
        maximum = max(clean_rates.values())
        key = filter(lambda x: clean_rates[x] == maximum, clean_rates.keys())
        result.append({"token": token, "rates":  maximum, 'name': list(key)[0]})

sorted_result = sorted(result, key=lambda x: x['rates'])
print(sorted_result)

driver.close()

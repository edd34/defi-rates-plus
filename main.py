from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from pprint import pprint
from helpers import extract_name_price, get_header_name

options = Options()
options.add_argument("--headless")

url = "https://defirate.com/lend/"
driver = webdriver.Firefox(options=options)
driver.get(url)

# # Uncomment in order to get rates for lending
# day_avg_btn = (
#     driver.find_element_by_id("selector-table")
#     .find_elements_by_tag_name("span")[1]
#     .find_element_by_xpath("./..")
#     .click()
# )


main_table = driver.find_element_by_id("main-table")
header = (
    main_table.find_element_by_tag_name("thead")
    .find_element_by_tag_name("tr")
    .find_elements_by_tag_name("th")
)





header_name = get_header_name(header)

rows = main_table.find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")





list_dict_name_rate = [extract_name_price(row) for row in rows]

driver.close()
result = []
for elem in list_dict_name_rate:
    token = elem["name"]
    rates = dict(zip(header_name, elem["rates"]))
    clean_rates = {k: float(str(v[:-1])) for k, v in rates.items() if not v in ["–", ""]}
    if clean_rates:
        maximum = max(clean_rates.values())
        key = filter(lambda x: clean_rates[x] == maximum, clean_rates.keys())
        result.append({"token": token, "rates":  maximum, 'name': list(key)[0]})

sorted_result = sorted(result, key=lambda x: x['rates'], reverse=True)
pprint(sorted_result)
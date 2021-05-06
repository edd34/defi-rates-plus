def get_header_name(header):
    header_name = []
    for i in range(1, len(header)):
        col = header[i]
        header_name.append(col.find_element_by_class_name("name").text)
    return header_name

def extract_name_price(row):
    name = row.find_element_by_class_name("name").text
    cols = row.find_elements_by_class_name("rate-cell")
    cols_text = [col.text for col in cols]
    return {"name": name, "rates": cols_text}
import time
import json
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

# Config Selenium
gecko_driver_path = '/usr/local/bin/geckodriver'
service = Service(gecko_driver_path)
options = webdriver.FirefoxOptions()
options.headless = True

# URL
url = "https://steamdb.info/sales/"

def initialize_driver():
    """Inicializa o driver do Selenium."""
    driver = webdriver.Firefox(service=service, options=options)
    return driver

def extract_page_data(driver):
    """Extrai os dados da página."""
    rows = []
    try:
        table = driver.find_element(By.CLASS_NAME, 'table-sales')
        for row in table.find_elements(By.TAG_NAME, 'tr')[1:]:
            cols = row.find_elements(By.TAG_NAME, 'td')
            if len(cols) > 4:
                name = extract_text(cols[2], 'a')
                subinfo1, subinfo2 = extract_subinfo(cols[2])
                discount = cols[3].text.strip()
                price = cols[4].text.strip()
                rating = cols[5].text.strip()
                release = cols[6].text.strip()
                rows.append({
                    'Name': name,
                    'Info1': subinfo1,
                    'Info2': subinfo2,
                    'Discount %': discount,
                    'Price': price,
                    'Rating': rating,
                    'Release': release
                })
    except Exception as e:
        print(f"Erro ao extrair dados: {e}")
    return rows

def extract_text(element, tag_name):
    """Extrai texto de um elemento."""
    try:
        return element.find_element(By.TAG_NAME, tag_name).text.strip()
    except:
        return ""

def extract_subinfo(element):
    """Extrai informações adicionais do elemento."""
    try:
        subinfo_element = element.find_element(By.CLASS_NAME, 'subinfo')
        subinfo1 = subinfo_element.find_element(By.CLASS_NAME, 'cat').text.strip()
        subinfo2 = subinfo_element.find_element(By.CLASS_NAME, 'highest-discount').text.strip()
        return subinfo1, subinfo2
    except:
        return "", ""

def save_data_to_json(data, filename):
    """Salva os dados extraídos em um arquivo JSON."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Dados extraídos e salvos em '{filename}'")

def save_data_to_csv(data, filename):
    """Salva os dados extraídos em um arquivo CSV."""
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding='utf-8')
    print(f"Dados extraídos e salvos em '{filename}'")

def navigate_and_extract_data(driver, url):
    """Navega pelas páginas e extrai os dados."""
    all_rows = []
    driver.get(url)
    time.sleep(5)
    while True:
        rows = extract_page_data(driver)
        all_rows.extend(rows)
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, 'button.dt-paging-button.next')
            if 'disabled' in next_button.get_attribute('class'):
                break
            next_button.click()
            time.sleep(5)
        except Exception as e:
            print(f"Erro ao acessar a próxima página: {e}")
            break
    return all_rows

def main(output_format='json'):
    driver = initialize_driver()
    try:
        data = navigate_and_extract_data(driver, url)
        if output_format == 'json':
            save_data_to_json(data, 'steam_sales.json')
        elif output_format == 'csv':
            save_data_to_csv(data, 'steam_sales.csv')
        else:
            print(f"Formato de saída '{output_format}' não suportado.")
    finally:
        driver.quit()

if __name__ == "__main__":
    output_format = input("Escolha o formato de saída (json/csv): ").strip().lower()
    main(output_format)

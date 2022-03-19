from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import re
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium.webdriver import ChromeOptions

def extract():
    """ Crawling covid data from covid19.gov.vn

    Agrs:
        Nothing, because with different page we got different code.

    Returns:
        2 dataframe: 
        + data1 - cases covid per city in current day.
        + data2 - dead cases in current day.
    
    Raises:
        Not yet.
    """
    # ------------------ Crawl Data ------------------ #
    #chromedriver_path = '/usr/local/bin/chromedriver' #---> define path of chromedriver in: '/usr/local/bin/chromedriver'. In case chromedriver not in $PATH.
    opts = ChromeOptions()
    opts.add_argument("--headless")
    opts.add_argument("window-size=1920,1080")

    driver = webdriver.Chrome(options=opts) #---> provide path location of chromedriver to excute. But to advoid unexpected error
    driver.maximize_window()
    driver.get('https://covid19.gov.vn/') #---> provide url to crawl
    

    iframe = driver.find_elements(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe[1]) #--> data we need in iframe[1]. Need to switch into there to get data. 

    # ------------------ PARSE HTML TO GET DATA ------------------ #
    soup = BeautifulSoup(driver.page_source, 'html.parser') # --> choose html-parser to parse html(page source).

    cases = soup.find_all("span", class_="red")
    case = []
    for i in range(len(cases)):
        if ''.join(re.findall("[0-9]",cases[i].text)).isnumeric():
            case.append(int(''.join(re.findall("[0-9]",cases[i].text))))
        else: case.append(0)

    cities = soup.find_all("span", class_="city")
    city = []
    for i in range(len(cities)):
        if i == 0:
            continue
        else: city.append(cities[i].text)

    date = datetime.today().strftime('%Y-%m-%d')
    df = pd.DataFrame({"City":city,"Cases":case,"Date":date})

    df_cases = df.sort_values(by=['Cases'], ascending=False).reset_index(drop=True)
    #---> sort dataframe by cases high to low. drop=True mean we drop existing index 
    # instead of adding it as and additional column to your df


    # ------------------ GET DEATH OF DAY IN HOVER POP-UP ELEMENT ------------------ #
    driver.find_element(By.ID, "death").click() #---> click to "death" tab.
    time.sleep(2)

    test = driver.find_elements(By.XPATH, "//*[name()='svg']//*[name()='g' and @class='highcharts-markers highcharts-series-1 highcharts-spline-series highcharts-tracker']/*[name()='path']")
    # ---> provide xpath to reach needed elements.
    test[6].click()

    ActionChains(driver).move_to_element(test[6]).perform() #---> test[6] is latest chart.
    a = driver.find_elements(By.TAG_NAME, "tspan")
    death = int(a[3].text)
    df_death = pd.DataFrame({"Date":date,"Death":death}, index=[0])     

    driver.quit()
    return df_cases, df_death 

def load(df_cases,df_death):
    # ------------------ Working With GG Sheet - Append DF To GG Sheet ------------------ #
    import gspread_dataframe as gd
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
            "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]      # --> google services to use ggsheet.            

    # ---> connect to ggsheet.
    # ---> create credentials.
    credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope) # "client_secret.json" --> json key file to access google api services account.
    client = gspread.authorize(credentials) # ---> authorize credentials.

    work_sheet_link_cases = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRKwSHvbcAazVGuKeAnIF0n85gDG3ZDnmurbDbDOq7F21ZpKHQ-fDwyaTG8xXj98HcSyyjk_U1hmjWs/pub?gid=1888332389&single=true&output=csv'
    # ---> link work sheet to use. This link just can use to read data, 
    # beacause we set that ggsheet public to web with csv format to easy to read by pandas
    work_sheet_link_death = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRKwSHvbcAazVGuKeAnIF0n85gDG3ZDnmurbDbDOq7F21ZpKHQ-fDwyaTG8xXj98HcSyyjk_U1hmjWs/pub?gid=686508364&single=true&output=csv'

    # ---> append cases data
    spreadsheet_cases = client.open('csv-to-gg-sheet').worksheet('covid_cases')   # ---> open work sheet to append(write more) data

    existing_data_cases = pd.read_csv(work_sheet_link_cases)                            # ---> get existing data
    updated_data_cases = pd.concat([existing_data_cases,df_cases])                      # ---> combine new data with existing data
    gd.set_with_dataframe(spreadsheet_cases, updated_data_cases)

    # ---> append death data

    spreadsheet_death = client.open('csv-to-gg-sheet').worksheet('covid_death')   # ---> open work sheet to append(write more) data

    existing_data_death = pd.read_csv(work_sheet_link_death)                            # ---> get existing data
    updated_data_death = pd.concat([existing_data_death,df_death])                      # ---> combine new data with existing data
    gd.set_with_dataframe(spreadsheet_death, updated_data_death)

data = extract()
data_cases = data[0]
data_death = data[1]

load(data_cases,data_death)
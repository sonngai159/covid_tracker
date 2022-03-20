# Viet Nam - Automatic Covid Crawler
A crawler tool to crawl data from [Covid Viet Nam](https://covid19.gov.vn/) to google sheets automatically.
# Requires: 
1. Python - 3.9 or newer
2. Pipenv
3. Google Drive API
4. Google Sheets
5. Azure Virtual Machine
6. Tableau
7. Crontab
# Getting Started:
### 2 - Pipenv Setup:
Use `$ pip install pipenv` to install pipenv. Then move to project folder `$ cd project_folder_path`. 
With pipfile in your project's file, install all dependencies `$ pipenv install`.
### 3 - Google Drive API Setup:
- Go to [Google Cloud Platform](https://console.cloud.google.com/home/dashboard), create new project.
- Go to API & Services -> Enable Apis & services. Enable "Google Drive API" and "Google Sheets API".
- Click on IAM & Admin, go to services account, create a new services account.
- Go to created services account -> key -> ADD KEY -> Create new key -> Json type. NOTE: keep this __json's key file__ to connect with google sheets.
### 4 - Google Sheets Setup:
- Create new sheet, name it "csv-to-gg-sheet". 
- Add 1 sheet name "covid_cases" to store covid case every day, 1 sheet name "covid_death" to store covid death case every day. *Note: when change sheets name we need to change it name in source code too.
- Publish both sheets to web with csv type, save the __share link__ to use.

### 5 - Azure Virtual Machine:
### 6 - Tableau Setup:
### 7 - Crontab Setup:

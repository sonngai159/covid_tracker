![GitHub](https://img.shields.io/github/license/sonngai159/covid_crawler?style=flat-square)
![GitHub issues](https://img.shields.io/github/issues/sonngai159/covid_crawler?style=flat-square)
![GitHub pull requests](https://img.shields.io/github/issues-pr/sonngai159/covid_crawler?style=flat-square)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)
![GitHub contributors](https://img.shields.io/github/contributors/sonngai159/covid_crawler?style=flat-square)\
![GitHub watchers](https://img.shields.io/github/watchers/sonngai159/covid_crawler?style=social)
![GitHub forks](https://img.shields.io/github/forks/sonngai159/covid_crawler?style=social)
![GitHub Repo stars](https://img.shields.io/github/stars/sonngai159/covid_crawler?style=social)
# Viet Nam - Covid Tracker
A crawler tool to crawl data from [Covid Viet Nam](https://covid19.gov.vn/) to google sheets automatically.
# Requires: 
1. Python - 3.9 or newer
2. [Pipenv](#2---pipenv-setup)
3. [Google Drive API](#3---google-drive-api-setup)
4. [Google Sheets](#4---google-sheets-setup)
5. [Azure Virtual Machine](#5---azure-virtual-machine)
6. [Tableau](#6---tableau-setup)
7. [Crontab](#7---crontab-setup)
8. Basic Linux knowledges
# Getting Started:
### 2 - Pipenv Setup:
Use `$ pip install pipenv` to install pipenv. Then create & move to the folder you want to be project folder.
With pipfile in your project's file, install all dependencies `$ pipenv install`.
### 3 - Google Drive API Setup:
- Go to [Google Cloud Platform](https://console.cloud.google.com/home/dashboard), create new project.
![create_project](https://github.com/sonngai159/covid_tracker/blob/master/asset/create_project.png)
- Go to API & Services -> Enable Apis & services. Enable "Google Drive API" and "Google Sheets API".
![enable_api_services](https://github.com/sonngai159/covid_tracker/blob/master/asset/enable_services.png)
- Click on IAM & Admin, go to services account -> create a new services account.
- Move to key tab -> ADD KEY -> Create new key -> Json type. NOTE: keep this ***json's key file*** to connect with google sheets.
![create_private_key](https://github.com/sonngai159/covid_tracker/blob/master/asset/create_private_key.png)
### 4 - Google Sheets Setup:
- Create new sheet, name it "csv-to-gg-sheet" (change any as your wish, need to change in source code too). 
- Add 1 work sheet name "covid_cases" to store covid case every day, 1 work sheet name "covid_death" to store covid death case every day. *Note: when change sheets name we need to change it name in source code too.
- Publish both sheets to web with csv type, save the ***share link*** to use in script.
### 5 - Azure Virtual Machine:
- Go to [Azure](https://portal.azure.com/#home), create new Virtual Machine, save it's ***ssh_key.pem***.
- Connect with Virtual Machine throgh ssh protocol, install python. 
- Push source code, pipfile, ***ssh_key.pem*** file, ***json's key*** file to remote machine.
- Install all dependencies by pipenv at [step 2](#2---pipenv-setup).
### 6 - Tableau Setup:
- Download Tableau, use google sheet as data source, make your visualization.
- Publish Tableau visualization to the tableau public server, it will auto update(1 per day) when your google sheet data change.
![tableau](https://github.com/sonngai159/covid_tracker/blob/master/asset/public_tableau.png)
### 7 - Crontab Setup:
- On [Azure Virtual Machine](#5---azure-virtual-machine) run `$ crontab -e` -> set cronjob to run source code at every time you wish.
![cron_job](https://github.com/sonngai159/covid_tracker/blob/master/asset/cronjob.png)


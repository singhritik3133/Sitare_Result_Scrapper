# 🎓 Sitare PeopleSoft Result Scraper

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Selenium](https://img.shields.io/badge/Library-Selenium-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

A powerful automation tool built with **Python** and **Selenium** to scrape academic results from the SRMU PeopleSoft portal. It automates the login, navigation, and PDF data extraction process to generate a consolidated Excel report.

## 🚀 Features
- **Automated Navigation:** Handles complex PeopleSoft menus (Self Service > Transcript).
- **PDF Extraction:** Uses `pdfplumber` to extract CGPA from the summary table in the generated PDF.
- **Bulk Processing:** Scrapes multiple Roll Numbers in a single run.
- **Excel Export:** Automatically saves results in a clean `.xlsx` format.
- **Error Handling:** Gracefully skips invalid IDs and continues processing.

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/SRMU-Result-Scraper.git](https://github.com/YOUR_USERNAME/SRMU-Result-Scraper.git)

### 2. Repository ko "Pro" dikhane ke liye Add-ons

* **About Section:** On the right side of the repository's main page, there is an 'About' section. Add relevant Keywords/Tags there, such as: python, selenium, web-scraping, automation, peoplesoft.
* **Requirements File:** please make file`requirements.txt` write ths like this.
    ```text
    selenium
    pandas
    pdfplumber
    webdriver-manager
    openpyxl
    ```
   This allows other users to install all necessary libraries with a single command: pip install -r requirements.txt.
* **License:** Ek **MIT License** On GitHub, go to "Add file" -> "Create new file," name it LICENSE, then click "Choose a license template" and select MIT.
* **Screenshots:** If possible, include a screenshot or a GIF showing the script running in the terminal. Visuals make the repo look much more professional.

### 3. Folder Structure
You can see your page like this 
```text
├── .gitignore          (To prevent unnecessary files from being uploaded)
├── LICENSE             (MIT License)
├── README.md           (Your project manual)
├── main.py             (Your actual source code)
└── requirements.txt    (List of dependencies/libraries)

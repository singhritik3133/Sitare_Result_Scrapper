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

### 1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/SRMU-Result-Scraper.git](https://github.com/YOUR_USERNAME/SRMU-Result-Scraper.git)
### 2. Repository ko "Pro" dikhane ke liye Add-ons

* **About Section:** Repository ke main page par right side mein 'About' section hota hai. Wahan achhe **Keywords/Tags** daalein jaise: `python`, `selenium`, `web-scraping`, `automation`, `peoplesoft`.
* **Requirements File:** Ek file banayein `requirements.txt` naam se aur usme ye likh dein:
    ```text
    selenium
    pandas
    pdfplumber
    webdriver-manager
    openpyxl
    ```
    Isse doosre users sirf ek command `pip install -r requirements.txt` se saari libraries install kar payenge.
* **License:** Ek **MIT License** add karein. GitHub par "Add file" -> "Create new file" karein aur naam `LICENSE` rakhein, fir "Choose a license template" par click karke MIT select karein.
* **Screenshots:** Agar ho sake toh ek screenshot ya GIF laga dein jisme script terminal par chalti hui dikh rahi ho. Visuals se repo bahut achhi dikhti hai.

### 3. Folder Structure
Aapka repo kuch aisa dikhna chahiye:
```text
├── .gitignore          (Taaki faltu files upload na ho)
├── LICENSE             (MIT License)
├── README.md           (Aapka project manual)
├── main.py             (Aapka asli code)
└── requirements.txt    (Libraries ki list)

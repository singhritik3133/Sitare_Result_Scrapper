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

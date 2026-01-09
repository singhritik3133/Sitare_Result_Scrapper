from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import os
import pdfplumber

# ---------------- CONFIG ----------------
LOGIN_URL = "https://eyojan.srmu.ac.in/psc/ps/?cmd=login&languageCd=ENG"
PASSWORD = "123" 
TERM_VALUE = "2501" 
START_ID = 202510101200001
END_ID   = 202510101200050 # Range yahan se badha lein

downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

# ---------------- OPTIMIZED DRIVER SETUP ----------------
options = webdriver.ChromeOptions()
# options.add_argument("--headless") # Speed ke liye ise uncomment karein (browser nahi dikhega)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--blink-settings=imagesEnabled=false") # Images disable (FAST loading)

prefs = {
    "download.default_directory": downloads_path,
    "download.prompt_for_download": False,
    "plugins.always_open_pdf_externally": True,
    "profile.managed_default_content_settings.notifications": 2
}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 20)
final_data = []

def get_cgpa_from_table(file_path):
    try:
        with pdfplumber.open(file_path) as pdf:
            first_page_text = pdf.pages[0].extract_text()
            name = "Not Found"
            for line in first_page_text.split('\n'):
                if "Student's Name:" in line:
                    name = line.split("Student's Name:")[1].split("University")[0].strip()
                    break

            tables = pdf.pages[0].extract_tables()
            if tables:
                summary_table = tables[-1]
                if len(summary_table) > 1:
                    # Column 2 (Index 1) se value uthana
                    cgpa_value = summary_table[1][1]
                    return name, cgpa_value
            return name, "N/A"
    except:
        return "Error", "Error"

# ---------------- MAIN LOOP ----------------
for user_id in range(START_ID, END_ID + 1):
    try:
        print(f"🚀 Processing: {user_id}")
        driver.get(LOGIN_URL)
        
        # 1. LOGIN (Fast approach)
        wait.until(EC.presence_of_element_located((By.ID, "userid"))).send_keys(str(user_id))
        driver.find_element(By.ID, "pwd").send_keys(PASSWORD)
        driver.find_element(By.NAME, "Submit").click()

        # 2. NAVIGATION (Steps kept exactly same)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Student Progress Report')]"))).click()
        
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(.,'Main Menu')]")))
        driver.switch_to.default_content()
        
        # Fast Clicks
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Main Menu')]"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Self Service')]"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Unofficial Transcript')]"))).click()

        # 3. GENERATE
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "ptifrmtgtframe")))
        term_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@id, 'STRM')]")))
        term_input.clear()
        term_input.send_keys(TERM_VALUE)
        
        old_files = set(os.listdir(downloads_path))
        gen_btn = driver.find_element(By.XPATH, "//input[contains(@value, 'Generate')]")
        driver.execute_script("arguments[0].click();", gen_btn)
        
        # 4. FAST FILE CHECK
        timeout = 15
        start_time = time.time()
        latest_pdf = None
        
        while time.time() - start_time < timeout:
            new_files = set(os.listdir(downloads_path)) - old_files
            pdf_files = [f for f in new_files if f.endswith(".pdf")]
            if pdf_files:
                latest_pdf = os.path.join(downloads_path, pdf_files[0])
                break
            time.sleep(1)

        if latest_pdf:
            name, cgpa = get_cgpa_from_table(latest_pdf)
            final_data.append({"User ID": user_id, "Name": name, "CGPA": cgpa})
            print(f"✅ Done: {name} | {cgpa}")
            os.remove(latest_pdf)
        else:
            final_data.append({"User ID": user_id, "Name": "Timeout", "CGPA": "N/A"})

    except Exception as e:
        print(f"⚠️ Skipping {user_id} due to error")
        final_data.append({"User ID": user_id, "Name": "Error", "CGPA": "N/A"})
    
    finally:
        driver.delete_all_cookies()
        driver.switch_to.default_content()

# ---------------- SAVE ----------------
df = pd.DataFrame(final_data)
df.to_excel(os.path.join(downloads_path, "Bulk_Results.xlsx"), index=False)
print(f"\n✨ Bulk processing complete! Data saved in Downloads.")
driver.quit()

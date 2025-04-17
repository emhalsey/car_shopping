from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pathlib import Path
import pandas as pd
import json

# Path to Edge WebDriver
driver_path = Path(__file__).parent / "msedgedriver.exe"

# Run in headless mode to avoid opening the Edge browser UI
edge_options = Options()
# edge_options.add_argument('--headless')

# Set up the Selenium WebDriver for Edge
service = Service(driver_path)
driver = webdriver.Edge(service=service, options=edge_options)
# driver.implicitly_wait(30)

# URL of the car listing page
url = "https://cars.usnews.com/cars-trucks/used-cars/for-sale"

# Load the page
driver.get(url)

# Wait for a specific element to load (for example, a unique identifier on the page).  This line was written with the help of ChatGPT
WebDriverWait(driver, 60).until(
    ec.presence_of_element_located((By.XPATH, '//script[@type="application/ld+json"]'))
)

# Find the <script> tag containing the JSON-LD data
json_script = driver.find_element(By.XPATH, '//script[@type="application/ld+json"]').get_attribute('innerHTML')

# Parse the JSON data
data = json.loads(json_script)

# Initialize an empty list to hold vehicle data
scraped_data = []

# Extract specific data safely with .get() to avoid errors
vehicle_info = {
    'price': data.get('Offer', {}).get('price', 'N/A'),
    'model': data.get('model', 'N/A'),
    'year': data.get('modelDate', 'N/A'),
    'mileageFromOdometer': data.get('value', 'N/A'),
    'state': data.get('addressRegion', 'N/A'),
}

# Append the extracted data to the list
scraped_data.append(vehicle_info)

# Close the WebDriver instance
driver.quit()

# Convert to DataFrame
df = pd.DataFrame(scraped_data)

# Build the file path to ensure it is relative to the script location
final_path = Path(__file__).parent.parent / "data" / "scraped_data.csv"

# Save to CSV
df.to_csv(final_path, index=False)

print(f"Yay! The scraped data has been saved to your data folder as 'scraped_data.csv'.")

import requests
import pandas as pd
import get_data

base_url = "https://cars.usnews.com/ajax/inventory/used-cars/search?range=50&price_max=25000&mileage_max=100000&used_checked=1&zip=13142&sort=0"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Referer": "https://cars.usnews.com/used-cars",
    "X-Requested-With": "XMLHttpRequest",
}

car_data = []
total_pages = 500

for page_num in range(1, total_pages + 1):
    if page_num < 2:
        response = requests.get(base_url, headers=headers)
    else:
        response = requests.get(f"{base_url}&page={page_num}", headers=headers)

    try:
        data = response.json()
            # check the data keys
        # print(f"Page {page_num} keys: {list(data.keys())}")
        listings = data.get("data", {}).get("listings", [])

    except Exception as e:
        print(f"Error parsing JSON on page {page_num}: {e}")
        print("Raw response:")
        print(response.text)
        continue

    if not isinstance(listings, list):
        print(f"Unexpected format in listings on page {page_num}")
        continue

    for car in listings:
        if not isinstance(car, dict):
            continue

        # filters
        year = car.get("year", 0)
        body_style = car.get("body_style", "").strip().lower()

        if 2017 <= year <= 2024 and body_style in ["suv", "hatchback"]:
            info = {
                'year': car.get("year", "N/A"),
                'make': car.get('make', 'N/A'),
                'model': car.get('model', 'N/A'),
                'body_style': car.get('body_style', 'N/A'),
                'price': car.get("price", "N/A"),
                'mileage': car.get("mileage", "N/A"),
                'city': car.get("city", "N/A")
            }
            car_data.append(info)
            # checking to make sure reading is correct
            # print(info)

# convert to exportable dataframe
df = pd.DataFrame(car_data)

# export data to output folder
scraped = get_data.export("data","scraped_data.csv")
# df.to_csv(scraped, index=False)
# Car Shopping Analysis  

I have to buy a new car within the next two months. And I'm a data geek, so of course, I needed to make a whole analysis and matching dashboard that would tell me the safest and most fuel-efficient SUV.  


## Steps

I'm not really sure what to put in a README file, so I'll put the steps I followed for this analysis here.

### 1. Exploratory Data Analysis (EDA)

I opened the dataset in Excel to complete some EDA and figure out what the data consisted of. I used the codes provided on the website to understand fields that had confusing names to me.

### 2. Import the data & do some data wrangling

I then cleaned and filtered the data with Pandas, narrowing the search to the parameters I was looking for.

Low-seated sedans make me carsick, and trucks are too expensive, so SUVs are my happy medium. Specifically, I wanted a used car so it would be cheaper (circa 2017–2024), and I needed a gas or hybrid-only vehicle since there aren't many EV charging stations near where I live.

I also wanted a fuel-efficient vehicle with a decent MPG, so I narrowed the search to include only SUVs with a combined city/highway MPG of 23 or higher.

Finally, I wanted to ensure the vehicle I would be driving is safe. I combined the fuel economy data with crash test data from NHTSA, which provided a rating category (out of 5 stars).

### 3. Web Scraping

Next, I found a JSON endpoint API on US News to pull data from, avoiding the need to use an external library like BeautifulSoup or selenium.

I used the pandas `.merge()` function to merge car models from the fuel economy data with dealership listings that were scraped off the web.

### 4. Multi-Attribute Decision Making (MADM) Analysis

Finally, I used a MADM to rank the cars according to my wants and needs. I looked at the top 10 results, their factors, and yes—their appearances because I'm shallow at heart, then decided which one I'd be buying.

Pretty simple car buying process, am I right?

### 5. Visualization

To make it easier to understand and interpret the results, I exported a neat table and bar chart on top of the `.csv` data. 

## Data Sources  

FuelEconomy.gov Web Services

<https://www.fueleconomy.gov/feg/ws/>

National Highway Traffic Safety Administration Datasets and APIs

<https://www.nhtsa.gov/nhtsa-datasets-and-apis#ratings/>

*Disclaimer: Parts of this program were made with the assistance of generative AI. All generated code has been marked within the script files.*  

<https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/>

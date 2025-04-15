# Car Shopping Analysis  

I have to buy a new car within the next two months. And I'm a data geek, so of course, I needed to make a whole analysis and matching dashboard that would tell me the most fuel efficient SUV.  


## Steps

I'm not really sure what to put in a README file, so I'll put the steps I followed for this analysis here.

### 1. Exploratory Data Analysis (EDA)

I opened the dataset in Excel to complete some EDA and figure out what the data consisted of. I used the codes provided on the website to understand fields that had confusing names to me.

### 2. Import the data & do some data wrangling

I then cleaned and filtered the data with Pandas, narrowing the search to the parameters I was looking for.

Low-seated sedans make me carsick, and trucks are too expensive, so SUVs are my happy medium. Specifically, I wanted a used car so it will be cheaper (circa 2017–2024), and I needed a gas or hybrid-only car since there aren't many EV charging stations near where I live.

I also wanted a fuel-efficient vehicle with a decent MPG, so I narrowed the search further to only include SUVs with a combined city/highway MPG of 23 or higher.

### 3. Web Scraping

Next, I used BeautifulSoup to scrape the web for used car prices on each make and model that matched the previous parameters. I had to make sure the cars were nearby so I could actually pick it up, which added a slight obstacle.

I used pandas' `.merge()` function to merge car models from the fuel economy data with dealership listings that were scraped off the web.

### 4. Ranking & Multi-Attribute Decision Analysis

Finally, I ranked the factors according to their importance—fuel efficiency being the most important, followed by price at a close second. I looked at the top ten results, their factors, and yes—their appearances because I'm shallow at heart, then decided which one I'd be buying.

Pretty simple car buying process, am I right?

### 5. Visualization

I couldn't let this hard work go to waste, so I made an interactive dashboard that could go on my portfolio and look pretty. I let the user filter by the various factors and displayed top picks, trends, or trade-offs that came with each model.

## Vehicle Data Source  

FuelEconomy.gov Web Services

<https://www.fueleconomy.gov/feg/ws/>

## Safety Data Sources  

National Highway Traffic Safety Administration Datasets and APIs

<https://www.nhtsa.gov/nhtsa-datasets-and-apis#ratings/>

Insurance Institute for Highway Safety (IIHS) & Highway Loss Data Institute (HLDI)

<https://www.iihs.org/ratings/driver-death-rates-by-make-and-model/>

<https://www.iihs.org/topics/auto-insurance/insurance-losses-by-make-and-model/>


*Disclaimer: Parts of this program were made with the assistance of generative AI. All generated code has been marked within the script files.*  

<https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/>
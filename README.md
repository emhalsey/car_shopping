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

### 4. Ranking & sensitivity analysis

Finally, I ranked the factors according to their importance—fuel efficiency being the most important, followed by price at a close second. I looked at the top ten results, their factors, and yes—their appearances because I'm shallow at heart, then decided which one I'd be buying.

Pretty simple car buying process, am I right?

### 5. Visualization

I couldn't let this hard work go to waste, so I made an interactive dashboard that could go on my portfolio and look pretty. I let the user filter by the various factors and displayed top picks, trends, or trade-offs that came with each model.

## Vehicle Data Source  

FuelEconomy.gov Web Services

<https://www.fueleconomy.gov/feg/ws/>


*Disclaimer: Parts of this program were made with the assistance of generative AI. All generated code has been marked within the script files.*

  
    
      
      

<https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/>

What to Include in your README

1. Project's Title

This is the name of the project. It describes the whole project in one sentence, and helps people understand what the main goal and aim of the project is.

2. Project Description

This is an important component of your project that many new developers often overlook.

Your description is an extremely important aspect of your project. A well-crafted description allows you to show off your work to other developers as well as potential employers.

The quality of a README description often differentiates a good project from a bad project. A good one takes advantage of the opportunity to explain and showcase:

- What your application does,

- Why you used the technologies you used,

- Some of the challenges you faced and features you hope to implement in the future.

3. Table of Contents (Optional)

If your README is very long, you might want to add a table of contents to make it easy for users to navigate to different sections easily. It will make it easier for readers to move around the project with ease.

4. How to Install and Run the Project

If you are working on a project that a user needs to install or run locally in a machine like a "POS", you should include the steps required to install your project and also the required dependencies if any.

Provide a step-by-step description of how to get the development environment set and running.

5. How to Use the Project

Provide instructions and examples so users/contributors can use the project. This will make it easy for them in case they encounter a problem – they will always have a place to reference what is expected.

You can also make use of visual aids by including materials like screenshots to show examples of the running project and also the structure and design principles used in your project.

Also if your project will require authentication like passwords or usernames, this is a good section to include the credentials.

6. Include Credits

If you worked on the project as a team or an organization, list your collaborators/team members. You should also include links to their GitHub profiles and social media too.

Also, if you followed tutorials or referenced a certain material that might help the user to build that particular project, include links to those here as well.

This is just a way to show your appreciation and also to help others get a first hand copy of the project.

7. Add a License

For most README files, this is usually considered the last part. It lets other developers know what they can and cannot do with your project.

We have different types of licenses depending on the kind of project you are working on. Depending on the one you will choose it will determine the contributions your project gets.

The most common one is the GPL License which allows other to make modification to your code and use it for commercial purposes. If you need help choosing a license, use check out this link: https://choosealicense.com/

Up to this point what we have covered are the minimum requirements for a good README. But you might also want to consider adding the following sections to make it more eye catching and interactive.
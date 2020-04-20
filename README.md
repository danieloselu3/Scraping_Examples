# Scraping_Examples
Scraping a few sites using Python

1. ## Scraping Hacker News ##
We’re going to scrape the https://news.ycombinator.com/news front page, using
requests and Beautiful Soup.
Hacker News is a popular aggregator of news articles that “hackers”(computer scientists, entrepreneurs, data scientists) find interesting.

2. ## Scraping Hacker News API ##
Here, instead of scraping the site, we obtain the data from the api provided by the site administrator.
In web scraping, the unwritten rule is to always start with an API, only when there is too much of rate limiting, or when there is no well written API do we settle on scraping the site.

3. ## Scraping Quotes to Scrape ##
We’re going to scrape http://quotes.toscrape.com, using requests and Beautiful Soup.
This page is provided by Scrapinghub as a more realistic scraping playground. Take some time to explore the page.
We’ll scrape out all the information, 
that is:
•	 The quotes, with their author and tags;
•	 And the author information, that is, date and place of birth, and
description.

4. ## Scraping Books to Scrape ##
We’re going to scrape http://books.toscrape.com, using requests and Beautiful Soup.
This page is provided by Scrapinghub as a more realistic scraping playground. 
Take some time to explore the page. We’ll scrape out all the information,
that is, for every book, we’ll obtain:
•	 Its title;
•	 Its image(url);
•	 Its price and stock availability;
•	 Its rating;
•	 Its product description;
•	 Other product information.

import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

def scrape_quotes():
    url = "http://quotes.toscrape.com/"
    response = requests.get(url)

    if response.status_code != 200:
        print("Faild to retrieve the webpage.")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    quotes_data = []

    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:
        text  = quote.find("span", class_="text").get_text()
        author = quote.find("small", class_="author").get_text()
        quotes_data.append([text, author])

    print("\nScraped Quotes:\n")
    print(tabulate(quotes_data, headers=["Quote", "Author"], tablefmt="fancy_grid"))

def scrape_news():
    url = "https://news.ycombinator.com//"
    response = requests.get(url)

    if response.status_code != 200:
        print("faild to retrieve the webpage.")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    news_data = []
    
    titles = soup.find_all("span", class_="titleline")

    for idx, title in enumerate(titles[:10], 1):
        link = title.find("a")
        if link:
            news_data.append([idx, link.get_text(), link['href']])

    print("\nTop Hacker News Headlines:\n")
    print(tabulate(news_data, headers=["#", "tilte", "link"], tablefmt="fancy_grid"))

def main():
    print("Interactive web scraper")
    print("------------------------")
    print("1. Scrape Quotes")
    print("2. Scrape Hacker News")
    choice = input("Enter your choice (1 or 2): ")

    if choice =='1':
        scrape_quotes()
    elif choice == '2':
        scrape_news()
    else:
        print("Invalid choice. please select 1 or 2.")

if __name__ == "__main__":
    main()
import requests
from bs4 import BeautifulSoup
print("Data Scrapping : Successfull")
print("Extracting all the links from the Website : lipsum.com")
print(' ')
def scrape_website(url):
    # Fetch the web page content
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract structured data
        # Here you can write specific code to find and extract the data you need
        # from the HTML structure using BeautifulSoup methods like find(), find_all(), etc.
        
        # Example: Extracting all the links on the page
        links = soup.find_all('a', href=True)
        for link in links:
            print(link['href'])

        # Example: Extracting all paragraphs with a specific class
        paragraphs = soup.find_all('p', class_='some-class')
        for paragraph in paragraphs:
            print(paragraph.text)

    else:
        print(f"Failed to fetch {url}. Status code: {response.status_code}")

# Example usage:
if __name__ == "__main__":
    url = 'https://www.lipsum.com/'  # Replace with the URL of the website you want to scrape
    scrape_website(url)




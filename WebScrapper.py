import requests
from bs4 import BeautifulSoup
import sys
import csv
import json
from urllib.parse import urlparse

def is_valid_url(url):
    """Check if the URL is valid."""
    parsed_url = urlparse(url)
    return bool(parsed_url.scheme and parsed_url.netloc)

def scrape_website(url, element, class_name=None):
    """Scrapes the given website for the specified HTML element and class name."""
    try:
        if not is_valid_url(url):
            print("Error: Invalid URL. Please enter a valid URL.")
            return None

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'lxml')

        results = soup.find_all(element, class_=class_name) if class_name else soup.find_all(element)

        if not results:
            print("No matching elements found.")
            return None
        
        return [item.get_text().strip() for item in results]

    except requests.exceptions.MissingSchema:
        print("Error: Invalid URL format. Please include 'http://' or 'https://'.")
    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the website. Check the URL and your internet connection.")
    except requests.exceptions.Timeout:
        print("Error: The request timed out. Try again later.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")

    return None

def save_results(results, output_format):
    """Saves the results to a file in CSV or JSON format."""
    if not results:
        print("No data to save.")
        return

    filename = f"scraped_results.{output_format}"
    
    if output_format == "csv":
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Scraped Data"])
            for row in results:
                writer.writerow([row])
    elif output_format == "json":
        with open(filename, mode="w", encoding="utf-8") as file:
            json.dump(results, file, indent=4)
    
    print(f"Results saved successfully as {filename}")

def main():
    """Main function to handle command-line arguments and execute the scraper."""
    if len(sys.argv) < 3:
        print("Usage: python scraper.py <URL> <element> [class_name] [csv/json]")
        sys.exit(1)

    url = sys.argv[1]
    element = sys.argv[2]
    class_name = sys.argv[3] if len(sys.argv) > 3 else None
    output_format = sys.argv[4] if len(sys.argv) > 4 else None

    results = scrape_website(url, element, class_name)

    if results:
        print("\nScraping Results:")
        for idx, item in enumerate(results, 1):
            print(f"{idx}. {item}")

        if output_format in ["csv", "json"]:
            save_results(results, output_format)

if __name__ == "__main__":
    main()

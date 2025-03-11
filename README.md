# Web Scraper

A simple Python web scraper that extracts content from a webpage based on a specified HTML element and optional class name. The scraped data can be saved in CSV or JSON format.

## Features
- Fetches and extracts content from a webpage
- Supports filtering by HTML elements and class names
- Saves results in CSV or JSON format
- Handles errors such as invalid URLs, connection issues, and timeouts

## Requirements
Ensure you have Python installed along with the required libraries:
```sh
pip install requests beautifulsoup4 lxml
```

## Usage
Run the script from the command line:
```sh
python scraper.py <URL> <element> [class_name] [csv/json]
```

### Arguments:
- `<URL>`: The webpage to scrape
- `<element>`: The HTML tag to extract (e.g., `p`, `h1`, `div`)
- `[class_name]` (optional): The class name to filter elements
- `[csv/json]` (optional): Save results in CSV or JSON format

### Example:
Extract all paragraph (`p`) elements from a webpage and save results in JSON format:
```sh
python scraper.py https://example.com p json
```

## Output
- Displays the scraped content in the terminal
- Saves data in `scraped_results.csv` or `scraped_results.json` if specified

## Error Handling
- Invalid URLs are detected and reported
- Handles connection errors, timeouts, and invalid responses

## License
This project is open-source and available under the MIT License.


import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def web_scan(url):
    try:
        # Send a GET request to the provided URL
        response = requests.get(url)
        print(f"Scanning URL: {url}")
        print(f"Status Code: {response.status_code}\n")

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract all anchor tags (<a>) with href attributes
        links = [urljoin(url, a['href']) for a in soup.find_all('a', href=True)]

        print(f"Found {len(links)} links on the page:")
        for link in links:
            try:
                # Check the status of each link
                link_response = requests.get(link, timeout=5)
                print(f"[{link_response.status_code}] {link}")
            except requests.exceptions.RequestException as e:
                print(f"[ERROR] Could not reach {link}: {e}")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to scan {url}: {e}")

# Example Usage
if __name__ == "__main__":
    target_url = input("Enter the URL to scan (e.g., https://example.com): ")
    web_scan(target_url)

import os
import requests
from bs4 import BeautifulSoup

# The URL of the website directory
url = "https://infinitearenas.com/xw2/images/artwork/pilots/"
short_url = "https://infinitearenas.com"

# Send a GET request to the URL
response = requests.get(url)
response.raise_for_status()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the links that end with .png, excluding specified patterns
png_links = [
    link.get("href")
    for link in soup.find_all("a")
    if link.get("href").endswith(".png")
    and not link.get("href").endswith("-delta7baethersprite.png")
    and not link.get("href").endswith("Copy.png")
    and not link.get("href").endswith("rebel-fang.png")
]

# Directory to save the images
save_dir = "pilots"
os.makedirs(save_dir, exist_ok=True)

# Download each PNG file
for link in png_links:
    file_name = os.path.join(save_dir, os.path.basename(link))
    file_url = short_url + link
    print(f"Downloading {file_url}...")

    # Send a GET request to the file URL
    file_response = requests.get(file_url)
    file_response.raise_for_status()

    # Save the file
    with open(file_name, "wb") as file:
        file.write(file_response.content)
    print(f"Saved {file_name}")

print("All PNG files have been downloaded.")

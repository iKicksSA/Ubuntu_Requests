

import requests
import os
from urllib.parse import urlparse

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Get URL from user
    url = input("Please enter the image URL: ")
    
    try:
        # Create directory if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)
        
        # Fetch the image
        response = requests.get(url, timeout=60)
        response.raise_for_status()  # Raise exception for bad status codes
        
        # Check if response is actually an image
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print("The provided URL is not an image.")
            return
        
        # Extract filename from URL or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        if not filename:  # if URL ends with slash or no filename, we're creating our own filemane
            ext = content_type.split("/")[-1]  # e.g., jpeg, png
            filename = f"downloaded_image.{ext}"
            
        # Save the image
        filepath = os.path.join("Fetched_Images", filename)
        
        # opening the directory we saved the img into.
        with open(filepath, 'wb') as f:
            f.write(response.content)
            
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        print("\nConnection strengthened. Community enriched.")
        
    except requests.exceptions.MissingSchema:
        print("Invalid URL format. Please include http:// or https://")
    except requests.exceptions.RequestException as e:
        print(f"Connection error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

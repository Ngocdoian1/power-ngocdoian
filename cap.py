import sys
import re
from playwright.sync_api import sync_playwright

def sanitize_filename(url):
    return re.sub(r'\W+', '_', url).strip("_")

def capture_screenshot(url):
    filename = "image.jpg"
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_viewport_size({"width": 1920, "height": 1080})
        page.goto(url, timeout=60000)
        page.screenshot(path=filename)  
        browser.close()
    
    print(f"Screenshot saved: {filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <URL>")
    else:
        capture_screenshot(sys.argv[1])

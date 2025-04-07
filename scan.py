import requests
import threading
import time
import os

PROXY_SOURCES = [
    'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
    'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt',
    'https://openproxylist.xyz/http.txt',
    'https://sunny9577.github.io/proxy-scraper/generated/http_proxies.txt',
    'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
    'https://openproxy.space/list/http',
    'https://proxyspace.pro/http.txt',
    'https://proxyspace.pro/https.txt',
    'https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt',
    'https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt',
    'https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt',
    'https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http_old.txt',
    'https://www.proxy-list.download/api/v1/get?type=https',
    'https://raw.githubusercontent.com/casals-ar/proxy-list/main/http',
    'https://raw.githubusercontent.com/casals-ar/proxy-list/main/https',
    'https://raw.githubusercontent.com/im-razvan/proxy_list/main/http.txt',
    'https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/free.txt',
    'https://raw.githubusercontent.com/elliottophellia/yakumo/master/results/http/global/http_checked.txt',
    'https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt',
    'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt',
    'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt',
    'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt',
    'https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/http/data.txt',
    'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt',
    'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/https_proxies.txt'
]

SUCCESS_FILE = "http.txt"
LOCK = threading.Lock()
live_count = 0
die_count = 0

def fetch_proxies():
    proxies = set()
    for url in PROXY_SOURCES:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                new_proxies = {p.strip() for p in response.text.splitlines() if p.strip()}
                proxies.update(new_proxies)
                print(f"\033[91m[\033[92m#\033[91m] \033[95mSucessfully get beg proxy: \033[93m{len(new_proxies)}")
        except:
            pass
    return list(proxies)

def check_proxy(proxy):
    global live_count, die_count
    start_time = time.time()
    try:
        response = requests.get("http://ip-api.com/json", proxies={"http": f"http://{proxy}", "https": f"http://{proxy}"}, timeout=2)
        latency = round((time.time() - start_time) * 2000)
        if response.status_code == 200:
            data = response.json()
            with LOCK:
                live_count += 1
                with open(SUCCESS_FILE, "a") as f:
                    f.write(proxy + "\n")
            print(f"\033[92mGood proxy \033[91m:: \033[93m{proxy} \033[91m:: \033[97mCountry: \033[93m{data.get('country', 'N/A')} \033[91m:: \033[97mIsp: \033[93m{data.get('isp', 'N/A')} \033[91m:: \033[97mTimezone: \033[93m{data.get('timezone', 'N/A')} \033[91m:: \033[97mTimeout: \033[93m{latency}ms")
        else:
            with LOCK:
                die_count += 1
    except:
        with LOCK:
            die_count += 1

def main():
    global live_count, die_count
    os.system("clear" if os.name == "posix" else "cls")
    proxies = fetch_proxies()
    
    print("\033[93mStart checker in proxy")
    print("\033[93mType\033[97m: http\033[97m/\033[97ms socks4\033[97m/\033[97m5")
    print("\033[93m--------------------------------------")
    
    time.sleep(5)

    threads = []
    for proxy in proxies:
        t = threading.Thread(target=check_proxy, args=(proxy,))
        threads.append(t)
        t.start()
        if len(threads) >= 500:
            for thread in threads:
                thread.join()
            threads.clear()

    for thread in threads:
        thread.join()

    print(f"\033[93mSucessfully checker")
    print(f"\033[93mTotal\033[97m: {len(proxies)}")
    print(f"\033[93mGood\033[97m: {live_count}")
    print(f"\033[93mBad\033[97m: {die_count}")

if __name__ == "__main__":
    main()

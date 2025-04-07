import telebot
import telebot
import psutil

# Thay thế bằng token bot của bạn
BOT_TOKEN = "7263955371:AAHkl6syD_cLbMQISw1cw-GOmPNWG-UMBrk"

# Danh sách người dùng được phép sử dụng lệnh đặc biệt (có thể là ID hoặc username)
AUTHORIZED_USERS = {6033886040, "username1", "username2"}  # Thay ID và username thật vào đây

bot = telebot.TeleBot(BOT_TOKEN)

# Lệnh mặc định
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Chào mừng! Đây là bot Telegram của bạn.")

# Lệnh chỉ dành cho người được ủy quyền
@bot.message_handler(commands=['cac'])
def admin_command(message):
    user_id = message.from_user.id
    username = message.from_user.username

    # Kiểm tra nếu người dùng có trong danh sách được phép
    if user_id in AUTHORIZED_USERS or (username and username in AUTHORIZED_USERS):
        bot.reply_to(message, "Bạn đã truy cập lệnh admin thành công!")
    else:
        bot.reply_to(message, "Bạn không có quyền sử dụng lệnh này.")

@bot.message_handler(commands=['cpu'])
def check_system_info(message):
    user_id = message.from_user.id
    username = message.from_user.username

    if user_id in AUTHORIZED_USERS or (username and username in AUTHORIZED_USERS):
        cpu_percent = psutil.cpu_percent()
        memory_percent = psutil.virtual_memory().percent

        message_text = f"🖥 Thông Tin PC 🖥\n\n" \
                       f"🇻🇳 Admin: NgocDoiAn\n\n" \
                       f"📊 CPU: {cpu_percent}%\n" \
                       f"🧠 Memory: {memory_percent}%"
        bot.reply_to(message, message_text)
    else:
        bot.reply_to(message, "🚫 Bạn không có quyền sử dụng lệnh này!")

# Chạy bot
print("Bot is running...")
bot.polling()
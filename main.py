import telebot
import requests

# TOKEN RESMI DARI BOTFATHER KAMU
TOKEN = '8767587794:AAG2dSMP6adwGFqTa7Q8mWhg5Nk0j28xY5U'
bot = telebot.TeleBot(TOKEN)

# NAMA PENCIPTA (TAMPIL SAAT DITANYA)
PENCIPTA = "Andrey Arsavin"

def get_ai_response(text):
    pertanyaan = text.lower()
    
    # LOGIKA KHUSUS UNTUK MENJAWAB SIAPA PENCIPTANYA
    if any(keyword in pertanyaan for keyword in ["siapa yang buat", "pencipta", "siapa buat", "siapa pembuat"]):
        return f"Aku dibuat oleh sang master, {PENCIPTA}! Dia orangnya keren banget."
    
    try:
        # MENGGUNAKAN API AI UNTUK JAWABAN UMUM (BAHASA INDONESIA)
        url = f"https://api.simsimi.net{text}&lc=id"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()['success']
        else:
            return "Maaf Andrey, otak AI saya sedang loading. Coba tanya lagi ya!"
    except:
        return "Aduh, server AI lagi penuh nih. Tanya lagi sebentar lagi ya!"

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f"Halo! Aku Nexa Bot, asisten cerdas buatan {PENCIPTA}. Silakan tanya apa saja, aku aktif 24 jam!")

@bot.message_handler(func=lambda message: True)
def chat_handler(message):
    # MENAMPILKAN STATUS 'TYPING' DI TELEGRAM AGAR TERLIHAT RESPONSIF
    bot.send_chat_action(message.chat.id, 'typing')
    
    # MENGAMBIL JAWABAN DARI AI
    jawaban = get_ai_response(message.text)
    
    # MENGIRIM JAWABAN KE USER
    bot.reply_to(message, jawaban)

if __name__ == "__main__":
    print(f"--- BOT BUATAN {PENCIPTA.upper()} SEDANG BERJALAN ---")
    bot.infinity_polling()

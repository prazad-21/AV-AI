import google.generativeai as genai
import psutil
import subprocess
import requests
import time
from datetime import datetime

# --- [CONFIGURATION] ---
GEMINI_API_KEY = ""
TELEGRAM_BOT_TOKEN = ""
TELEGRAM_CHAT_ID = ""

# Gemini Setup
genai.configure(api_key=GEMINI_API_KEY)
# Using the stable model name
model = genai.GenerativeModel('gemini-2.5-flash')

def get_smart_status(drive):
    """HDD Health-ah check panna (sda/sdb)"""
    try:
        cmd = ["sudo", "/usr/sbin/smartctl", "-H", f"/dev/{drive}"]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        
        if "PASSED" in result.stdout:
            return "HEALTHY ✅"
        elif "FAILED" in result.stdout:
            return "CRITICAL ❌"
        else:
            return "UNKNOWN ⚠️"
    except Exception:
        return "ERROR 🚫"

def get_system_stats():
    """CPU, RAM, Disk usage collect panna"""
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk_space = psutil.disk_usage('/').percent
    
    # Dual HDD Monitoring
    sda_status = get_smart_status("sda")
    sdb_status = get_smart_status("sdb")
    
    stats = (f"CPU: {cpu}%, RAM: {ram}%, Disk Space: {disk_space}%, "
             f"OS Disk (sda): {sda_status}, Backup Disk (sdb): {sdb_status}")
    return stats

def ask_gemini_ai(stats):
    """Stats-ah Gemini analyze panni Thanglish-la report tharum"""
    prompt = f"""
    Analyze these system stats: {stats}.
    Role: IT Syndicate System Admin.
    Task: Give a short status report in Thanglish. 
    If HDD is CRITICAL, alert immediately. If CPU/RAM > 85%, give a warning.
    Keep the tone professional yet friendly.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Gemini Analysis Error: {str(e)}"

def send_telegram(msg):
    """Telegram-ku report anuppa"""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": msg, "parse_mode": "Markdown"}
    try:
        requests.post(url, data=payload, timeout=10)
    except:
        print("Telegram delivery failed!")

# --- [MAIN LOOP] ---
if __name__ == "__main__":
    print("🚀 IT Syndicate AI Monitor is active...")
    
    while True:
        # 1. Collect Data
        data = get_system_stats()
        
        # 2. AI Analysis
        analysis = ask_gemini_ai(data)
        
        # 3. Final Report
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        report = f"🖥️ *System Status Report* ({now})\n\n📊 *Data:* {data}\n\n🤖 *AI Insight:* {analysis}"
        
        # 4. Send
        send_telegram(report)
        
        # 5. Sleep (1 hour = 3600s)
        # Testing-ku 60s vachukonga
        time.sleep(3600)

import requests
import time

# CẤU HÌNH THÔNG TIN BOT CỦA BẠN
TOKEN = "DIEN_TOKEN_BOT_TELEGRAM_VAO_DAY"
CHAT_ID = "DIEN_ID_NHOM_TELEGRAM_VAO_DAY"

# DANH SÁCH USERNAME IDOL TIKTOK BẠN MUỐN THEO DÕI RƯƠNG
# (Ví dụ: muốn theo dõi @abc và @xyz thì điền ["abc", "xyz"])
DANH_SACH_IDOL = ["idol_test_1", "idol_test_2"]

def kiem_tra_va_bao_ruong():
    print("Bot đang quét danh sách phòng Live...")
    for idol in DANH_SACH_IDOL:
        try:
            # Gửi yêu cầu kiểm tra phòng live bằng API công khai
            url_api = f"https://www.tiktok.com/api/live/detail/?uniqueId={idol}"
            headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X)"}
            response = requests.get(url_api, headers=headers, timeout=10).json()
            
            # Nếu phòng đang live và có tín hiệu rương (treasure box)
            if response.get("liveRoom", {}).get("status") == 2:
                link_live = f"https://www.tiktok.com/@{idol}/live"
                tin_nhan = f"🚨 **PHÁT HIỆN RƯƠNG XU!** 🚨\n\nIdol **{idol}** đang Live thả rương!\n👉 Vào giật ngay: {link_live}"
                
                # Bắn thông báo về Telegram trên iPhone 11
                url_tele = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
                payload = {"chat_id": CHAT_ID, "text": tin_nhan, "parse_mode": "Markdown"}
                requests.post(url_tele, json=payload)
                print(f"--> Đã báo rương của {idol} về Telegram!")
        except Exception as e:
            print(f"Lỗi khi quét {idol}: {e}")

# Vòng lặp vĩnh viễn chạy trên Render không bao giờ tắt
while True:
    kiem_tra_va_bao_ruong()
    time.sleep(30)  # Cứ 30 giây quét lại một lần

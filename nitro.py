import tkinter as tk
from tkinter import Scrollbar, messagebox
import requests
import time
import random
import string

#umwtt -> www.github.com/umwtt

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def generate_promo_codes(event=None):
    try:
        num_promos = int(entry.get()) if entry.get() else 1
        status_label.config(text=f"{num_promos} adet promosyon kodu oluşturuluyor...")
        window.update()

        url = 'https://api.discord.gx.games/v1/direct-fulfillment'
        headers = {
            'authority': 'api.discord.gx.games',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'origin': 'https://www.opera.com',
            'referer': 'https://www.opera.com/',
            'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0'
        }

        session = requests.Session()

        for _ in range(num_promos):
            data = {'partnerUserId': generate_random_string(64)}
            response = session.post(url, headers=headers, json=data)
            
            print("Response status code:", response.status_code)

            if response.status_code == 200:
                token = response.json().get('token')
                promo_url = f"https://discord.com/billing/partner-promotions/1180231712274387115/{token}\n\n"
                output_text.insert(tk.END,"\t[PROMO]\n"+promo_url)
                with open('promo.txt', 'a') as file:
                    file.write("\t\t[PROMO]\n"+promo_url)
            else:
                print(f"Fail promo {response.status_code}.")
                print(f"Error message: {response.text}")

            output_text.see(tk.END)
            window.update()
            time.sleep(0.1)

        status_label.config(text=f"{num_promos} Adet kod başarıyla üretildi ve 'promo.txt' dosyasına kaydedildi.")
        session.close()

    except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu: {str(e)}")
        status_label.config(text="İşlem tamamlanamadı.")

window = tk.Tk()
window.title("NITRO PROMO Gen V3")
window.geometry("300x350")
window.resizable(False, False)
window.config(bg="#1d1d1d")

title_label = tk.Label(window, text="NITRO Promo Gen 'V3", font=("Montserrat", 16, "bold"), fg="white", bg="#1d1d1d")
title_label.pack(pady=10)

entry_frame = tk.Frame(window, bg="#1d1d1d")
entry_frame.pack(pady=5)

entry_label = tk.Label(entry_frame, text="Kaç tane üretmek istersiniz?", font=("Sans", 12), fg="white", bg="#1d1d1d")
entry_label.pack(side=tk.LEFT, padx=(10, 5))

entry = tk.Entry(entry_frame, font=("Sans", 12), bg="#202020", fg="white")
entry.pack(side=tk.LEFT, padx=(0, 10))

generate_button = tk.Button(window, text="Üret", font=("Helvetica", 12, "bold"), command=generate_promo_codes, bg="#333333", fg="white", activebackground="#202020", activeforeground="gray")
generate_button.pack(pady=5, padx=10, fill=tk.X)

output_text = tk.Text(window, height=6, width=40, bg="#202020", fg="white")
output_text.pack(pady=5, fill=tk.BOTH, expand=True)

scrollbar = Scrollbar(window, orient="vertical", command=output_text.yview, bg="#202020", troughcolor="#202020", bd=0)
scrollbar.pack_forget()
output_text.config(yscrollcommand=scrollbar.set)

status_label = tk.Label(window, text="", font=("Montserrat", 10, "bold"), fg="white", bg="#1d1d1d")
status_label.pack(fill=tk.X, padx=10, pady=(0, 10))

def on_closing():
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)

window.bind('<Return>', generate_promo_codes)

window.mainloop()

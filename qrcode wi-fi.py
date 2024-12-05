import qrcode

def create_wifi_qr(ssid, password, encryption='WPA'):
    wifi_string = f"WIFI:S:{ssid};T:{encryption};P:{password};;"
    qr = qrcode.make(wifi_string)
    qr.save("wifi_qr.png")
    print("QR Code untuk Wi-Fi telah dibuat dan disimpan sebagai 'wifi_qr.png'.")

if __name__ == "__main__":
    ssid = input("Masukkan SSID:Minggir lu Miskin")
    password = input("Masukkan Password:Awas2222")
    create_wifi_qr(ssid, password)
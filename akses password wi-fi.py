import subprocess

def get_wifi_passwords():
    # Mengambil daftar semua jaringan Wi-Fi yang tersimpan
    networks = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    
    wifi_list = []
    for network in networks:
        if "All User Profile" in network:
            # Mengambil nama jaringan
            wifi_name = network.split(":")[1][1:-1]
            # Mengambil password untuk jaringan tersebut
            try:
                wifi_password = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi_name, 'key=clear']).decode('utf-8')
                password_line = [line for line in wifi_password.split('\n') if "Key Content" in line]
                if password_line:
                    wifi_list.append((wifi_name, password_line[0].split(":")[1][1:]))
                else:
                    wifi_list.append((wifi_name, "No password"))
            except subprocess.CalledProcessError:
                wifi_list.append((wifi_name, "Error retrieving password"))

    return wifi_list

if __name__ == "__main__":
    wifi_passwords = get_wifi_passwords()
    for wifi in wifi_passwords:
        print(f"SSID: {wifi[0]}, Password: {wifi[1]}")
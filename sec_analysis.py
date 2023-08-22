import pywifi
from pywifi import const

def check_encryption(ssid):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    iface.scan()
    scan_results = iface.scan_results()

    for result in scan_results:
        if result.ssid == ssid:
            if result.akm[0] == const.AKM_TYPE_WPA2PSK:
                return "WPA2-PSK"
            elif result.akm[0] == const.AKM_TYPE_WPAPSK:
                return "WPA-PSK"
            elif result.akm[0] == const.AKM_TYPE_WEP:
                return "WEP"
    
    return "No encryption"

if __name__ == "__main__":
    ssid = "MyNetwork"  # Replace with the SSID of the network to be checked
    encryption = check_encryption(ssid)
    print(f"Encryption of network {ssid}: {encryption}")
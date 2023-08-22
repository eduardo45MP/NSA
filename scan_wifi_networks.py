import wifi
# Allow identification of other interfaces
def scan_wifi_networks():
    # Get information about available Wi-Fi networks
    wifi_list = wifi.Cell.all('wlo1')  # Use 'wlo1' or the name of your Wi-Fi interface

    # Display information about the found networks
    for cell in wifi_list:
        print(f"SSID: {cell.ssid}")
        print(f"BSSID: {cell.address}")
        print(f"Signal Quality: {cell.quality}")
        print(f"Channel: {cell.channel}\n")

if __name__ == "__main__":
    print("Initiating scan of nearby Wi-Fi networks...\n")
    scan_wifi_networks()
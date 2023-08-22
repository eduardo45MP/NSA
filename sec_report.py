def generate_security_report(ssid, encryption, weak_password, common_security):
    report = f"Security Report for Wi-Fi Network: {ssid}\n\n"
    
    if encryption == "No encryption":
        report += "Vulnerability: The network does not use encryption.\n"
    
    if weak_password:
        report += "Vulnerability: Weak password detected.\n"

    if common_security:
        report += "Vulnerability: Common security settings are below recommended standards.\n"

    if not (encryption or weak_password or common_security):
        report += "No security vulnerabilities were found.\n"

    return report

# Example usage:
ssid = "MyNetwork"
encryption = "WPA2-PSK"
weak_password = False
common_security = True

security_report = generate_security_report(ssid, encryption, weak_password, common_security)
print(security_report)
import json

class WifiProfile:
    def __init__(self, ssid, bssid, password):
        self.ssid = ssid
        self.bssid = bssid
        self.password = password

    def __str__(self):
        return f"SSID: {self.ssid}\nBSSID: {self.bssid}\nPassword: {self.password}"

def save_profile(profile, filename):
    with open(filename, 'w') as file:
        json.dump(vars(profile), file)

def load_profile(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        return WifiProfile(**data)

# Create a network profile
profile = WifiProfile(ssid='MyNetwork', bssid='12:34:56:78:90:AB', password='MyPassword')

# Save the profile to a file
save_profile(profile, 'profile.json')

# Load the profile from a file
loaded_profile = load_profile('profile.json')

# Display the loaded profile
print(loaded_profile)
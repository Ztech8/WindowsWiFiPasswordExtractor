import subprocess
import re

ascii_banner = """
 _    _ _       ______ _  ______                                   _   _____     _                  _             
| |  | (_)      |  ___(_) | ___ \                                 | | |  ___|   | |                | |            
| |  | |_ ______| |_   _  | |_/ /_ _ ___ _____      _____  _ __ __| | | |____  _| |_ _ __ __ _  ___| |_ ___  _ __ 
| |/\| | |______|  _| | | |  __/ _` / __/ __\ \ /\ / / _ \| '__/ _` | |  __\ \/ / __| '__/ _` |/ __| __/ _ \| '__|
\  /\  / |      | |   | | | | | (_| \__ \__ \\ V  V / (_) | | | (_| | | |___>  <| |_| | | (_| | (__| || (_) | |   
 \/  \/|_|      \_|   |_| \_|  \__,_|___/___/ \_/\_/ \___/|_|  \__,_| \____/_/\_\\__|_|  \__,_|\___|\__\___/|_|   
                                                                                                                  
                                                                                                                  
"""

def get_wifi_profiles():
    command = 'netsh wlan show profiles'
    output = subprocess.run(command, capture_output=True, text=True, shell=True)
    return output.stdout

def get_wifi_profile_password(profile_name):
    command = f'netsh wlan show profile name="{profile_name}" key=clear'
    output = subprocess.run(command, capture_output=True, text=True, shell=True)
    
    # Use regular expressions to extract the password from the output
    password_match = re.search(r'Key Content\s+:\s+(.*)', output.stdout)
    
    if password_match:
        return password_match.group(1)
    else:
        return "Password not found for the specified profile."

def main():
    print(ascii_banner)
    print("Wi-Fi Profiles:")
    profiles = get_wifi_profiles()
    print(profiles)

    profile_name = input("Enter the profile name to get the password for: ")
    password_output = get_wifi_profile_password(profile_name)
    print("\nPassword Information: ",password_output)
    

if __name__ == "__main__":
    main()

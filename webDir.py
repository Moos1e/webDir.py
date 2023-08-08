import requests

def scan_website_directories(domain):
    base_url = f"https://{domain}/"  
    directories = "wordlist.txt"
    
    with open(directories, "r") as file:
        directories = file.read()

    print(f"Scanning {domain}...")
    existing_directories = []

    for directory in directories:
        url = f"{base_url}{directory}"
        response = requests.get(url)

        if response.status_code == 200:
            existing_directories.append(directory)
            print(f"Directory found: {url}")

    if not existing_directories:
        print("No directories found on this website.")

    print()

if __name__ == "__main__":
    domains_file = "domains.txt"  
    with open(domains_file, "r") as file:
        domains = file.read().splitlines()

    for domain in domains:
        scan_website_directories(domain)
                                          

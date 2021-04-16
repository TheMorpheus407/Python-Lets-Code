import requests

domain = "google.com"
file = open("files/subdomains.txt")
subdomains = []
for i in file.readlines():
    subdomains.append(i.replace('\n', ''))

print(f"------- CHECKING {len(subdomains)} Subdomains -------")
found = []
for sub in subdomains:
    url = f'http://{sub}.{domain}'
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        found.append(sub)
        print(f"[+++] FOUND: {sub}")

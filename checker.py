import requests

try:
    usernames = list(open(input("Username File Path: ")).read().strip().split())
    output = input("Output File Path: ")
    client_id = input("Client ID: ")
except Exception as e:
    print(f"[-] {e}")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Authorization": "OAuth 2-293736-1181042851-tTckEMv1ILnqd",
    "Origin": "https://soundcloud.com",
    "DNT": "1",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Sec-GPC": "1"
}


def checker(username):
    querystring = {"url": f"https://soundcloud.com/{username}", "client_id": f"{client_id}", "app_version": "1666782543", "app_locale": "en"}

    response = requests.get("https://api-v2.soundcloud.com/resolve", headers=HEADERS, params=querystring)
    if response.status_code == 200:
        print(f"{username} is not taken.")
    else:
        print(f"{username} is taken.")


def main():
    for username in usernames:
        checker(username)


if __name__ == "__main__":
    main()

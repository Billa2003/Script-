import requests
from bs4 import BeautifulSoup as bs

url = 'https://n.facebook.com'
xurl = url + '/login.php'

ua = 'Mozilla/5.0 (Linux; Android 4.1.2; GT-I8552 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36'

def login():
    user = input('Username/Email/Number: ')
    pswd = input('Password: ')
    
    req = requests.Session()
    req.headers.update({
        'user-agent': ua,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en_US',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1'
    })

    response_body = req.get(xurl)
    inspect = bs(response_body.text, 'html.parser')

    # HTML देखने के लिए
    print(inspect.prettify())

    # लस्ड एलिमेंट ढूंढें
    lsd_element = inspect.find('input', {'name': 'lsd'})
    if lsd_element:
        lsd_key = lsd_element['value']
    else:
        print("lsd element not found")
        return

    jazoest_element = inspect.find('input', {'name': 'jazoest'})
    if jazoest_element:
        jazoest_key = jazoest_element['value']
    else:
        print("jazoest element not found")
        return

    data = {
        'lsd': lsd_key,
        'jazoest': jazoest_key,
        'email': user,
        'pass': pswd,
        'login': 'submit'
    }

    response_body2 = req.post(xurl, data=data, allow_redirects=True, timeout=300)

    cookie = str(req.cookies.get_dict())
    if 'c_user' in cookie:
        cookies_json = req.cookies.get_dict()
        print("Parsed Cookie JSON:", cookies_json)
    else:
        print('Incorrect details')

if __name__ == '__main__':
    login()
from ytmusicapi import setup

raw_headers = """accept: */*
accept-encoding: gzip, deflate, br, zstd
accept-language: tr,en;q=0.9,en-GB;q=0.8,en-US;q=0.7
authorization: SAPISIDHASH 1772048318_09396379c6f02b0269dc37d046bfe533c90aad37_u SAPISID1PHASH 1772048318_09396379c6f02b0269dc37d046bfe533c90aad37_u SAPISID3PHASH 1772048318_09396379c6f02b0269dc37d046bfe533c90aad37_u
content-encoding: gzip
content-length: 1476
content-type: application/json
cookie: YSC=sCicGKvUFfg; HSID=AgLnGy2iHM-JelShK; SSID=AwI6i8e3JBAN2s3Iw; APISID=_76kdT2Gnb_Xgv7R/AFVnW2AYmvpYic7nU; SAPISID=HBFE44j3jNb530yr/ABQ7rBtt6McIbJPLh; __Secure-1PAPISID=HBFE44j3jNb530yr/ABQ7rBtt6McIbJPLh; __Secure-3PAPISID=HBFE44j3jNb530yr/ABQ7rBtt6McIbJPLh; LOGIN_INFO=AFmmF2swRgIhAM3PhKdyzrw6RmbtTlr2adEj2M69ZqE216QG_J45mBxaAiEAuS5hr7QG2GWReZJN6N9ZIo26oNrtjZzLtygRHkJ6IXo:QUQ3MjNmeUFtUUExM0c3MVZOMElmN1JqU3ZzRndBczh1c19waDBvcnVIZS02emJEYmdIUFZQZ2lPOGZ0OTRoVEJNV2RzNnZRUUhsQVB4UFE5WkJCOVNwelRVM18zekgtaUtrSjk5WUhvUWxuYTJjSGd4dTF4eUxDcFA5ZmF3dmQ5UlRLeVVoTGxpNThkcUV2M0JOUlFaSmY0eFRabXBQbElR; VISITOR_INFO1_LIVE=0O8YApfxwIA; VISITOR_PRIVACY_METADATA=CgJUUhIEGgAgJg%3D%3D; VISITOR_INFO1_LIVE=0O8YApfxwIA; VISITOR_PRIVACY_METADATA=CgJUUhIEGgAgJg%3D%3D; wide=1; SID=g.a0007AhJ7y3wb5n_2hYLWXDXdoWS7IMoP6vUROzeP8fb3ixEeTXmrhnSu8AUFEQPoUO_HcuuhwACgYKAa8SARUSFQHGX2MianFwmhxchnnUI4Yd-7u2PRoVAUF8yKpTJDhNcNDGe8sI1jDvEUDq0076; __Secure-1PSID=g.a0007AhJ7y3wb5n_2hYLWXDXdoWS7IMoP6vUROzeP8fb3ixEeTXmWwyLZ5CbhY-mWo7WstllZwACgYKAe4SARUSFQHGX2MiSJBk78uiyKeD1I4s2meeDxoVAUF8yKpOSiOimb7D-VD_9ZarcQ2c0076; __Secure-3PSID=g.a0007AhJ7y3wb5n_2hYLWXDXdoWS7IMoP6vUROzeP8fb3ixEeTXmAD2OAEGyz51QVxsMuIKjJQACgYKAfcSARUSFQHGX2Mi7vFoiCDrk8zjhGatAx45CBoVAUF8yKojdpGSSsJo8In_YTFMxtO50076; __Secure-YNID=16.YT=3V-mkuv0OTGgeEBRg6kQPjhISIWMR1S8ggSgwp76KCWROjKeZneFw9O3htZ83lMNJM0FvAAy8Sua6rxUNfwecgsp2IbxtodY7aE39o1ua2qm3WCMNX2eVafG6-aJ4TinTK68dEzR3ZF4fPSIVevkiH8o7bdu7tyWbxRPJHUH1ftW9AxgPMMo9Y5YlsazylmdibSHD2NyWpXspxC1IUMxkGHA8xPm4KIhyTHAYy-sTr_Ggi6grGFBoU3jIIZUjHNkejAPV_ShjgQZwDDbBlcmkct9TSpErmryLwtp4ZDfymY7CYr6FwXKKzC6YRlAwcsfvBOOsiOcPLE7UZwrfY5v8g; __Secure-ROLLOUT_TOKEN=CMy2ofrdx9XCPhCu4aS975aMAxjBx7vqwfSSAw%3D%3D; _gcl_au=1.1.225029332.1772018118; PREF=f6=40000080&tz=Europe.Istanbul&f7=150&f4=4000000&repeat=NONE; __Secure-1PSIDTS=sidts-CjQBBj1CYoKfI6seOgHLjIX4RVB2-I8rVJhiedUEDDp9XZzaUpLYfEsaxU38JVo-yDvGKf4kEAA; __Secure-3PSIDTS=sidts-CjQBBj1CYoKfI6seOgHLjIX4RVB2-I8rVJhiedUEDDp9XZzaUpLYfEsaxU38JVo-yDvGKf4kEAA; SIDCC=AKEyXzU6rGDb6Lzs4SA6pyt4PIliTNQIx_V-__krV5jTQqUW3-IOR8xf_Dx5uIliRIzIgDzlXdPf; __Secure-1PSIDCC=AKEyXzVj3dkLvdWFJBbGM3721wHDxhbO9oRmox6NCQ_sOeainyQoEICNJiciGoXTGp7ReABDJqeI; __Secure-3PSIDCC=AKEyXzX0VZGCr3AGi86VQpWAnY4wwXBwI4JdKy2pN9hxHAyB6VN7q3K_96sxZmME23oj340U0vo
origin: https://music.youtube.com
priority: u=1, i
referer: https://music.youtube.com/
sec-ch-ua: "Not:A-Brand";v="99", "Microsoft Edge";v="145", "Chromium";v="145"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "macOS"
sec-fetch-dest: empty
sec-fetch-mode: same-origin
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0
x-goog-authuser: 2
x-goog-visitor-id: CgswTzhZQXBmeHdJQSi8n_3MBjIKCgJUUhIEGgAgJg%3D%3D
x-origin: https://music.youtube.com
x-youtube-bootstrap-logged-in: true
x-youtube-client-name: 67
x-youtube-client-version: 1.20260223.03.00"""

setup(filepath="browser.json", headers_raw=raw_headers)
print("✅ Harika! YENİ browser.json dosyası başarıyla oluşturuldu.")
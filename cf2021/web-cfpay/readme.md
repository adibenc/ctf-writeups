# cf pay

```bash

curl 'http://103.152.242.56:6901/transaction/send/' \
  -H 'Proxy-Connection: keep-alive' \
  -H 'Cache-Control: max-age=0' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'Origin: http://103.152.242.56:6901' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'Referer: http://103.152.242.56:6901/dashboard/' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Cookie: csrftoken=UMppivHdG8JYDtptVrgyc5R3vJAjaQrabYX94NNrW6ZXjeCpfxUAt53PgSGtaUsM; sessionid=4osucdem2n46cnd1haoomqe4wdq3vc8j' \
  --data-raw 'csrfmiddlewaretoken=cYG3nNVItxDdo3hqFU4FBzR1jTfF6rp6taeN951WJvTc4OumZ0IHSz3N42lP6vqI&recipient=adib&amount=50&msg=1&transaction_password=1' \
  --compressed \
  --insecure
  
```

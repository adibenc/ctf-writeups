# Forensic - Vidcap

[304 pts] VidCap
# Description
Found this pcap of my ex's network traffic. I knew they're streaming video but I can't extract it. Can you help me ?

Author: xMaximusKl


Setelah memerika file pcap, terdapat komunikasi rtmp (Real-Time Messaging Protocol), dimana video diakses streaming. Kita extract dengan tcpflow

```
tcpflow -T test.rtmp -r capture.pcapng
```

Lalu kita convert file rtmp ke flv dan jalankan video lewat player.

https://github.com/quo/rtmp2flv


COMPFEST13{aha_gotcha_9437e8f141}
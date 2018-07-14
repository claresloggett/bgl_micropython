from network import WLAN
wlan = WLAN(mode=WLAN.STA)
import machine

ssid = "ssid""
passwd = "passwd"

nets = wlan.scan()
for net in nets:
    if net.ssid == ssid:
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, passwd), timeout=5000)
        while not wlan.isconnected():
            machine.idle() # save power while waiting
        print('WLAN connection succeeded!')
        break

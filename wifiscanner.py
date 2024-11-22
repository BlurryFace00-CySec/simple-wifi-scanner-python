import pywifi
from pywifi import const
import time

def init_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    return iface

def scan_network(iface):
    iface.scan()
    time.sleep(5)
    scan_results = iface.scan_results()
    return scan_results

def display_results(results): 
    for network in results: 
        print(f"SSID: {network.ssid}, Signal: {network.signal}, Auth: {network.akm}")
                                                            
if __name__ == "__main__":
    iface = init_wifi()
    results = scan_network(iface)
    display_results(results)
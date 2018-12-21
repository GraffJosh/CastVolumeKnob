import gc
import uos, machine
import utime as time
import wificonf
import esp

ssid = wificonf.WIFI_SSID 
passw = wificonf.WIFI_PASSWORD 
uos.dupterm(machine.UART(0, 115200), 1)

def timed(func):
    def wrapper():
        start = start = time.ticks_ms() # get millisecond counter
        func()
        delta = time.ticks_diff(time.ticks_ms(), start)
        print("wifi connection time: ", delta, " ms")
    return wrapper

@timed
def do_connect():
    import network
    #import machine

    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, passw)
        while not sta_if.isconnected():
            pass
            #machine.idle()
    print('network config:', sta_if.ifconfig())

gc.collect()
esp.osdebug(None)

do_connect()
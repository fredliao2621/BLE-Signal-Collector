from bluepy.btle import Scanner, DefaultDelegate
from logging.handlers import RotatingFileHandler
from datetime import datetime
from socket import gethostname
import sys, logging, json, requests


class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

logname = datetime.now().strftime('%Y%m%d')+'.log'
logger = logging.getLogger('scan')
logger.setLevel(logging.INFO)
handler = RotatingFileHandler(logname, maxBytes=5000000, backupCount=99999)
logger.addHandler(handler)
logger.addHandler(logging.StreamHandler(sys.stdout))

ble_filter = {
'0000e6b9-0000-1000-8000-00805f9b34fb',
'0000ce9c-0000-1000-8000-00805f9b34fb',
'00002fa9-0000-1000-8000-00805f9b34fb',
'0000190f-0000-1000-8000-00805f9b34fb',
'00000f8e-0000-1000-8000-00805f9b34fb',
'0000efbb-0000-1000-8000-00805f9b34fb',
'000027ef-0000-1000-8000-00805f9b34fb',
'00001a05-0000-1000-8000-00805f9b34fb',
'0000b1fc-0000-1000-8000-00805f9b34fb',
'0000f22e-0000-1000-8000-00805f9b34fb',
'0000dd9b-0000-1000-8000-00805f9b34fb',
'00007dd1-0000-1000-8000-00805f9b34fb',
'0000ccb5-0000-1000-8000-00805f9b34fb',
'0000950b-0000-1000-8000-00805f9b34fb',
'0000fff1-0000-1000-8000-00805f9b34fb'}


while True:
    scanner = Scanner().withDelegate(ScanDelegate())
    devices = scanner.scan(0.3, passive=True)

    for dev in devices:
        uid = dev.getValueText(3)
        if str(uid) == "None":
            continue
        logger.info(datetime.now().isoformat()+'\t'+dev.addr+'\t'+dev.addrType+'\t'+str(dev.rssi)+'\t'+ str(uid))
        
        if uid in ble_filter:
                my_data = {"time":datetime.now().isoformat(),
                           "mac":dev.addr,
                           "type":dev.addrType,
                           "RSSI":str(dev.rssi),
			               "uuid":uid}
                r = requests.post('http://140.116.72.66:9527/sniffer_four', data=my_data)

# Check: Does libusb work

import usb.core
dev = usb.core.find()
print(dev)

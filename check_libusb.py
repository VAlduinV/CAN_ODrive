# Проверка: работает ли libusb

import usb.core
dev = usb.core.find()
print(dev)

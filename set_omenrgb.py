import pywinusb.hid as hid


def sample_handler(data):
    print("Raw data: {0}".format(data))


FILTER = hid.HidDeviceFilter(vendor_id=0x103c, product_id=0x84fd)
hid_device = FILTER.get_devices()
device = hid_device[0]
device.open()
print(hid_device)
target_usage = hid.get_full_usage_id(0xff00, 0x01)
device.set_raw_data_handler(sample_handler)
print(target_usage)

report = device.find_output_reports()

print(report)
print(report[0])

# Customisable Data
buffer = [0x00]*58
buffer[0] = 0x00
buffer[1] = 0x00
buffer[2] = 0x12
buffer[3] = 0x01  # LED Type: Static (0x01), Breathing (0x06), Color Cycle (0x07), Blinking (0x08).
buffer[4] = 0x01
buffer[5] = 0x01
buffer[8] = 0x128  # For custom colore. Change RED Value in RGB. For others modes, then Static leave at 0x00
buffer[9] = 0x00  # For custom colore. Change Green Value in RGB. For others modes, then Static leave at 0x00
buffer[10] = 0x128  # For custom colore. Change Blue Value in RGB. For others modes, then Static leave at 0x00
buffer[48] = 0x64  # Brightness 25% (0x19), 50% (0x32), 75% (0x4b), 100% (0x64)
buffer[49] = 0x0a
buffer[54] = 0x01  # LED Module  - Front LED is 0x01, inside LED Strip (Bar) is 0x02
buffer[55] = 0x01
buffer[56] = 0x01  # Some build-in Themes - Galaxy (0x01), Volcano (0x02), Jungle (0x03), Ocean (0x04)
buffer[57] = 0x02  # Speed Value (0x01), Medium (0x02), Fast (0x03)

print(" ".join(hex(n) for n in buffer))
report[0].send(buffer)

from board import D9
from storage import remount
# import touchio
from digitalio import DigitalInOut, Direction, Pull

USB_access = False

# Pushbutton switch on D9
switch = DigitalInOut(D9)
switch.switch_to_input(Pull.UP)

if not switch.value:
    print('Switch pressed on boot')
    USB_access = not USB_access
else:
    print('Switch NOT pressed on boot')


print('USB_access = ', USB_access)
# If the switch is pressed during boot-up (USB_access = True) CircuitPython can write to the drive via USB (Mu, etc.)
# If the switch is not pressed during boot-up (USB_access = False) CircuitPython can write to the drive from program code
remount("/", USB_access)

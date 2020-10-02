import board
import storage
# import touchio
from digitalio import DigitalInOut, Direction, Pull

USB_access = False

# Pushbutton switch on D3
switch = DigitalInOut(board.D3)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

if not switch.value:
    print('Switch pressed on boot')
    USB_access = not USB_access
else:
    print('Switch NOT pressed on boot')


print('USB_access = ', USB_access)
# If the switch is pressed during boot-up (USB_access = True) CircuitPython can write to the drive via USB (Mu, etc.)
# If the switch is not pressed during boot-up (USB_access = False) CircuitPython can write to the drive from program code
storage.remount("/", USB_access)

#!/usr/bin/env python

import pexpect
import sys
import time

def clamp(val, minval, maxval):
    return min(max(val, minval), maxval)


def pwd2hex(pwd):
    hexkeystring = ""
    for char in pwd:
        hexkeystring += hex(ord(char)) + " "
    return hexkeystring.strip()

# 0 and 1 are off, 100 is max
def brightness2hex(brightness):
    return hex(clamp(brightness, 2, 100))

# the box says 2700 -- 6000 but internally it's 2700 -- 6500
def colour2hex(brightness):
    clamped_colour = clamp(brightness, 2700, 6500)
    high_byte = clamped_colour // 256
    low_byte = clamped_colour - 256 * high_byte
    return str(hex(low_byte)) + ' ' + str(hex(high_byte))

def set_pwd(child, pwd):
    child.sendline("select-attribute 0000ffba-0000-1000-8000-00805f9b34fb")
    child.expect('service')
    child.sendline("write '" + pwd2hex(pwd) + "'")
    time.sleep(2.0)

def set_colour(child, colour):
    child.sendline("select-attribute 0000ffb6-0000-1000-8000-00805f9b34fb")
    child.expect('service')
    child.sendline("write '" + colour2hex(colour)+ "'")
    time.sleep(2.0)

def set_brightness(child, brightness):
    child.sendline("select-attribute 0000ffb8-0000-1000-8000-00805f9b34fb")
    child.expect('service')
    child.sendline("write '" + brightness2hex(brightness) + "'")
    time.sleep(2.0)

 
def main():
    prompt = '#'
    address = '48:70:1E:4E:44:0C'
    pwd = str(1436)
    brightness = 100
    colour = 6500
    child = pexpect.spawn('sudo bluetoothctl')
    child.logfile = sys.stdout.buffer
    child.expect(prompt)
  
    child.sendline('scan on')
    child.expect('Device.*' + address + '.*')
    child.sendline('scan off') 
    # child.expect(prompt)
    
    child.sendline('connect ' + address)
    child.expect('Connection successful')
    child.expect('Characteristic')
    # time.sleep(3.0)
    
    child.sendline('menu gatt')
    child.expect('Menu gatt:')
    
    set_pwd(child, pwd)
    # set_brightness(child, brightness)
    # set_colour(child, colour)
    
    child.sendline("back")
    child.expect(prompt)
    
    child.sendline('disconnect')
    child.expect('Successful disconnected')
    child.expect(prompt)
    
    child.sendline('quit')
    child.expect(pexpect.EOF)


if __name__ == "__main__":
    main()



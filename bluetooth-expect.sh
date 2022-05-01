#!/usr/bin/expect -f

set prompt "#"
set address [lindex $argv 0]

spawn sudo bluetoothctl
expect -re $prompt
# send "remove $address\r"
# sleep 1
expect -re $prompt
send "scan on\r"
expect "Device $address"
# send_user "\nSleeping\r"
# sleep 5
# send_user "\nDone sleeping\r"
send "scan off\r"
# expect "Controller"

send "connect $address\r"
sleep 5

send "menu gatt\r"
expect "Menu gatt:"

#login
send "select-attribute 0000ffba-0000-1000-8000-00805f9b34fb\r"
send "write '0x31 0x34 0x33 0x36'\r"
sleep 2

#brightness
send "select-attribute 0000ffb8-0000-1000-8000-00805f9b34fb\r"
send "write '0x64'\r"
sleep 2

#color
send "select-attribute 0000ffb6-0000-1000-8000-00805f9b34fb\r"
# 2700
# send "write '0x8c 0x0a'\r"
# sleep 1
# 4000
# send "write '0xa0 0x0f'\r"
# 6500
send "write '0x64 0x19'\r"
sleep 2

send "back\r"
send "disconnect\r"
send "quit\r"
expect eof



# python expect script for BLE lamp

## scope

I have an LED lamp by Paulmann where the brightness and colour temperature are
adjustable with either a smartphone app or a dedicated remote control.  When
switching it off and on, it loses its state and resets to max brightness / min
colour temperature.  If I wanted to enjoy 2700 K, I would have bought candles.

I don't think a telephone is a suitable HID for a lamp and long term support is
an open question.  I also don't want an additional piece of hardware lying
around.  In either case, resetting the colour temperature whenever switching a
lamp on is inconvenient.  Very.  Instead, it would be nice to automatically
follow a colour profile during the course of a day (higher temperature during
daytime / early evening and lower towards the late evening).  This should
happen automatically, for example using a cron job.

## usage

After setting the correct lamp address and pwd:

```
./bluetooth-expect.py <brightness> <colour temp>
```

where the brightness is an integer between 2..100 and the colour temperature is
an integer between 2700..6500 (even though the box says 2700..6000).

## issues

The lamp seems to be extremely sensitive towards multiple open connections.  It
can be required to close + exit the telephone app to avoid interference.


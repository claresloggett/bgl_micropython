
A mini micropython project - carried out at SciPy 2018 after Roberto Colistete's [micropython tutorial](https://github.com/rcolistete/MicroPython_Tutorial_SciPy_2018).

This code just retrieves my BGL measurement from a [NightScout server](https://github.com/nightscout/cgm-remote-monitor), and sets the LED colour accordingly.

To use this code, you'll need to set the `ssid` and `passwd` for a wifi network in `boot.py`,
and replace `MY-NIGHTSCOUT-URL` in `main.py`.

This is a little first demo project - you should not use it to monitor your blood sugar! It contains no error checking and there are several conditions that can cause it to give a false result.

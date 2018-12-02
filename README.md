# pybkup2usb

**`pybkup2usb`** is a python module to simplify backing up files to a USB flash drive on any OS platform.

## Quick Start

Install from [GitHub](https://github.com/djacobson/pybkup2usb):

```
$ git clone https://github.com/djacobson/pybkup2usb
$ cd pybkup2usb
```

Run the demo, with and without a USB flash drive plugged into your computer:

```
> python3 demo.py
```

Examine the single line of code in ``demo.py``:

```
retstatus, retmsg = bkup2usb.backup(bkupdir, prefix='MyID')
```

## About

The original objective of this module was to make something surprisingly complex easy, and accomplish the following:

- Automatically discover the path to the first available USB flash drive (if one is plugged in)
- Backup some files to it
- That's it!

Simple right? ...except do this on any OS platform with Python, and abstract away as much complexity as possible. Seriously, all I wanted to do was the above! You'd think something like that would be pretty straight-forward... :/

### To Do

- Version 1, it works. :)
- Ok, I should probably add a CLI for this simple tool. But, It probably deserves more robust (warning: complexity) parameters. This version was literally for a one-push-button backup GUI app.

### Dependencies

For Posix OSs (i.e.: Linux / Ubuntu, Raspbian, MacOS, etc.):

- ``pyudev``
- ``psutil``

For Windows:

- ``pywin32``

### Tests

- Platforms tested: **Python 3.6** on **Raspbian**, **Ubuntu 18.10**, **Windows 10**

### Authors, Contributors, etc.

Version 1 of `pybkup2usb` was designed and written by [David Jacobson](http://blog.jacobsonhome.com/), but, the base functionality is really just an encapsulation of the generous contributions of [Howard Lightstone](https://mail.python.org/pipermail/python-win32/2006-December/005406.html) for the Windows USB code, and the excellent StackExchange answer contributed by [Michael Daffin](https://unix.stackexchange.com/questions/294553/location-of-automounted-usb-devices) and [Arjuna](https://stackoverflow.com/questions/4273252/detect-inserted-usb-on-windows) for the Posix USB code.

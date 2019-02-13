# pybkup2usb

**`pybkup2usb`** is a python module to simplify backing up a folder or file(s) to a USB flash drive on any OS platform.

## Quick Start

Install from [GitHub](https://github.com/djacobson/pybkup2usb):
```
$ git clone https://github.com/djacobson/pybkup2usb
$ cd pybkup2usb
$ pip3 install -e .
```

Run the following command, with and without a USB flash drive plugged into your computer:
```
> bkup2usb stuff_to_backup
```

...or, to run directly from source (i.e.: skipping the ``pip3 install`` above):

```
> python3 -m pybkup2usb stuff_to_backup
```

Add a prefix to your backup target:

```
> bkup2usb stuff_to_backup -p MyID
```

Also, simply type ``bkup2usb -h`` for help with parameters.

Using in your application code is as simple as the following lines of code (prefix is optional):

```
from pybkup2usb import bkup2usb

retstatus, retmsg = bkup2usb.backup(bkupsource, prefix='MyID')
```

## About

The original objective of this module was to make something surprisingly complex easy, and accomplish the following:

- Automatically discover the path to the first available USB flash drive (if one is plugged in)
- Backup some files to it
- That's it!

Simple right? ...except do this on any OS platform with Python, and abstract away as much complexity as possible. Seriously, all I wanted to do was the above! You'd think something like that would be pretty straight-forward... :/

### To Do

- Version 1, it works. :)

- If like me, you are building a dedicated device for a single-purpose app, and interested in using this USB function (i.e.: your app) as the single user interface to the USB flash drive + backup, you may be interested in disabling / suppressing the general desktop feature of automatically launching the File Manager app after inserting and automounting a USB flash drive. Below is a possible solution...

   For Ubuntu:

   ``gsettings set org.gnome.desktop.media-handling automount-open false`` [Credit: ish](https://askubuntu.com/questions/191527/disable-auto-opening-nautilus-window-after-auto-mount)

   I'm still looking for an equivalent solution for Raspbian's Gnome desktop.

### Dependencies

For Posix OSs (i.e.: Linux / Ubuntu, Raspbian, MacOS, etc.):

- ``pyudev``
- ``psutil``

For Windows:

- ``pywin32``

### Tests

- Platforms tested: **Python 3.6** on **Raspbian**, **Ubuntu 18.10**, **Windows 10**

### Authors, Contributors, etc.

Version 1 of `pybkup2usb` was designed and written by [David Jacobson](http://blog.jacobsonhome.com/) ([github](https://github.com/djacobson)), but, the base functionality is really just an encapsulation of the generous public forum contributions of [Howard Lightstone](https://mail.python.org/pipermail/python-win32/2006-December/005406.html) for the Windows USB code, and the excellent StackExchange answer contributed by [Michael Daffin](https://unix.stackexchange.com/questions/294553/location-of-automounted-usb-devices) and [Arjuna](https://stackoverflow.com/questions/4273252/detect-inserted-usb-on-windows) for the Posix USB code.

#!/usr/bin/env python

#
# Script: pybkup2usb/bkup2usb.py Module
#
# Author V1: David Jacobson (david@jacobsonhome.com)

import os
from datetime import datetime
import shutil


def get_usb_paths_windows():
	"""
	Credit:
	https://stackoverflow.com/questions/4273252/detect-inserted-usb-on-windows
	https://mail.python.org/pipermail/python-win32/2006-December/005406.html
	"""
	import win32file
	path_list = None  # []
	drivebits = win32file.GetLogicalDrives()
	for d in range(1, 26):
		mask = 1 << d
		if drivebits & mask:
			# here if the drive is at least there
			drname = '%c:\\' % chr(ord('A') + d)
			t = win32file.GetDriveType(drname)
			if t == win32file.DRIVE_REMOVABLE:
				if not path_list:
					path_list = []
				path_list.append(drname)

	return path_list


def get_usb_paths_posix():
	"""
	Credit:
	https://unix.stackexchange.com/questions/294553/location-of-automounted-usb-devices
	"""
	import pyudev
	import psutil

	path_list = None  # []
	context = pyudev.Context()

	removable = [device for device in context.list_devices(subsystem='block', DEVTYPE='disk') if device.attributes.asstring('removable') == "1"]
	for device in removable:
		partitions = [device.device_node for device in context.list_devices(subsystem='block', DEVTYPE='partition', parent=device)]
		# print("All removable partitions: {}".format(", ".join(partitions)))
		# print("Mounted removable partitions:")
		for p in psutil.disk_partitions():
			if p.device in partitions:
				# print("  {}: {}".format(p.device, p.mountpoint))
				if not path_list:
					path_list = []
				path_list.append(p.mountpoint)

	return path_list


def get_first_usb_path():
	path_list = None
	if os.name == 'nt':
		path_list = get_usb_paths_windows()
	else:
		path_list = get_usb_paths_posix()

	ret_path = None
	if path_list:
		if len(path_list) >= 1:
			ret_path = path_list[0]

	return ret_path


def get_bkup_fname(file_or_folder_name, prefix=None, suffix=None):
	""" <prefix>_<YYMMDD>_<HHMM>_<file_or_folder>_<suffix>
	"""
	sdtnow = datetime.now().strftime("%Y%m%d_%H%M%S")
	path, fbasename = os.path.split(file_or_folder_name)

	fname = "{}_{}".format(sdtnow, fbasename)
	if prefix:
		fname = prefix + '_' + fname
	if suffix:
		fname = fname + '_' + suffix

	return fname


def backup(from_file_or_folder, prefix=None):
	if not os.path.exists(from_file_or_folder):
		return False, 'Path or file [{}] does not exist to backup.'.format(from_file_or_folder)

	usb_path = get_first_usb_path()
	if usb_path:
		# Build dest file or folder name
		to_path = os.path.join(usb_path, get_bkup_fname(from_file_or_folder, prefix))

		# Copy it to removable media path
		try:
			if os.path.isdir(from_file_or_folder):
				shutil.copytree(from_file_or_folder, to_path)
			else:
				shutil.copy2(from_file_or_folder, to_path)
		except (IOError, os.error) as why:
			return False, why

		return True, 'Successfully copied [{}] to [{}]'.format(from_file_or_folder, to_path)
	else:
		return False, 'No Removable mount path found'

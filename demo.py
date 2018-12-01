#
# Script: pybkup2usb/demo.py Module
#
# Author V1: David Jacobson (david@jacobsonhome.com)

import os
from pybkup2usb import bkup2usb


def main():
	bkupdir = os.path.join(os.getcwd(), 'stuff_to_backup')
	retstatus, retmsg = bkup2usb.backup(bkupdir, prefix='MyID')
	print(retmsg)


if __name__ == "__main__":
	main()

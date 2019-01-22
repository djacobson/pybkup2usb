#
# Script: pybkup2usb/runcli.py Module
#
# Author V1: David Jacobson (david@jacobsonhome.com)
# https://github.com/djacobson/pybkup2usb

import os
import argparse

from pybkup2usb import bkup2usb

# from pybkup2usb._version import __version__


def parse_args():
	parser = argparse.ArgumentParser(description='Backup folder or file(s) to USB flash drive')

	parser.add_argument(
		'path_or_files_to_backup',
		help='Folder or file(s) to backup to USB')

	parser.add_argument(
		'-p', '--prefix',
		dest='prefix',
		default=None,
		required=False,
		help='Optional prefix to prepend to backup folder name: <prefix>_<YYMMDD>_<HHMM>_<file_or_folder_name>_<suffix>')

	parser.add_argument(
		'-s', '--suffix',
		dest='suffix',
		default=None,
		required=False,
		help='Optional suffix to append to backup folder name: <prefix>_<YYMMDD>_<HHMM>_<file_or_folder_name>_<suffix>')

	return parser.parse_args()


# Following supports stand-alone execution and
# smooth inclusion into other Py modules
def main():
	args = parse_args()

	bkupsource = args.path_or_files_to_backup
	if len(os.path.dirname(bkupsource)) == 0:
		# Missing path, default to current path
		bkupsource = os.path.join(os.getcwd(), bkupsource)

	retstatus, retmsg = bkup2usb.backup(
		bkupsource,
		prefix=args.prefix,
		suffix=args.suffix)
	print(retmsg)


if __name__ == "__main__":
	main()

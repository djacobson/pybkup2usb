from setuptools import setup

setup(
	name='pybkup2usb',
	version='1.0',
	description='Python module to simplify backing up files to a USB flash drive',
	url='https://github.com/djacobson/pybkup2usb',
	author='David Jacobson',
	author_email='david@jacobsonhome.com',
	license='MIT',
	packages=['pybkup2usb'],
	zip_safe=False,
	entry_points = {
		'console_scripts': ['bkup2usb=pybkup2usb.runcli:main'],
	}
)

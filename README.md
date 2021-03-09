# DV503-Assignment2

## Guide to install TkInter

Tkinter comes pre-installed with the Python installer binaries for Mac OS X and the Windows platform. So if you install Python from the official binaries for Mac OS X or Windows platform, you are good to go with Tkinter.

For Debian versions of Linux you have to install it manually by using the following commands.

For Python 3

sudo apt-get install python3-tk

For Python 2.7

sudo apt-get install python-tk

Linux distros with yum installer can install tkinter module using the command:

yum install tkinter

Verifying Installation

To verify if you have successfully installed Tkinter, open your Python console and type the following command:

import tkinter as tk # for Python 3 version
or

import Tkinter as tk # for Python 2.x version
You have successfully installed Tkinter, if the above command executes without an error.

To check the Tkinter version, type the following commands in your Python REPL:

For python 3.X

import tkinter as tk
tk._test()
For python 2.X

import Tkinter as tk
tk._test()
Note: Importing Tkinter as tk is not required but is good practice as it helps keep things consistent between version.
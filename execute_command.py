#!/usr/bin/env python3

import subprocess

command = "%SystemRoot%\Sysnative\msg.exe * Test"
subprocess.Popen(command, shell=True)
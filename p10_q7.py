#! /usr/bin/env python3
import subprocess

ret = subprocess.run(["ls","-l"])
print(ret)
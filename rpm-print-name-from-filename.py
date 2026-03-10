#!/usr/bin/python3
import libdnf5
import sys

nevra = libdnf5.rpm.Nevra.parse(sys.argv[1], libdnf5.rpm.VectorNevraForm(1, libdnf5.rpm.Nevra.Form_NEVRA)).pop()
print(nevra.get_name())
